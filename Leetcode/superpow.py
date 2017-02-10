def superPow(a, b):
	b_size = len(b)
	b = map(str,b)
	b_in_int = int(''.join(b))
	return(pow(a,b_in_int))