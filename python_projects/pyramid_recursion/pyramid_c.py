"""pyramid_c.py"""
from time import perf_counter
import argparse

count = 0
parser = argparse.ArgumentParser()
parser.add_argument("num", type=int)
args = parser.parse_args()
levels = args.num
cache = dict()
cache_hits = 0

def weight_format(r, c):
    answer = weight_on(r,c)
    return "{:.2f}".format(answer)

def weight_on(r, c):
    weight = 200
    global count
    global cache_hits
    count += 1
    rc = (r,c)
    if rc in cache:
        cache_hits += 1
        return cache[rc]
    else:
        if r <= 0:
            data = 0
            cache[rc] = data
            return 0
        elif c == 0:
            data = (weight + weight_on(r-1, c))/2
            cache[rc] = data
            return data
        elif r == c:
            data = (weight + weight_on(r-1, c-1))/2
            cache[rc] = data
            return data
        else:
            data = (weight + 200 + weight_on(r-1, c-1) + weight_on(r - 1, c)) / 2
            cache[rc] = data
            return data

def main():
    r = 0
    c = 0
    index = 1
    row = " "

    with open("part3.out", "w") as file:
        file.write('')

    start = perf_counter()
    for _ in range(levels):
        if index > levels:
            break
        for _ in range(index):
            weight = weight_format(r, c)
            row += " " + weight
            c += 1
        with open("part3.out", "a") as file:
            file.write(row + '\n')
            file.close()
        print(row)
        row = ' '
        index += 1
        r += 1
        c = 0
    end = perf_counter()


    print(f"Elapsed time: {end - start:.8f} seconds")
    print(f"Number of function calls: {count}")
    print(f"Cache hits: {cache_hits}")
    with open("part3.out", "a") as file:
        file.write(f"Elapsed time: {end - start:.8f} seconds\n")
        file.write(f"Number of function calls: {count}\n")
        file.write(f"Cache hits: {cache_hits}")
        file.close()

if __name__ == "__main__":
    main()