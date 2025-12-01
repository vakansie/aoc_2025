
file = 'day1-1.txt'

position = 50

def parse_input(file):
    zero_count = 0
    with open(file, 'r') as file:
        for line in file:
            sign = 1 if line[0] == 'R' else -1
            clicks = int(line[1:])
            print(line.strip('\n'))
            rotate_dial(sign * clicks)
            if position == 0:
                zero_count += 1

            print(position)
        print(f'Zero position count: {zero_count}')

def rotate_dial(amount:int):
    global position
    new_position = position + amount
    print(f'New position before wrap: {new_position}')
    position = (new_position % 100)

parse_input(file)
