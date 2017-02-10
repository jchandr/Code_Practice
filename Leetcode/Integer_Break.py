n = int(input())

current_max_product = 1
present_product = 1

while(n>2):
	a = 0
	b = 0
	if(n % 2 == 0):
		a = (n/2) + 1
		b = (n/2) - 1
		present_product = a * b
	else:
		


print (current_max_product)