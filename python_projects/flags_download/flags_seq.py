"""flags_seq.py"""
import os
from time import perf_counter
import requests
from random import randint
from concurrent.futures import ThreadPoolExecutor


url = "https://www.sciencekids.co.nz/images/pictures/flags680/"
flag_folder_path = "/Users/samoblad/files/projects/flags"
flags = []
items = 0

with open("flags.txt", 'r') as file:
    for line in file:
        flags.append(line.strip() + ".jpg")
        items += 1

def download_flag(url, flag):
    url = url + flag
    fresp = requests.get(url)
    if not fresp:
        raise Exception(f"Can not download {flag}")
    if not os.path.exists("/Users/samoblad/files/projects/flags"):
        os.mkdir("/Users/samoblad/files/projects/flags")
    os.chdir("/Users/samoblad/files/projects/flags")
    fp = open(flag, 'wb')
    fp.write(fresp.content)
    num_bytes = len(fresp.content)
    fp.close()
    os.chdir("/Users/samoblad/files/projects")
    return num_bytes

def download_flags(selected_flags: list):
    start = perf_counter()
    num_bytes = 0
    items = 0
    for flag in selected_flags:
        items += 1
        download_flag(url, flag)
        num_bytes += download_flag(url, flag)
    end = perf_counter()
    timer = (end - start)
    print(f"Total time elapsed: {timer}")
    print(f"Total number of bytes downloaded: {num_bytes}")
    print(f"total items downloaded: {items}")
    with open("flags_seq.out", "w") as file:
      file.write(f"Total number of bytes downloaded: {num_bytes}\n")
      file.write(f"Total time elapsed: {timer} (s)\n")
      file.write(f"total items downloaded: {items}")
    file.close()


download_flags(flags)

