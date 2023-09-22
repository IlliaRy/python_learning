n = 5
i=0
k = []
sum = 0



while n>= 0:
    while i <= n:
        print(i, "current index")
        k.append(n%2)
        i =i+1
    Sum_1 = sum(k)
    print(Sum_1)
    k = []
    i=0
n = n-1
    


