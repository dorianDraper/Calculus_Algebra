import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# linear function of distance = speed * time 
def distance(speed, time):
    return speed * time

speed = 2.5 # m/s this means the object is moving at 2.5 meters per second
time = np.linspace(0, 10, 10)
distance = distance(speed, time)
plt.plot(time, distance)
plt.xlabel('time')
plt.ylabel('distance')
plt.title('distance = speed * time')
plt.show()
# create a dataframe from the above data
df = pd.DataFrame({'time': time, 'distance': distance})
print(df)

# Given the following variables:
# initial_speed = 0, 
# t = time, 
# a = acceleration 
# and equations distance = initial_speed * t + 0.5 * a * (t^2) 
# and speed = initial_speed + a * t 
# find the acceleration value and build the quadratic function (t ∈ [0,10]). Also create a graph and a table.
initial_speed = 0
a = 2
t = np.linspace(0, 10, 100)
distance = initial_speed * t + 0.5 * a * (t**2)
speed = initial_speed + a * t
plt.plot(t, distance)
plt.xlabel('time')
plt.ylabel('distance')
plt.plot(t, speed)
plt.xlabel('time')
plt.ylabel('speed')
plt.show()
df = pd.DataFrame({'time': t, 'distance': distance, 'speed': speed})
print(df)