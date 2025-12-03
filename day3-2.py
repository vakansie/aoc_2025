file = 'day3.txt'

def parse_file(file) -> list[str]:
    with open(file, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def find_max_joltage(bank:str) -> int:
    while len(bank) > 12:
        bank = turn_1_off(bank)
    return int(bank)    
    
def turn_1_off(bank:str) -> str:
    occuring = set(bank)
    lowest = sorted(occuring)[0]
    for index, battery in enumerate(bank):
        if battery == lowest:
            bank = bank[:index] + bank[index + 1:]
            return bank
        elif battery < bank[index + 1]:
            bank = bank[:index] + bank[index + 1:]
            return bank


banks = parse_file(file)
# print(sum(list(map(find_max_joltage, banks))))

total_joltage = 0
for bank in banks:
    max_joltage = find_max_joltage(bank)
    print(f'bank: {bank} -> max joltage: {max_joltage}')
    total_joltage += max_joltage

print(f'total joltage: {total_joltage}')