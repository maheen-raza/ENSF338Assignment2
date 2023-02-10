
import json
import sys
import matplotlib.pyplot as plt
import numpy as np
import threading 
from threading import stack_size
stack_size(33554432)

from time import perf_counter
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:

            break
    array[start], array[high] = array[high], array[start]
    return high
# Load the input arrays from the JSON file
with open("questiontwo.json") as f:
    data = json.load(f)
    #inputs = data["inputs"]

# Sort each input array and print the result
timingresult = []
for arr in data:
    timestart = perf_counter()
    low = 0
    high = len(data) - 1
    
    func1(arr, low, high)
    timestop = perf_counter()
    timingresult.append(timestop-timestart)


print(data)
print(timestop-timestart)
plt.plot(timingresult)
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.show()

with open("sorted.json", "w") as outfile:
   json.dump(data, outfile)


"""
Average-case time complexity: O(n log n)
"""
