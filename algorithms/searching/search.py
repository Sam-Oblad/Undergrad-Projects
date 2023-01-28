#search.py
import random
import math
import time
        
def rand_list(size_val):
    L = range(size_val)
    myList = []
    for i in range(size_val):
        myList.append(random.choice(L))
        myList.sort()
    return myList

def linear_search(Lyst, target):
    start = time.perf_counter()
    calls = 0
    for i in range(len(Lyst)):
        calls += 1
        if Lyst[i] == target:
            end = time.perf_counter()
            timer = "%.3f" % ((end - start) * 1000000)
            return (True, calls, f"Time Elapses: {timer} Microseconds")
    end = time.perf_counter()
    timer = "%.3f" % ((end - start) * 1000000)
    return (False, calls, f"Time Elapses:  {timer} Microseconds")
def test_linear(test_list, target):
    print(linear_search(test_list, target))

def binary_search(lyst, target):
    start = time.perf_counter()
    calls = 0
    low = 0
    mid = 0
    high = len(lyst) - 1
    while low <= high:
        calls += 1
        mid = (high + low) // 2
        
        if lyst[mid] < target:
            low = mid + 1
        elif lyst[mid] > target:
            high = mid - 1
        else:
            end = time.perf_counter()
            timer = "%.3f" % ((end - start) * 1000000)
            return (True, calls, f"Time Elapses: {timer} Microseconds")
    end = time.perf_counter()
    timer = "%.3f" % ((end - start) * 1000000)
    return (False, calls, f"Time Elapses:  {timer} Microseconds")
def test_binary(test_list, target):
    print(binary_search(test_list, target))

def jump_search(arr, x):
    start = time.perf_counter()
    calls = 0
    n = len(arr)
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        calls += 1
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            end = time.perf_counter()
            timer = "%.3f" % ((end - start) * 1000000)
            return (False, calls, f"Time Elapses:  {timer} Microseconds")
    while arr[int(prev)] < x:
        calls += 1
        prev += 1
        if prev == min(step, n):
            end = time.perf_counter()
            timer = "%.3f" % ((end - start) * 1000000)
            return (False, calls, f"Time Elapses:  {timer} Microseconds")
    if arr[int(prev)] == x:
            end = time.perf_counter()
            timer = "%.3f" % ((end - start) * 1000000)
            return (True, calls, f"Time Elapses: {timer} Microseconds")
    end = time.perf_counter()
    timer = "%.3f" % ((end - start) * 1000000)
    return (False, calls, f"Time Elapses:  {timer} Microseconds")
def test_jump(test_list, target):
    print(jump_search(test_list, target))


def main():
    myList = rand_list(1000)

    print("\nLinear Test:")
    test_linear(myList, 151)

    print("\nJump_search Test")
    test_jump(myList, 151)

    print("\nBinary Test")
    test_binary(myList, 151)
    print('\n')
if __name__ == "__main__":
    main()