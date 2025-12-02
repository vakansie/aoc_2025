file = 'day2.txt'

def parse_input(file):
    ranges = []
    with open(file, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            ranges.extend([tuple(map(int, part.split('-'))) for part in parts if part])
    return ranges

def find_factors(length:int) -> list[int]:
    factors = []
    for i in range(1, length + 1):
        if length % i == 0:
            factors.append(i)
    factors.pop(0)
    return factors

def is_repeating(digits:int) -> bool:
    string = str(digits)
    length = len(string)
    slices = []
    for factor in find_factors(length):
        slice_length = length // factor
        slice = [string[i:i + slice_length] for i in range(0, length, slice_length)]
        slices.append(slice)
    # print(slices)
    for slice in slices:
        if len(list(set(slice))) == 1:
                print(f'true on: {slice}, digits: {digits}')
                return True
    return False

sum_of = 0
ranges = parse_input(file)
print(ranges)
for rang in ranges:
    start, end = rang
    for digits in range(start, end + 1):
        if is_repeating(digits):
            print(digits)
            print('+1')
            sum_of += digits

# print(is_repeating(123123123))
print(f'sum = {sum_of}')