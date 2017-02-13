class Shopping_Center:
	def __init__(self,c_n,n_f_t,f_t_l):
		center_number = c_n
		no_fish_types = n_f_t
		fish_type_list = f_t_l


s1 = input().strip().split(' ')
centers = []
total_types_of_fish = int(s1[2])
for x in range(1,int(s1[0])+1):
	center_info = input().strip().split(' ')
	no_fish_types =  int(center_info[0])
	center_info = center_info[1:]
	fish_type_list = []
	for x in center_info:
		fish_type_list.append(int(x))

	center = Shopping_Center(x,no_fish_types,fish_type_list)
	centers.append(center)

connection_matrix = [[0 for y in range(int(s1[0])+1)] for x in range(int(s1[0])+1)]
collected_fish_types = []

for x in range(0,int(s1[1])):
	s3 = input().strip().split()
	connection_matrix[int(s3[0])][int(s3[1])] = int(s3[2])
	connection_matrix[int(s3[1])][int(s3[0])] = int(s3[2])

def find_min_time(centers):

	

print(find_min_time())