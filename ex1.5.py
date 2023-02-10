import time
import matplotlib.pyplot as plt

def timing(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return end - start

def func1(n):
    if n == 0 or n == 1:
        return n
    else:
        return func1(n-1) + func1(n-2)

def func2(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = func2(n-1, memo) + func2(n-2, memo)
        return memo[n]

n_values = range(36)
func1_times = [timing(func1, n) for n in n_values]
func2_times = [timing(func2, n) for n in n_values]

plt.plot(n_values, func1_times, label="Original Code")
plt.plot(n_values, func2_times, label="Optimized Code")
plt.legend()
plt.xlabel("n (numbers 0-35)")
plt.ylabel("Time (s)")
plt.show()
