#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except (FileNotFoundError, OSError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                    # Expected output: 15
    print(add('10', 5))                  # Expected output: 15
    print(add('abc', 5))                 # Expected output: error: could not add numbers
    print(read_file('seneca2.txt'))      # Expected output: File contents or error
    print(read_file('file10000.txt'))    # Expected output: error: could not read file

