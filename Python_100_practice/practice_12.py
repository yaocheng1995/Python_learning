from math import sqrt

n = 0
for i in range(101,200) :
	k = 0 
	m = int(sqrt(i))
	for j in range(2,m+1) :
		p = i % j
		if p == 0 :
			k = 1
	if k == 0 :
		print (i)
		n += 1
print (' ')
print ('the total are : %d' %n)

