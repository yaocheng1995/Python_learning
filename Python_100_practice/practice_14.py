p = 1 
while p > 0 :
    n = int(input('Input a number:'))
    if  n <= 0 :
        print ("请输入一个正确的数字！")
    else :
        p = 0

print (n, "=", end=" ")
q = 1
while q > 0 :
    for i in range (2,n+1) :
        if n%i == 0 :
            n = int(n/i)
            if n == 1 :
                print (i)
                q = 0
            else : 
                print (i, "*", end=" ")
            break
