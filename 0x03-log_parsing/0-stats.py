#!/usr/bin/python3
import sys
import re
import signal

pattern = re.compile(
    r'^\d{1,3}(\.\d{1,3}){3} - \[\d{2}/\w{3}/\d{4}(:\d{2}){3} \+\d{4}\] '
    r'"GET /projects/\d+ HTTP/1\.1" (200|301|400|401|403|404|405|500) \d+$'
)

total_file_size = 0
line_count = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

def print_statistics():
    """Function to print statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def signal_handler(sig, frame):
    """Handle CTRL + C and print statistics before exiting."""
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        if pattern.match(line.strip()):
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            total_file_size += file_size

            if status_code in status_code_count:
                status_code_count[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
