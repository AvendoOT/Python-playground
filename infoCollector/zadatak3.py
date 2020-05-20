#!/usr/bin/env python3
import os
import re
import sys


def printStudents(labExams, students, student):

    length = len(labExams)

    print("JMBAG       SURNAME, NAME       ", end='')

    for i in range(length):
        print("     L" + str(i+1), end='')
    print()
    for i in students:
        print(i + "  " + "%-20s" % (student[i]["surname"] + ", " + student[i]["name"]), end='')
        for j in range(1, length+1):
            print("    " + "%-3.1f" % (student.get(i, 0).get(j, 0)), end='')
        print()


def main():
    student = {}

    if (len(sys.argv) != 2):
        # command line arguments python3 fileName.py directory
        exit("Illegal argument number")

    emptyList = []

    if (os.path.isdir(str(sys.argv[1]))):
        emptyList.append(sys.argv[1])
    else:
        exit("Directory is not given")
    directory = emptyList[0]
    path = str(directory)+"/studenti.txt"
    file = open(path, "r")

    students = []

    for row in file:
        jmbag, surname, name = row.rstrip().split(" ")
        student[jmbag] = {"surname": surname, "name": name}
        students.append(jmbag)
    file.close()

    labExams = []
    listDirs = os.listdir(str(directory))

    for lab in listDirs:
        if re.match("(Lab_[0-9]+_g[0-9]+.txt)", lab): # regex for laboratory
            file = open(lab, "r")
            exam = int(lab.split("_")[1])
            if exam not in labExams:
                labExams.append(exam)
            for row in file:
                if not student.get(row.split(" ")[0], 0).get(exam, 0):
                    student[row.split(" ")[0]][exam] = float(row.split(" ")[1])
                else:
                    string = student[row.split(" ")[0]]["name"] + student[row.split(
                        " ")[0]]["surname"] + "has already joined - TERMINATING"
                    exit(string) # program ends if student is already joined, invalid files
                    #print(string)
    file.close()

    printStudents(labExams, students, student)


if __name__ == '__main__':
    main()
