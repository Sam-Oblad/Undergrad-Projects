This project is based on actual work done for the Department of Homeland Security. The goal is to detect the presence of dangerous materials, such as in a point of entry at an airport or other location. All items pass through a scanner which reports certain radioactive emissions as voltage spikes. The software takes the digitized voltage measurements and examines them for such spikes.

The raw data is quite jagged, so we apply a smoothing filter before analyzing it. The filter generates a new sequence of numbers obtained as follows: starting with the 4th entry and ending with the 4th from the last entry, replace each entry with a weighted average of itself and the six points around it. Let   yi  be the point to be smoothed. The following formula implements our filter:

floor((yi−3+2yi−2+3yi−1+3yi+3yi+1+2yi+2+yi+3)/15) 

In our new sequence of smoothed data, the center point   yi  of every interval of seven points is replaced by applying the formula above. The first and last 3 data values are left unchanged from the original raw data, since there aren’t enough points before or after them to use the smoothing formula. The original data array is left unchanged. Here is a plot of the smoothed data:
image of smoothed data
It is better to use the smoothed data for detecting pulses.
Requirements
In this project, you will process all of the files in the current folder with a “.dat” suffix in the file name.

For each such file, you will:
Read the data into an array of integers using numpy.loadtxt
Generate smoothed data into another array of integers
Find the beginning of each pulse by examining the smoothed data
Compute the area of each pulse using the raw data
Graph both the raw and smoothed data on the same plot, each with their own axis
Detect a pulse by looking for a “rise” over three consecutive points,   yi,yi+1,yi+2 . The rise is   𝑦i+2−yi . If the rise exceeds a certain "voltage threshold", where   vt=100 , then a pulse begins at position   i . Record this position. After finding a pulse start position, advance through the data starting at   yi+2  until the samples start to decrease before looking for the next pulse.
To compute the area of a pulse, start at the beginning of the pulse and add the next 50 raw   y  values together. If the next pulse starts in less than 50 values, stop adding at that point.

For each file, plot both sets of data in a single plot and save it to a file. For example, one of the files is named 2_Record2308.dat, so you will store your plots in the file 2_Record2308.pdf, etc..

Do not hard code the file names (see main below). You will also write the original file name, pulse start positions, and corresponding areas to the file 2_Record2308.out. If your computations are correct, the following will appear in 2_Record2308.out: