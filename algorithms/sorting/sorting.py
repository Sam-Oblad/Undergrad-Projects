from random import seed, sample
DATA_SIZE = 10
seed(0) 
DATA = sample(range(DATA_SIZE * 3), k=DATA_SIZE) 
test = DATA.copy() # don't sort DATA, sort a copy of DATA 

def reset():
    global test
    test = DATA.copy()

def is_sorted(lyst):
    compareLyst = sorted(lyst)
    for num in lyst:
        if not type(num) is int:
            raise TypeError
    if lyst == compareLyst:
        return True
    else:
        return False

def quicksort(numbers):
    comps = 0
    swaps = 0
    def partition(numbers, start_index, end_index, comps, swaps):
        # Select the middle value as the pivot.
        midpoint = start_index + (end_index - start_index) // 2
        pivot = numbers[midpoint]
    
        # "low" and "high" start at the ends of the list segment
        # and move towards each other.
        low = start_index
        high = end_index
    
        done = False
        while not done:
            
            # Increment low while numbers[low] < pivot
            while numbers[low] < pivot:
                low = low + 1
                comps += 1

        
            # Decrement high while pivot < numbers[high]
            while pivot < numbers[high]:
                high = high - 1
                comps += 1

            if low >= high:
                done = True
            else:
                swaps += 1
                temp = numbers[low]
                numbers[low] = numbers[high]
                numbers[high] = temp
                low = low + 1
                high = high - 1

        return (high, comps, swaps)

    def sort(numbers, start_index, end_index, comps, swaps):
        if end_index <= start_index:
            return
        high = partition(numbers, start_index, end_index, comps, swaps)
        sort(numbers, start_index, high[0], high[1], high[2])
        sort(numbers, high[0] + 1, end_index, high[1], high[2])
        return (numbers, high[1], high[2])
    if not type(numbers) is list:
        raise TypeError
    size = len(numbers)
    result = sort(numbers, 0, size - 1, comps, swaps)
    return result

def mergesort(lyst):
    comps = 0
    swaps = 0
    def sort(numbers, i, k, comps, swaps):
        j = 0
        
        if i < k:
            j = (i + k) // 2 #find midpoint in partition
            
            #Recursively sort left and right partitions
            sort(numbers, i, j, comps, swaps)
            sort(numbers, j + 1, k, comps, swaps)
            
            #merge left and right partition in sorted order
            compsSwaps = merge(numbers, i, j, k, comps, swaps)
            
            return(numbers, compsSwaps[0], compsSwaps[1])
        
        
    def merge(numbers, i, j, k, comps, swaps):
        merged_size = k - i + 1
        merged_numbers = [0] * merged_size
        
        merge_pos = 0
        left_pos = i
        right_pos = j + 1
        
        #Add smallest element from left or right partition to merged nums
        while left_pos <= j and right_pos <= k:
            if numbers[left_pos] <= numbers[right_pos]:
                merged_numbers[merge_pos] = numbers[left_pos]
                left_pos += 1
                comps += 1
            else:
                merged_numbers[merge_pos] = numbers[right_pos]
                right_pos += 1
                comps += 1
            merge_pos += 1
            
        # if left partition is not empty, add remaining elements to merged nums
        while left_pos <= j:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
            merge_pos += 1
            
        # if right partition is not empty, add remaining elements to merged nums
        while right_pos <= k:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
            merge_pos += 1
            
        #Copy merge number back to nums
        for merge_pos in range(merged_size):
            
            numbers[i + merge_pos] = merged_numbers[merge_pos]
        return (comps, swaps)

    if not type(lyst) is list:
        raise TypeError
    size = len(lyst)
    result = sort(lyst, 0, size - 1, comps, swaps)
    return result

def selection_sort(lyst):
    def sort(numbers):
        comps = 0
        swaps = 0
        for i in range(len(numbers)-1):
            #find index of smallest remaining element
            index_smallest = i
            for j in range(i+1, len(numbers)):
                comps += 1
                if numbers[j] < numbers[index_smallest]:
                    index_smallest = j
            
            #Swap numbers[i] and numbers[index_smallest]
            swaps += 1
            temp = numbers[i]
            numbers[i] = numbers[index_smallest]
            numbers[index_smallest] = temp

        return (numbers, comps, swaps)
    
    if not type(lyst) is list:
        raise TypeError
    result = sort(lyst)
    return result

def insertion_sort(lyst):
    def sort(numbers):
        comps = 0
        swaps = 0
        tswaps = 0
        for i in range(1, len(numbers)):
            j = i
            # Insert numbers[i] into sorted part 
            # stopping once numbers[i] in correct position
            
            while j > 0 and numbers[j] < numbers[j - 1]:
                # Swap numbers[j] and numbers[j - 1]
                temp = numbers[j]
                numbers[j] = numbers[j - 1]
                numbers[j - 1] = temp
                j -= 1
                swaps += 1
                comps += 1
                
            if tswaps != swaps:
                tswaps = swaps
            else:
                comps += 1
        return (numbers, comps, swaps)
    if not type(lyst) is list:
        raise TypeError
    result = sort(lyst)
    return result
    
def main():
    print("starting quicksort")
    results = quicksort(test) 
    print(f"Is Sorted? = {is_sorted(test)}")
    # print(f"Original Data: {DATA}")
    print(f"QuickSorted Data: {results}")
    print("\n")
    reset()
    
    print("starting selection_sort")
    results = selection_sort(test)
    print(f"Is Sorted? = {is_sorted(test)}")
    # print(f"Original Data: {DATA}")
    print(f"SelectionSort Data: {results}")
    print("\n")
    reset()
    
    print("starting insertion_sort")
    results = insertion_sort(test)
    print(f"Is Sorted? = {is_sorted(test)}")
    # print(f"Original Data: {DATA}")
    print(f"insertion sorted Data: {results}")
    print("\n")
    reset()
    
    print("starting mergesort")
    results = mergesort(test)
    print(f"Is Sorted? = {is_sorted(test)}")
    # print(f"Original Data: {DATA}")
    print(f"Merge Sort Data: {results}")
    print("\n")
    reset()    
    
if __name__ == "__main__":
    main()