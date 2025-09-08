l=[32,44,1,33,2,3,94]
maax=l[0]
miin=l[0]
for i in l:
    if i>maax:
        maax=i
    if i<miin:
        miin=i
print("Maximum is:",maax)
print("Minimum is:",miin)   