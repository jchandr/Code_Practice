from collections import deque

co_ordinates_queue = deque([])
node_trace_set = []

def return_adjacent_nodes(n):
	i = 0;
	adjacent_nodes = []
	r = n.row
	c = n.col
	a = 0
	try:
		a = maze[r-1]
		a = maze[r+1]
		a = maze[c + 1]
		a = maze[c - 1]
	except IndexError:
		r - 1 = 1
		r + 1 = 1
		c + 1 = 1
		c - 1 = 1


	if((r in range(0,total_row+1)) and (r in range(0,total_col+1)) and maze[r-1][c-1]==0):
		temp = Node()
		temp.parent.append([r,c])
		temp.row = r-1
		temp.col = c-1
		adjacent_nodes.append(temp)
		i = i + 1


	if((r in range(0,total_row+1)) and (r in range(0,total_col+1)) and maze[r+1][c+1]==0):
		temp = Node()
		temp.parent.append([r,c])
		temp.row = r+1
		temp.col = c+1
		adjacent_nodes.append(temp)
		i = i + 1

	if((r in range(0,total_row+1)) and (r in range(0,total_col+1)) and maze[r-1][c+1]==0):
		temp = Node()
		temp.parent.append([r,c])
		temp.row = r-1
		temp.col = c+1
		adjacent_nodes.append(temp)
		i = i + 1

	if((r in range(0,total_row+1)) and (r in range(0,total_col+1)) and maze[r+1][c-1]==0):
		temp = Node()
		temp.parent.append([r,c])
		temp.row = r+1
		temp.col = c-1
		adjacent_nodes.append(temp)
		i = i + 1

	if((r in range(0,total_row+1)) and (r in range(0,total_col+1)) and maze[r-1][c]==0):
		temp = Node()
		temp.parent.append([r,c])
		temp.row = r-1
		temp.col = c
		adjacent_nodes.append(temp)
		i = i + 1

	if((r in range(0,total_row+1)) and (r in range(0,total_col+1)) and maze[r+1][c]==0):
		temp = Node()
		temp.parent.append([r,c])
		temp.row = r+1
		temp.col = c
		adjacent_nodes.append(temp)
		i = i + 1

	if((r in range(0,total_row+1)) and (r in range(0,total_col+1)) and maze[r][c-1]==0):
		temp = Node()
		temp.parent.append([r,c])
		temp.row = r
		temp.col = c-1
		adjacent_nodes.append(temp)
		i = i + 1

	if((r in range(0,total_row+1)) and (r in range(0,total_col+1)) and maze[r][c+1]==0):
		temp = Node()
		temp.parent.append([r,c])
		temp.row = r
		temp.col = c+1
		adjacent_nodes.append(temp)
		i = i + 1

	# print(i)
	return adjacent_nodes



class Node:
	parent = []
	row = 0
	col = 0

def enqueue(co_ordinates):
	co_ordinates_queue.append(co_ordinates)


def solve_maze(maze):
	root = Node()
	root.parent = [0,0]
	root.row = 0
	root.col = 0
	co_ordinates_queue.append(root)

	while co_ordinates_queue:
		current = co_ordinates_queue.popleft()
		if(maze[current.row][current.col] == 2):
			return current

		adjacent_nodes1 = return_adjacent_nodes(current)
		
		for a_node in adjacent_nodes1:
			if not(a_node in node_trace_set):
				node_trace_set.append(a_node)
				a_node.parent.append(current)
				co_ordinates_queue.append(a_node)			



maze = [[1,0,0,0],[0,5,0,0],[0,5,0,2],[0,0,0,0]]
total_row = len(maze)
total_col = len(maze[0])
dummy_x = 1
dummy_y = 1
solve_maze(maze)
print(node_trace_set)