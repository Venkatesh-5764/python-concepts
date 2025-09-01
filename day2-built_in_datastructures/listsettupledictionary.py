# Create a list and print all elements.
li=[112,14,15,1,18]
for i in li:
    print(i,end="\n")
# Access elements using positive & negative indexing.
print(li[-1],"is the last element")
print(li[1],"is the second element from the list")
print(li[0],"is the first element in the list")
print(len(li),"is the length of the given list")
# Slice a list (list[2:5], list[::-1]).
print(li[::])
print(li[1::])
print(li[1::2])
print(li[2:4])
# Append an element to a list.
li.append(1000)
print(li)
# Insert an element at a specific index.
li[3]='venky'
print(li)
# Remove an element by value.
li.remove('venky')
print(li)
# Remove an element by index (pop).
print(li.pop(2))

# Find length of a list.
print(len(li))
# Find max and min element.
print(max(li),min(li))
maa=li[0]
minii=li[0]

for j in range (len(li)):
    if(li[j]>maa):
        maa=li[j]
    if(li[j]<minii):
        minii=li[j]
print(maa,minii)

# Sort a list in ascending and descending order.
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if(li[i]>li[j]):
            li[i],li[j]=li[j],li[i]
print("Ascending order:",li)
li.reverse()
print("Descending order:",li)
# Reverse a list without using slicing.
for i in range(len(li)//2):
    li[i],li[len(li)-1-i]=li[len(li)-1-i],li[i]
print(li)
# Count occurrences of an element.
count=0
for i in range(len(li)):
    if(li[i]==14):
        count+=1                
print("14 occurs",count,"times")

# Find index of an element.
for i in range(len(li)):
    if(li[i]==18):
        print("index of 18 is",i)


# Copy a list (shallow vs deep copy).
li2=li.copy()
print("copied list is",li2)


# Concatenate two lists.
li3=[1,2,3,4]
li4=li+li3      
print("concatenated list is",li4)