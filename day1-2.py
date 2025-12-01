
file = 'day1-1.txt'

position = 50
zero_count = 0


def parse_input(file):
    with open(file, 'r') as file:
        for line in file:
            sign = 1 if line[0] == 'R' else -1
            clicks = int(line[1:])
            print(line.strip('\n'))
            rotate_dial(sign, clicks)
            print(position)
        print(f'Zero position count: {zero_count}')

def rotate_dial(sign:int, clicks:int):
    global position
    global zero_count
    amount = sign * clicks
    for I in range(abs(amount)):
        position =  (position + sign) % 100
        if position == 0:
            zero_count += 1
            print('+1')

parse_input(file)
