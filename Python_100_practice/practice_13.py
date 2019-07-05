n = 0

for i in range(100,1000) :
	a = int(i / 100)
	b = int(i / 10) % 10
	c = i % 10
	m = a ** 3 + b ** 3 + c ** 3
	if i == m :
		print (i)
		n += 1

print ('the total is :', n)
