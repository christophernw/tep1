import os
import random

def generate_num(n, mn=1, mx=10**9):
    return [random.randint(mn, mx) for _ in range(n)]

dataset_detail = [
    ('kecil', 2**9),
    ('sedang', 2**13),
    ('besar', 2**16),
]

if __name__ == '__main__':
    dataset_dir = 'dataset'
    if not os.path.exists(dataset_dir):
        os.mkdir(dataset_dir)
    
    for file_name, num_count in dataset_detail:
        generated_nums = generate_num(num_count)
        with open(os.path.join(dataset_dir, f'{file_name}.txt'), 'w+') as f:
            f.write('\n'.join([str(num) for num in generated_nums]))
        
        with open(os.path.join(dataset_dir, f'{file_name}_sorted.txt'), 'w+') as f:
            f.write('\n'.join([str(num) for num in sorted(generated_nums)]))

        with open(os.path.join(dataset_dir, f'{file_name}_reversed.txt'), 'w+') as f:
            f.write('\n'.join([str(num) for num in sorted(generated_nums, reverse=True)]))