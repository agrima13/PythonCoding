string = ['H','E','L','L',"O"]

def reverse_str(s):
    j = len(s) - 1
    for i in range(int(len(s)/2)):
        s[i],s[j]=s[j],s[i]
        j = j -1
    return s

print(reverse_str(string))