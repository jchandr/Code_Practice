import numpy
import sys

# R = 10
# C = 10

# G=	[[7,2,8,3,4,5,5,8,6,4],
# 	[6,7,3,1,1,5,8,6,1,9],
# 	[8,9,8,8,2,4,2,6,4,3],
# 	[3,8,3,0,5,8,9,3,2,4],
# 	[2,2,2,9,5,0,5,8,1,3],
# 	[5,6,3,3,8,4,5,3,7,4],
# 	[6,4,7,3,5,3,0,2,9,3],
# 	[7,0,5,3,1,0,6,6,0,1],
# 	[0,8,3,4,2,8,2,9,5,6],
# 	[4,6,0,7,9,2,4,1,3,7]]

# r = 3 
# c = 4
# P= 	[[9,5,0,5],
# 	[3,8,4,5],
# 	[3,5,3,0]]

def find_subgrid():
	total_found_subgrids = []
	total_size = 0
	for c_i in range(0,C - c + 1):
		for r_i in range(0,R):
			total_found_subgrids.append(G[r_i][c_i:c_i+c])
			

	# print(total_found_subgrids)
	i = 1
	total_size = (C - c)*(R-1)
	current_found_subgrid = []
	print(total_size)


t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)
    print(find_subgrid())
