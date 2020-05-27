s = "The metahumans have atacked Central City again"

#Method 1 to reverse the string
print(s[len(s)::-1])

#Method 2 : Without specifying the length explicitly
print(s[::-1])

##Method 3 : Loop

reversedString=[]
index = len(s) # calculate length of string and save in index
while index > 0:
    reversedString += s[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
print(str(reversedString)) # reversed string


## Method 4

reversedstring=''.join(reversed(s))
print(reversedString)

