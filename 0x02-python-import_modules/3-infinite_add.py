#!/usr/bin/python3
if __name__ == "__main__":
    import sys
def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        i = 1
        total_sum = 0
        while i <= n:
            total_sum += int(argv[i])
            i += 1
        print("{:d}".format(total_sum))

