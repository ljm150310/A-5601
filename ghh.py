base_url = "https://alidocs.dingtalk.com/i/nodes/YMyQA2dXW79vRra2Trg9xOROJzlwrZgb"
query_param = "utm_scene=person_space"
new_query_param = "value=ncdjcjdwhjjf"

# 如果原URL已经有查询参数，需要在其后加上"&"，如果没有则加上"?"。
separator = "&" if "?" in base_url else "?"
new_url = f"{base_url}{separator}{new_query_param}"

# 如果需要保留原有参数，还需加上原有的参数
if query_param in base_url:
    new_url = f"{base_url}&{new_query_param}"
else:
    new_url = f"{base_url}{separator}{new_query_param}"

print(new_url)
