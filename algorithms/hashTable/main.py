import time
import sys 
from hashmap import HashMap
from decimal import Decimal, ROUND_HALF_UP
# Part 1 -- Write weight_on_cacheless() method
count = 0
cache = HashMap()
cache_hits = 0

def resetCount():
    global count
    count = 0
def weight_on_cacheless(r, c):
    global count
    count += 1
    if r <= 0:
        return 0
    
    elif c == 0:
        return round(200 + weight_on_cacheless(r-1, c), 2) / 2
    
    elif r == c:
        return round(200 + weight_on_cacheless(r-1, c-1), 2) / 2
    
    else:
        left = weight_on_cacheless(r-1, c-1)
        right = weight_on_cacheless(r-1, c)
        left = round(left, 2)
        right = round(right, 2)
        return round((200 + 200 + left + right) / 2, 2)
       

# Part 3 -- Write weight_on_with_caching() method
def weight_on_with_caching(r, c):
    global count
    global cache_hits
    count += 1
    rc = (r, c)
    weight = 200
    try: 
        cache[rc]
        cache_hits += 1
        return cache[rc]
    except KeyError:
        if r <= 0:
            data = 0
            cache[rc] = data
            return 0
        elif c == 0:
            data = round((200 + weight_on_with_caching(r - 1, c)) / 2, 2)
            cache[rc] = data
            return data
        elif r == c:
            data = round((200 + weight_on_with_caching(r - 1, c - 1)) / 2, 2)
            cache[rc] = data
            return data
        else:
            left = weight_on_with_caching(r - 1, c - 1)
            right = weight_on_with_caching(r - 1, c)
            left = round(left, 2)
            right = round(right, 2)
            data = round((200 + 200 + left + right) / 2, 2)
            cache[rc] = data
            return data

def main():
    # Part 2 -- Use weight_on_cacheless() method
    # Cacheless
    print("Cacheless:")
    start = time.perf_counter()
    i = 0
    num = int(sys.argv[1])
    f = open("cacheless.txt","w")
    print()
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format(weight_on_cacheless(i,j)) + " "
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    print(f"Number of function calls: {count}")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    f.close()
    
    # Part 3 -- Use weight_on_with_caching() method, with your HashMap ADT
    resetCount()
    start = time.perf_counter()
    i = 0
    num = int(sys.argv[1])
    f = open("with_caching.txt","w")
    print()
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_with_caching(i,j))) + " "
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    print(f"Number of function calls: {count}")
    print(f"Number of cache hits: {cache_hits}")

    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    f.close()

if __name__=="__main__":
    main()
