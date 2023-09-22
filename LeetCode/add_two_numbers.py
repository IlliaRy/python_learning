

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
out= []
k=0
i=0
max_l=max(len(l1),len(l2))

while len(l1)<len(l2):
    l1.insert(0,0)
while len(l2)<len(l1):
    l2.insert(0,0)

while i < max_l :
    sum = l1[i]+l2[i]
    if sum+k < 10:
       out.append(sum+k)
       print(out, "less then 10")
       k=0 
    else:
       out.append((sum)%10)
       print(out, "more then 10 added nex number")
       k=sum//10
       if i == max_l-1:
            out.append(k)
    i=i+1
    print(out)
