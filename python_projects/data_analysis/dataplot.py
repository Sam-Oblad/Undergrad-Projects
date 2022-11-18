"""dataplot.py"""
import numpy as np
from matplotlib import pyplot as plt
import glob

def filter_data(file):
    file = np.loadtxt(file, dtype = np.int32)
    copy_file = file
    length = int(copy_file.size) - 6 #skip 0:4 and -3:-1
    filtered_points = np.array([])
    for _ in range(length):
        six_nums = copy_file[0:7]
        filtered_point = int((six_nums[0]+(2*six_nums[1])+(3*six_nums[2])+(3*six_nums[3])+(3*six_nums[4])+(2*six_nums[5])+(six_nums[6]))/15)
        filtered_points = np.append(filtered_points, filtered_point)
        copy_file = np.delete(copy_file, [0])
    filtered_points = filtered_points.astype('int32')
    return filtered_points

def analyze(file):
    rawdata = np.loadtxt(file, dtype = np.int32)
    smoothdata = filter_data(file)
    pulses = np.array([])
    i = 0
    vt = 100
    pulse_dict = {}
    while i < len(smoothdata) - 2:
        if (smoothdata[i+2] - smoothdata[i]) > vt:
            pulses = np.append(pulses, i + 3)
            i += 1
            while i < len(smoothdata) - 2 and (smoothdata[i+1] > smoothdata[i]):
                i += 1
        i += 1
    pulses = pulses.astype(np.int32)

    for _ in pulses:
        if pulses.size > 1:
            if pulses[1] - pulses[0] > 50:
                area = 0
                i = pulses[0]
                for _ in range(50):
                    area += rawdata[i]
                    i += 1
                pulse_dict[pulses[0]] = area
                pulses = np.delete(pulses, [0])
            else:
                area = 0
                i = pulses[0]
                iters = pulses[1] - pulses[0]
                for _ in range(iters):
                    area += rawdata[i]
                    i += 1
                pulse_dict[pulses[0]] = area
                pulses = np.delete(pulses, [0])
        else:
            area = 0
            i = pulses[0]
            for _ in range(50):
                area += rawdata[i]
                i += 1
            pulse_dict[pulses[0]] = area

    file_out = open(file.replace('dat', 'out'), "w")
    i = 1
    file_out.write(f"{file}\n")
    for key, value in pulse_dict.items():
        file_out.write(f"Pulse {i}: {key} ({value})\n")
        i += 1

    count = int(rawdata.size) + 1
    x_1 = np.arange(1, count)
    y_1 = rawdata
    count = int(smoothdata.size) + 1
    x_2 = np.arange(1, count)
    y_2 = smoothdata
    plt.title(f"{file}")
    plt.xlabel("Measurement")
    plt.ylabel("Voltage")
    plt.plot(x_1, y_1, color ="black")
    plt.plot(x_2, y_2, color = "green")
    plt.savefig(f"{file}.pdf", format = "pdf")
    plt.close()
    
def main(): 
   for fname in glob.glob('*.dat'): 
        analyze(fname)

if __name__ == '__main__':
    main()
