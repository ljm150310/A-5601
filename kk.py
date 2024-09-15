import os
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import asyncio
from aiohttp import ClientSession
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 数据库引擎初始化
engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(bind=engine)

Base = declarative_base()

# 定义 VerificationCode 模型
class VerificationCode(Base):
    __tablename__ = 'verification_codes'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String, nullable=False)
    code = Column(String, nullable=False)
    expiry_time = Column(DateTime, nullable=False)

# 数据库交互抽象
def db_session_scope():
    """提供一个数据库会话范围的上下文管理器"""
    session = Session()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        logging.error(f"Database error: {e}")
        raise
    finally:
        session.close()

# 异步发送短信
async def async_send_sms(phone_number, code, sms_api_url, api_key):
    """异步发送短信"""
    try:
        async with ClientSession() as session:
            url = f"{sms_api_url}?phone={phone_number}&code={code}&key={api_key}"
            async with session.get(url) as response:
                if response.status != 200:
                    logging.error(f"Failed to send SMS to {phone_number}. Status: {response.status}")
    except asyncio.TimeoutError:
        logging.error(f"Timeout occurred while sending SMS to {phone_number}")
    except Exception as e:
        logging.error(f"An error occurred while sending SMS to {phone_number}: {e}")

# 生成验证码并存储到数据库，同时异步发送短信
def generate_and_store_verification_code(phone_number, sms_api_url, api_key):
    """生成验证码并存储到数据库，同时异步发送短信"""
    with db_session_scope() as session:
        code = ''.join(str(random.randint(0, 9)) for _ in range(6))
        expiry_time = datetime.now() + timedelta(minutes=5)
        new_code = VerificationCode(phone_number=phone_number, code=code, expiry_time=expiry_time)
        session.add(new_code)
    
    # 异步发送验证码
    asyncio.create_task(async_send_sms(phone_number, code, sms_api_url, api_key))
    return code

# 验证验证码
def verify_code(phone_number, user_code):
    with db_session_scope() as session:
        stored_code = session.query(VerificationCode).filter_by(phone_number=phone_number).first()
        if stored_code and stored_code.code == user_code and stored_code.expiry_time > datetime.now():
            return True
    return False
    