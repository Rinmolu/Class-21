list1=[23,83,49,67,12,98]
print("Original List ",list1)
count=0
for i in list1:
    count=count+i
avg=count/len(list1)
print("Sum ",count)
print("Average Is...  ",avg)
list1.sort()
print("Smallest Number Is...  ",list1[0])
print("Largest Number Is...  ",list1[-1])
