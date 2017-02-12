import sys

n = 3
s = ['A','B','AE']
s.sort()

values = []

for t in s:
	temp_val = 0
	for c in t:
		temp_val = temp_val + ord(c)
	values.append(temp_val)

print(values)