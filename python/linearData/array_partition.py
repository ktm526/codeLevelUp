#https://leetcode.com/problems/array-partition/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        result = 0
        for i in range(len(sorted_nums),0, -2):
            result+=sorted_nums[-i]
        return result