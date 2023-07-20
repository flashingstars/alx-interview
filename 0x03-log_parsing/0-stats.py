#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""


import sys

# Dictionary to store the count of all status codes
status_count = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}

total_file_size = 0
line_count = 0  # Keep count of the number of lines processed

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # Check if the status code exists in the dictionary and increment its count
            if status_code in status_count.keys():
                status_count[status_code] += 1

            # Update total file size
            total_file_size += file_size

            # Update line count
            line_count += 1

        if line_count == 10:
            line_count = 0  # Reset line count
            print('File size: {}'.format(total_file_size))

            # Print out status code counts
            for key, value in sorted(status_count.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(status_count.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
