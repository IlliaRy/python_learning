l1 = [9,9,9,9,9,9,9,9]
l2 = [9,9,9,9]
out= []
k=0
i=0
j=0

while len(l1)<len(l2):
    l1.insert(0,0)
while len(l2)<len(l1):
    l2.insert(0,0)
print(l1,l2)