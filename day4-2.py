import numpy as np

file = 'day4.txt'
directions = ((-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1))

def parse_flie(file):
    with open(file) as f:
        lines = f.readlines()
        grid =  [[1 if char == '@' else 0 for char in line.strip()] for line in lines]
        array = np.array(grid)
    return array

def is_inbounds(coords: tuple[int,int]) -> bool:
    return 0 <= coords[0] < array.shape[0] and 0 <= coords[1] < array.shape[1]

def is_reachable(coords: tuple[int,int]) -> bool:
    global array
    blockers = 0
    for direction in directions:
        neighbor = coords[0] + direction[0], coords[1] + direction[1]
        if not is_inbounds(neighbor):
            continue
        if array[neighbor] in (1, 4):
            blockers += 1
            if blockers >= 4:
                return False
    return True

def remove_reachables(array: np.ndarray) -> np.ndarray:
    for column in range(shape[0]):
        for row in range(shape[1]):
            if array[row, column] == 0:
                continue
            elif is_reachable((row, column)):
                array[row, column] = 4
    return array

def all_removed(array: np.ndarray) -> bool:
    return np.where(array == 4)[0].shape[0] == 0

array = parse_flie(file)
shape = array.shape
count = 0
while True:
    array = remove_reachables(array)
    if not all_removed(array):
        count += np.where(array == 4)[0].shape[0]
        print(f'count: {count}')
        array = np.where(array == 4, 0, array)

    else:
        print(f'done. count: {count}')
        break