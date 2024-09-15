import some_module


def some_function():
    some_module.install(some_package)

someimport some_module
import some_module

def some_function():
    some_module.install(some_package)

some_function()


def some_function():
    some_module.install(some_package)

some_function()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def update_clock(num, scatter):
    current_time = time.localtime()
    seconds = current_time.tm_sec + (current_time.tm_min * 60) + (current_time.tm_hour * 3600)
    seconds %= 3600  # Keep it within one hour

    # Calculate positions of the hands
    second_angle = (seconds % 60) * 6 + 90
    minute_angle = ((seconds // 60) % 60) * 6 + 90
    hour_angle = (((seconds // 3600) % 12) * 30) + ((seconds // 60) % 60) * 0.5 + 90

    # Set the position of the hands
    scatter.set_offsets([(0, 0), (0.9 * np.cos(np.deg2rad(second_angle)), 0.9 * np.sin(np.deg2rad(second_angle))),
                         (0.7 * np.cos(np.deg2rad(minute_angle)), 0.7 * np.sin(np.deg2rad(minute_angle))),
                         (0.5 * np.cos(np.deg2rad(hour_angle)), 0.5 * np.sin(np.deg2rad(hour_angle)))])
    
    return scatter,

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.axis('off')  # Turn off axes
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Create a scatter plot for the clock hands
scatter = ax.scatter([], [], s=100, c=['r', 'b', 'g'], alpha=0.6)

# Create an animation
ani = animation.FuncAnimation(fig, update_clock, fargs=[scatter], interval=1000)

plt.show()
