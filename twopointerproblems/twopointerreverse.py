l=[1,2,3,4,5,6,7]
n=len(l)
lef=0
rig=n-1
while(lef<rig):
    temp=l[lef]
    l[lef]=l[rig]
    l[rig]=temp
    lef =lef+1
    rig= rig-1
print(l)