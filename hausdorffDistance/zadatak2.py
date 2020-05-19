#!/usr/bin/env python3
import sys
from os import path

def generate(file) :
	print("Hyp#Q10#Q20#Q30#Q40#Q50#Q60#Q70#Q80#Q90")
	quant = 1
	for row in file : 
		num = []
		row = list(row.rstrip().split(" ")) # trim line
		length = len(row)
		for i in range(length) :
			row[i] = float(row[i]) 
		row.sort()
		for i in range(1, 10) :
			value = int(round(i/10*length))
			num.append(row[value])
		print(("\n%03d" % quant))
		for j in range (9) : # because of step 0.1
			print("#{0}".format(str(num[j])), end = "")
			
		quant += 1
		

def main() :

	if (len(sys.argv) != 2) :
		exit("Illegal argument number") # command line arguments python3 fileName.py inputFile.txt

	emptyList = []

	if (path.exists(str(sys.argv[1]))) :
		emptyList.append(sys.argv[1])
	else :
		exit("File doesn't exist")

	file = open(sys.argv[1], "r") 
	generate(file.readlines()) # file lines returned as list

if __name__ == "__main__" :
	main()
