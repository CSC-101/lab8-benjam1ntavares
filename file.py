import sys


file = sys.argv[1]

try:
    with open(file, 'r') as open_file:
        for line in open_file:
            split_line = line.strip().split(',')
            if len(split_line) != 2:
                print(f'error: invalid format: "{line.strip()}"')
                continue

            try:
                float_1 = float(split_line[0].strip())
                float_2 = float(split_line[1].strip())
                print(float_1 + float_2)
            except ValueError as ve:
                print(f'error: invalid line "{line.strip()}": {ve}')
                continue

except FileNotFoundError as fnf:
    print(f'error: file "{file}" not found')

