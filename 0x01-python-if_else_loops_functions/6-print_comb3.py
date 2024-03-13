#!/usr/bin/python3
for i in range(0, 9):
    for m in range(i + 1, 10):
        if i == 8:
            print("{}{}".format(i, m))
        else:
            print("{}{}".format(i, m), end=", ")
