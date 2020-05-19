#!/usr/bin/env python3

import sys
import os.path
from os import path
from sys import argv

def testIfCompatible(dim) :
	columns = dim[0].split(" ")[1]
	rows = dim[1].split(" ")[0]
	if (columns != rows) :
		exit("Matrices are not compatible")
 
def getArguments(i) :

	if (path.exists(str(argv[i]))) :
		emptyList.append(argv[i])
	else :
		exit("Doesn't exist - argument => " + str(i))
	
def getMatrix (whichMatrix) :

	row = matrix[whichMatrix].split("\n") # split by rows
	dimension[whichMatrix] = row[0] # top row is dimension of a matrix
	if (len(dimension[whichMatrix].split(" ")) != 2) :
		exit("Invalid matrix") # if matrix's dimensions are not valid (only row and column number)
	
	elements = row[1:] # matrix elements are from the second row to the end 
	dictionary = {} # matrix will be saved as dictionary
	
	if (whichMatrix == 1) :
		testIfCompatible(dimension) # test if two matrices could be multiplied

	for el in elements :
		try :
			el01 = el.split(" ")
			r = int(el01[0]) # row 
			c = int(el01[1]) # column
			dictionary[(r,c)] = float(el01[2]) # value of an element at given position
		except ValueError:
			pass
	return dictionary

def exportResult(matrix, output, dim) :
	file = open(output, "w")
	rowNum = dim[1].split(" ")[0]
	colNum = dim[0].split(" ")[1]
	file.write(str(rowNum) + " " + str(colNum) + "\n")
	for key in matrix.keys() :
		if (key != rowNum and key != colNum):
			file.write(str(key[0]) + " " + str(key[1]) + " " + str(matrix[key]) + "\n")
	file.close()
		

def multiplyMatrix(matA, matB, dim, output) :
	multiplyMatrix = {}
	for i in range (1, int(dim[0].split(" ")[0])+1):  # range from 1 to no of matrix A rows
		for j in range(1, int(dim[1].split(" ")[1])+1): # range from 1 to no of matrix B columns
			multiplyMatrix[(i,j)] = 0
			for k in range(1, int(dim[0].split(" ")[1])+1): # to matrix A columns
				multiplyMatrix[(i,j)] += float(matA.get((i,k), 0) * matB.get((k,j),0)) # if key
										# doesn't exists add 0
			if multiplyMatrix[(i,j)] == 0:
				del multiplyMatrix[(i,j)] # delete empty spaces
	exportResult(multiplyMatrix, output, dim)
	return multiplyMatrix
	
	 
# main
emptyList = []

if (len(argv) != 3) :
	exit("Illegal argument number") # command line arguments python3 fileName.py inputFile.txt outputFile.txt

getArguments(1)
getArguments(2)

inputFile = emptyList[0]
outputFile = emptyList[1]

file = open(inputFile, "r").read()
matrix = file.split("\n\n") # first empty line is the end of a first matrix, and scnd matrix starts after 
			    # the second empty line
dimension = [0,0] # dimensions of input matrices

matrix01 = getMatrix(0)
matrix02 = getMatrix(1)

print (multiplyMatrix(matrix01, matrix02, dimension, outputFile)) # result of multiplied matrices






