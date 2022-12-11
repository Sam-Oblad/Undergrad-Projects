"""pyramid.py"""
from time import perf_counter
import argparse

count = 0
parser = argparse.ArgumentParser()
parser.add_argument("num", type=int)
args = parser.parse_args()
levels = args.num

def weight_format(r, c):
    answer = weight_on(r,c)
    return "{:.2f}".format(answer)

def weight_on(r, c):
    weight = 200
    global count
    count += 1
    if r <= 0:
        data = 0
        return 0
    elif c == 0:
        data = (weight + weight_on(r-1, c))/2
        return data
    elif r == c:
        data = (weight + weight_on(r-1, c-1))/2
        return data
    else:
        data = (weight + 200 + weight_on(r-1, c-1) + weight_on(r - 1, c)) / 2
        return data

def main():
    r = 0
    c = 0
    index = 1
    row = " "

    with open("part2.out", "w") as file:
        file.write('')

    start = perf_counter()
    for _ in range(levels):
        if index > levels:
            break
        for _ in range(index):
            weight = weight_format(r, c)
            row += " " + weight
            c += 1
        with open("part2.out", "a") as file:
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
    with open("part2.out", "a") as file:
        file.write(f"Elapsed time: {end - start:.8f} seconds\n")
        file.write(f"Number of function calls: {count}\n")
        file.close()

if __name__ == "__main__":
    main()