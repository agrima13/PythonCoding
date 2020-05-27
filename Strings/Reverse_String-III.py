class Solution:

    def reverseWords( s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])

    if __name__ == '__main__':
        print(reverseWords("The Metahumans have attacked Central City again"))




