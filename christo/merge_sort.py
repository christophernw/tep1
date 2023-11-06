import os
import sys
import time
import tracemalloc
from memory_profiler import memory_usage

# KODINGAN MERGE SORT PADA UMUMNYA
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    
    ptr1, ptr2 = 0, 0
    while ptr1 < len(left) and ptr2 < len(right):
        if left[ptr1] < right[ptr2]:
            result.append(left[ptr1])
            ptr1 += 1
        else:
            result.append(right[ptr2])
            ptr2 += 1
        
    while ptr1 < len(left):
        result.append(left[ptr1])
        ptr1 += 1

    while ptr2 < len(right):
        result.append(right[ptr2])
        ptr2  += 1
    
    return result


# fungsi untuk evaluasi memori & running time
def profile_sort(sort_func, A):
    memory_usages = memory_usage((time_profile_sort, (sort_func, A)), max_iterations=1)
    print(f'{max(memory_usages)} MB')

# fungsi cari running time
def time_profile_sort(sort_func, A):
    start_time = time.time()
    sort_func(A)
    end_time = time.time()
    print(f'{(end_time - start_time) * 1000} ms')

if __name__ == '__main__':
    sys.setrecursionlimit(2**17)
    dataset_dir = 'dataset'
    for file_name in os.listdir(dataset_dir):
        with open(os.path.join(dataset_dir, file_name), 'r') as f:
            test = [int(num) for num in f.read().split('\n')]
        
        print(f'Running time (ms) dan Memory Access (MB) untuk "{file_name}":')
        profile_sort(merge_sort, test)
        print("=" * 30)
    