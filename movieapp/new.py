v="aeiouAEIOU"
s="strings"
c=0
k=0
for i in s:
    if i in v:
        k+=1
    else:
        c+=1
print("vowel",k)
print("cons",c)