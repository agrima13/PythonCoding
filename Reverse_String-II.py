class Solution:
    def reverseStr(s: str, k: int):
        a = list(s)
        for i in range(0, len(a),2*k):
            a[i:i + k] = reversed(a[i:i + k])
        return "".join(a)

    if __name__ == '__main__':
        print(reverseStr("abcdef",2))