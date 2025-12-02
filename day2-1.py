file = 'day2ex.txt'

def parse_input(file):
    ranges = []
    with open(file, 'r') as file:
        for line in file:
            print(line.strip())
            parts = line.strip().split(',')
            # ranges.extend(line.strip('\n').split(','))
            ranges.extend([tuple(map(int, part.split('-'))) for part in parts if part])

    print(ranges)


parse_input(file)