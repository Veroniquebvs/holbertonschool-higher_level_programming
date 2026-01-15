#!/usr/bin/python3
import sys
sum = 0
if __name__ == "__main__":
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        else:
            sum = sum + int(sys.argv[i])
    print("{}".format(sum))
