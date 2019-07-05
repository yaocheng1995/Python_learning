year = int(input('year:\n'))
mouth = int(input('mouth:\n'))
day = int(input('day:\n'))

mouths = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < mouth <= 12 :
	sum = mouths[mouth - 1]
else :
	print('data error')
sum += day

leap = 0
if (year%400 == 0) or ((year%4 == 0) and (year%100 != 0)) :
	leap = 1
if (leap == 1) and (mouth > 2) :
	sum += 1
	
''' 调用calendar模块
leap = calendar.isleap(year)
if (leap == 'Ture') :
	sum += 1
'''
print ('it is the %dth day .'%sum)

