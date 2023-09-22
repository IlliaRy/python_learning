nums = [3,2,4]
print("vector:", nums)

target = 6

l_num = len(nums) #vector length
in_fi = 0 #index of first elem
in_la = l_num-1 #index of last elem


hasht = []
for i in range (in_fi, in_la+1): #fill the hash table
    diff = target-nums[i]
    hasht.insert(i, diff) 
print("hasht", hasht)
print("l_num", l_num)
print("in_fi", in_fi)
print("in_la", in_la)

i=1
count = True
while i <= in_la and count :
    for j in range(in_fi, in_la+1):
        if i == j:
            continue
        else:
            if hasht[j] == nums[i]:
                print("indices:", i, j)
                count = False
    i +=1
            
    