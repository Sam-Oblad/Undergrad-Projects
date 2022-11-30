In this project, you will download jpegs for flags from all the countries in the world from a public website. The files appear in the following web folder:

https://www.sciencekids.co.nz/images/pictures/flags680/

The names of the files have the following form <country_name>.jpg. For example, the jpeg for the United States is United_States.jpg. The country names are in the input file flags.txt, which is provided for you.
The directory above is protected: you’ll get a 404 error if you try to read the
directory, but it works fine if you add a file name to complete the URL. For example:
https://www.sciencekids.co.nz/images/pictures/flags680/United_States.jpg
Requirements
Write three similar programs that do the following:
Download all flag files into a “flags” subdirectory
Report the total number of bytes downloaded
Report the elapsed execution time of the script using time.perf_counter()
The three versions of the program must be:
flags_seq.py: download flags sequentially, no concurrency
flags_thread.py: use threads, which timeslices on a single core
flags_smp.py: use multiprocessing for multicore parallelism
Use the requests module discussed in class to make the HTTP requests.
Inspect your flags directory after each execution to verify that all the jpegs have been freshly downloaded.
The three corresponding output files must be:
flags_seq.out
flags_thread.out
flags_smp.out
Each output file must have the following format. Your exact numbers will vary, but must be reasonable.

Elapsed time: 10.28958823 
3110197 bytes downloaded