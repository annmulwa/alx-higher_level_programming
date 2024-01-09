#!/usr/bin/python3
"""
Reads stdin and computes metrics
"""


def print_stats(size, status_codes):
    """
    Reads stdin line by line and computes
    metrics
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    cnt = 0

    try:
        for line in sys.stdin:
            if cnt == 10:
                print_stats(size, status_codes)
                cnt = 1
            else:
                cnt += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in possible_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
