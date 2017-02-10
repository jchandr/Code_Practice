def isSelfCrossing(x):
	if(len(x)<4):
		return False
	max = 0

	for i in x:
		if(i > max):
			max = i
	graph_dimension = (max * 2) + 2
	graph = [[0 for x in range(graph_dimension)] for y in range(graph_dimension)]
	graph[int(graph_dimension/2)][int(graph_dimension/2)] = 0
	input_length = 0
	input_length = len(x)
	current_x = int(graph_dimension/2)
	current_y = int(graph_dimension/2)
	# printgraf(graph,graph_dimension)
	for i in range(0,input_length):
		if(i%4 == 0):
			for j in range(0,x[i]):
				if(graph[current_x][current_y] == 1 or graph[current_x][current_y+1] == 1):
					return True
				graph[current_x][current_y] = 1
				current_y = current_y + 1
			# printgraf(graph,graph_dimension)
		if(i%4 == 1):
			for j in range(0,x[i]):
				if(graph[current_x][current_y] == 1 or graph[current_x-1][current_y] == 1):
					return True
				graph[current_x][current_y] = 1
				current_x = current_x - 1
			# printgraf(graph,graph_dimension)
		if(i%4 == 2):
			for j in range(0,x[i]):
				if(graph[current_x][current_y] == 1 or graph[current_x][current_y-1] == 1):
					return True
				graph[current_x][current_y] = 1
				current_y = current_y - 1
			# printgraf(graph,graph_dimension)
		if(i%4 == 3):
			for j in range(0,x[i]):
				if(graph[current_x][current_y] == 1 or graph[current_x+1][current_y] == 1):
					return True
				graph[current_x][current_y] = 1
				current_x = current_x + 1
			# printgraf(graph,graph_dimension)
	return False

	

def printgraf(graph,graph_dimension):
	for h in range(0,graph_dimension):
		for k in range(0,graph_dimension):
			print(graph[h][k],end = " ")
		print("\n",end="")

	print()


in_x = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,13,1]
print(isSelfCrossing(in_x))
in_x = [2,1,1,2]
print(isSelfCrossing(in_x))