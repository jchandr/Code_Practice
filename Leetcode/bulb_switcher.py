def bulbSwitch(n):
	a = []
	for i in range(1,n):
		if (i%2 == 0):
			a.append(0)
		else:
			a.append(1)
		print(a)

bulbSwitch(4)