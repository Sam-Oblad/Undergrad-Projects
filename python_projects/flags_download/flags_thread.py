"""flags_thread.py"""
import os
import requests
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor

url = "https://www.sciencekids.co.nz/images/pictures/flags680/"
flags = []
urls = []
items = 0

with open("flags.txt", 'r') as file:
    for line in file:
        flags.append(line.strip() + ".jpg")

for flag in flags:
    urls.append(url + flag)

def download_flag(url):
    fresp = requests.get(url)
    url_list = url.split("/")
    fname = url_list[-1]
    if not fresp:
        raise Exception(f"Can not download {fname}")
    
    if not os.path.exists("/Users/samoblad/files/portfolio/python_projects/flags_download/flags"):
        os.mkdir("/Users/samoblad/files/portfolio/python_projects/flags_download/flags")

    with open(f"flags/{fname}", "wb") as wf:
        wf.write(fresp.content)
        num_bytes = len(fresp.content)
        size.append(int(num_bytes))
        items.append(1)

if __name__ == "__main__":
    size = []
    items = []
    start = perf_counter()
    with ThreadPoolExecutor() as th:
        res = th.map(download_flag, urls)

        
    end = perf_counter()
    timer = (end - start)
    print(f"Total time elapsed: {timer}")
    print(f"Total number of bytes downloaded: {sum(size)}")
    print(f"total items downloaded: {sum(items)}")
    with open("flags_thread.out", "w") as file:
        file.write(f"Total number of bytes downloaded: {sum(size)}\n")
        file.write(f"Total time elapsed: {timer} (s)\n")
        file.write(f"total items downloaded: {sum(items)}")
    file.close()
