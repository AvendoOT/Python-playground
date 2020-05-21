#!/usr/bin/env python3

import sys
from os import path


def generate(file):
    print("--------------------------------")
    print("IP adrese     |     Br. pristupa")
    print("--------------------------------")

    ips = {}
    i = 0
    for row in file:
        thisRow = row.split(" ")
        ipAddress = thisRow[0]
        ipAddress = ipAddress.split(".")
        num1 = ipAddress[0]
        num2 = ipAddress[1]
        string = num1 + "." + num2 + ".*.*"
        i += 1
        a = {i: string}
        ips.update(a)
    values = ips.values()
    keyList = ips.values()
    visited = []
    for value in values:
        if (value in visited):
            continue
        visited.append(value)
        count = 0
        for key in keyList:
            if (value == key):
                count += 1
	# OVDJE ISPISUJEM BEZ SORTIRANJA ZBOG ISTEKA VREMENA ! ŽAO MI JE 
        print (value + "          " + str(count))


def main():

    if (len(sys.argv) != 2):  # command line arguments python3 fileName.py textfile.txt
        exit("Illegal argument number")

    emptyList = []

    if (path.exists(str(sys.argv[1]))):
        emptyList.append(sys.argv[1])
    else:
        exit("File doesn't exist")

    file = open(sys.argv[1], "r")
    generate(file.readlines())
    file.close()


if __name__ == "__main__":
    main()
