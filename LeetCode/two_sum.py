nums = [3,2,4]
target = 6
hash = []

for i in range(len(nums)):
    print(i,nums[i],"current index and number")
    for j in range(len(hash)):
        print(j,hash, "current hash index and hash")
        if hash[j] == nums[i]:
            print(i, j)
        else:
            print("hash number wi index [",j,"] isn't req number")
    else:
        hash.append(target-nums[i])
        print(hash, "After append")