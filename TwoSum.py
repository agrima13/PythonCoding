
class Solution:
    def twoSum(nums, target) -> [int]:
        result = {}
        for index, element in enumerate(nums):
            difference = target - element
            if element not in result:
                result[difference] = index
            else:
                return [index, result[element]]


    if __name__ == '__main__':
        nums = [2,7,11,15]
        print(twoSum(nums,17))