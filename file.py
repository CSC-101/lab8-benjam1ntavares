import sys

file = sys.argv[1]

try:
    with open(file, 'r') as open_file:
        for line in file:
            pass

except FileNotFoundError as fnfe:
    print(f'error: file "{file}" not found')
