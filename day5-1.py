file = 'day5.txt'

def parse_file(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
        range_lines = [tuple(map(int, num)) for num in [line.split('-') for line in lines if '-' in line]]
        id_lines = [int(line) for line in lines[len(range_lines) + 1:]]
        return range_lines, id_lines

def count_fresh_ids(ranges: list[tuple[int,int]], ids: list[int]):
    fresh_count = 0
    for id in ids:
        for (start, end) in ranges:
            if id >= start and id <= end:
                fresh_count += 1
                break
    return fresh_count

range_lines, id_lines = parse_file(file)
print(range_lines)
print(id_lines)
fresh_count = count_fresh_ids(range_lines, id_lines)
print(fresh_count)