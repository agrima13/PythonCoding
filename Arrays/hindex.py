## Program to calculate the H Index of a researcher

## What is an H Index ?

# H Index = If Atleast x number fo papers have been cited atleast x number of times then your HIndex = X
# For example If my array has 1,4,1,4,2,1,3,5,6 citations then here there are atleast 4 papers that have been cited 4 times.
# Hence the Hindex = 4

def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    citations.sort()
    n = len(citations)
    for i,c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0


arr = [1,4,1,4,2,1,3,5,6]
print(hIndex(arr))

## Time Complexity here is O(nlogn)
## Space Complexity O(1)
