"""flags_smp.py"""
import os
import requests
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor

def download_flag(url):
        fresp = requests.get(url)
        url_list = url.split("/")
        fname = url_list[-1]
        if not fresp:
            raise Exception(f"Can not download {fname}")
        
        if not os.path.exists("/Users/samoblad/files/projects/flags"):
            os.mkdir("/Users/samoblad/files/projects/flags")

        with open(f"flags/{fname}", "wb") as wf:
            wf.write(fresp.content)
            num_bytes = len(fresp.content)
        return(num_bytes)


if __name__ == "__main__":
    
    items = 0
    size = 0
    url = "https://www.sciencekids.co.nz/images/pictures/flags680/"
    urls = []
    flags = []

    with open("flags.txt", 'r') as file:
        for line in file:
            flags.append(line.strip() + ".jpg")

    for flag in flags:
        urls.append(url + flag)

    items = len(flags)

    for url in urls:
        fresp = requests.get(url)
        size += len(fresp.content)

    start = perf_counter()
    with ProcessPoolExecutor() as p:
        res = p.map(download_flag, urls)
    end = perf_counter()

    timer = (end - start)
    print(f"Total time elapsed: {timer}")
    print(f"Total number of bytes downloaded: {(size)}")
    print(f"total items downloaded: {(items)}")
    with open("flags_smp.out", "w") as file:
        file.write(f"Total number of bytes downloaded: {(size)}\n")
        file.write(f"Total time elapsed: {timer} (s)\n")
        file.write(f"total items downloaded: {(items)}")
    file.close()


"""When I tried to append the byte and item amounts to a list
like I did in my thread.py, I could not get it to work the same. It would quit before
downloading the flags. The only way I could calculate it was to do it one by one after 
I did the normal process executor
"""