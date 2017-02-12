#!/bin/python3

import sys
import math

def encrypt(in_string):
	in_string = in_string.replace(' ','')
	in_len = len(in_string)
	# print(in_len)
	sq_matrix_size = math.ceil(math.sqrt(in_len))
	char_list = []
	for x in in_string:
		char_list.append(x)

	for i in range(0,sq_matrix_size):
		for j in range(0,sq_matrix_size):
			

# s = input().strip()
s = "if man was meant to stay on the ground god would have given us roots"

encrypt(s)