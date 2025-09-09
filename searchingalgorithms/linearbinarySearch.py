def linearsearch(arr,targetvar):
    for i in range(0,len(arr)):
        if(arr[i]==targetvar):
            print("element found at position ",i)
def binarysearch(arr,targetvar):
    arr.sort()
    lef=0
    rig=len(arr)-1
    while lef<=rig:
        mid=(lef+rig)//2
        if(arr[mid]==targetvar):
            return mid
        elif (arr[mid]<targetvar):
            lef=mid+1
        else:
            
            rig=mid-1
    return -1
resul=binarysearch([13,14,16,19,22,24,56],24)
print(resul)