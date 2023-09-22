nums = [3,3]
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

for i in range (in_fi+1, in_la):
    for j in range (in_fi, in_la+1):
        print(i,j)
        if nums[i] == hasht[j]:
            print("indices:", i,j)
            break
    
        
        



