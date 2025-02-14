#!/usr/bin/env python3
# Author ID: [bturja-nandini-dia]

# Existing functions from lab5a.py
def read_file_string(file_name):
    # Reads the entire contents of the file as a single string
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    # Reads the entire contents of the file as a list of lines
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

# New functions for writing to files
def append_file_string(file_name, string_of_lines):
    # Appends string_of_lines to the end of the file
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    # Writes each item in list_of_lines as a separate line in the file
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Copies content from file_name_read to file_name_write, adding line numbers
    with open(file_name_read, 'r') as fr, open(file_name_write, 'w') as fw:
        for i, line in enumerate(fr, start=1):
            fw.write(f"{i}:{line.strip()}\n")

# Main script execution block
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    # Testing append_file_string
    append_file_string(file1, string1)
    print(read_file_string(file1))

    # Testing write_file_list
    write_file_list(file2, list1)
    print(read_file_string(file2))

    # Testing copy_file_add_line_numbers
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

