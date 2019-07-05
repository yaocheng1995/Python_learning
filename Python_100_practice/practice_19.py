num = []
for i in range (2, 1001) :
    n = 0
    for j in range (1, i) :
        if i%j == 0 :
            n += j
    if n == i :
        num.append(i)
print (num)
