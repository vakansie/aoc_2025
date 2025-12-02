file = 'day2.txt'

def parse_input(file):
    ranges = []
    with open(file, 'r') as file:
        for line in file:
            # print(line.strip())
            parts = line.strip().split(',')
            ranges.extend([tuple(map(int, part.split('-'))) for part in parts if part])
    return ranges

def is_repeating(digits:int):
    string = str(digits)
    length = len(string)
    if length % 2:
        return False

    index = int(length / 2)
    first, last = string[:index], string[index:]
    # print(first, last)
    if first == last:
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

print(f'sum = {sum_of}')

# print(is_repeating(123123))