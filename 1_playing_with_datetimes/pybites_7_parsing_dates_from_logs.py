from datetime import datetime
from pathlib import Path
import urllib.request
import re

"""
Day 2: Parsing dates from logs
Github source: https://github.com/mikeckennedy/100daysofcode-with-python-course/tree/master/days/01-03-datetimes
PyBites URL: https://codechalleng.es/bites/7/

Instructions: Parse log entries for datetimes and calculate the time between two shutdown initializations.
"""

# prep
tempfile = Path('/tmp/log.txt')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', tempfile)


# program
def main():
    # Read in list of lines from log file
    list_of_lines = read_file(tempfile)

    # Check for shutdown init command, then convert line to timestamp
    timestamps = list(filter(None, [convert_to_datetime(log) for log in list_of_lines]))

    # Find interval between max and min
    diff = time_between_shutdowns(timestamps)

    return diff


# code
def read_file(filename: Path):
    """Read in tempfile return list of lines"""
    with open(filename, 'r', encoding='utf8') as inf:
        lines = inf.readlines()

        return lines


def convert_to_datetime(line):
    """Given a line extract timestamp and convert to datetime"""
    datetime_regex = re.compile(
        r'[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T(2[0-3]|[01][0-9])(:[0-5][0-9]){2}')

    if line.endswith('Shutdown initiated.\n'):
        match = re.search(datetime_regex, line).group()
        date_and_time = datetime.strptime(match, '%Y-%m-%dT%H:%M:%S')

        return date_and_time


def time_between_shutdowns(lines):
    min_date = min(lines)
    max_date = max(lines)

    difference = max_date - min_date

    print(f"The interval between shutdown initiations is {difference}")
    return difference


if __name__ == '__main__':
    main()
