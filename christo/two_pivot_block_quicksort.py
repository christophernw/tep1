import sys
import os
import time
import tracemalloc
from memory_profiler import memory_usage

BLOCK_SIZE = 64

def partition(arr, l, r):
    n = r - l + 1
    
    # base case
    if n <= 1:
        return (l, r)
    
    if arr[l] > arr[r]: # exchange pivot
        arr[l], arr[r] = arr[r], arr[l]

    p, q = arr[l], arr[r] # assign pivot

    block = [0 for _ in range(BLOCK_SIZE)] # bikin block
    i, j, k = 1+l, 1+l, 1+l # 3 indeks penanda region
    num_p, num_q = 0, 0 # ukuran pada block yang ada nilai valid nya

    while k < r:
        t = min(BLOCK_SIZE, r - k)
        for c in range(t): # cari yang <= q , masukan ke block
            block[num_q] = c
            num_q = num_q + (q >= arr[k + c])

        for c in range(num_q): # tukar nilai nilai yang missplaced sebelumnya
            arr[j + c], arr[k + block[c]] = arr[k + block[c]], arr[j + c]

        k = k + t # naikan iterator k

        for c in range(num_q): # cari yang < q, masukan ke block
            block[num_p] = c
            num_p = num_p + (p > arr[j + c])

        for c in range(num_p): # tukar nilai-nilai yang missplaced sebelumnya
            arr[i], arr[j + block[c]] = arr[j + block[c]], arr[i]
            i += 1 # naikan iterator i
        
        j = j + num_q # naikan iterator j
        num_p, num_q = 0, 0 # reset

    # letakan pivot di posisi yang benar
    arr[i-1], arr[l] = arr[l], arr[i-1] 
    arr[j], arr[r] = arr[r], arr[j]

    return (i-1, j)

def two_pivot_block_lomuto(arr, l=None, r=None):
    if l is None:
        l, r = 0, len(arr)-1
    
    rec_stack = [(l, r)]

    # stack di sini digunakan untuk menghindari adanya recursion exceeded
    while len(rec_stack):
        l, r = rec_stack.pop()
        i, j = partition(arr, l, r)

        if l < i-1:
            rec_stack.append((l, i-1))
        if i+1 < j-1:
            rec_stack.append((i+1, j-1))
        if j+1 < r:
            rec_stack.append((j+1, r))
    
    return arr

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
        profile_sort(two_pivot_block_lomuto, test)
        print("=" * 30)
        
