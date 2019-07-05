a = int(input ("a = "))
n = int(input ("n = "))
s = 0
t = a
for i in range (1, n+1) :
    s += a
    a = 10*a + t
print (s)
