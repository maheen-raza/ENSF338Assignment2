import sys
import json
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    store = []
    storeappend= (low, high)
    store.append(storeappend)
    
    while store:
        low, high = store.pop()
        if low<high:
            pivot = func2(arr, low, high)
            pivotlow = pivot-1
            pivothigh = pivot +1
            lower = (low, pivotlow)
            higher = (high, pivothigh)
            store.append(lower)
            store.append(higher)
    if low< high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi+1, high)

def func2(array, start, end):
    middle = (end-start)//2
    p = array[middle]
    low = start+1
    high = end 
    while True:
        while low <= high and array[high] >= p:
            high = high -1

        while low <= high and array[low] <= p:
            low = low+1

        if low<= high:
            array[low], array[high]=array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

timelist = []
f = open("questiontwo.json")
data = json.load(f)


indice = list()
times = list()

for i in data:
    start = time.time()
    func1(i, 0, len(i)-1)
    end = time.time()
    indice.append(len(i))
    times.append(end-start)

plt.plot(indice, times)
plt.xlabel("Index")
plt.ylabel("Times")
plt.title("QuickSort Times for Arrays")
plt.show()

