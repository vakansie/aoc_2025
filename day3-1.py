file = 'day3.txt'

def parse_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def find_max_joltage(bank:str) -> int:
    nums = set(bank)
    highest = sorted(nums, reverse=True)
    prime_jolt_spot = bank.index(highest[0])
    if prime_jolt_spot == len(bank) - 1:
        max_joltage = highest[1] + highest[0]
        return int(max_joltage)
    else:
        remaining_spots = bank[prime_jolt_spot + 1:]
        next_highest = sorted(set(remaining_spots), reverse=True)[0]
        max_joltage = highest[0] + next_highest
        return int(max_joltage)

banks = parse_file(file)
total_joltage = 0
for bank in banks:
    max_joltage = find_max_joltage(bank)
    print(f'bank: {bank} -> max joltage: {max_joltage}')
    total_joltage += max_joltage
print(f'total joltage: {total_joltage}')