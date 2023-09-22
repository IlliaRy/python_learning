
s = 'bbbb'

s_dic = {}
length = 0
l=0


for i, letter in enumerate(s):
    print(i, letter,' - current I, Letter')
    while s[i] in s_dic:
        print(s_dic,' - before delete')
        print(s[l], l,' - letter and number to delete')
        s_dic.pop(s[l]) #keep clearing dict while letter from S is inside
        print(s_dic,' - after delete')
        l = l+1 #move pointer along S
        print(l,' - number to delete')
    s_dic[letter] = l #after all is cleared add letter do dict
    length = max(length,len(s_dic)) #if no duplicates l is NOT increasing and I - is. So the max diff should be the length
print(length)

