## Program to calculate the H Index of a researcher

## What is an H Index ?

# H Index = If Atleast x number fo papers have been cited atleast x number of times then your HIndex = X
# For example If my array has 1,4,1,4,2,1,3,5,6 citations then here there are atleast 4 papers that have been cited 4 times.
# Hence the Hindex = 4

arr = [1,4,1,4,2,1,3,5,6]
j = 0
ans = 0
count = 0

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[j] >= arr[i]:
            count = count + 1

    if(arr[i] == count):
        h_index = arr[i]

print("The H Index is", h_index)
