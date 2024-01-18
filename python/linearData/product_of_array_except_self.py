#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        p = 1
        for x in range(0, len(nums)):
            result.append(p)
            p *= nums[x]
        p=1
        for x in range(len(nums)-1, -1, -1):
            result[x] *= p
            p*= nums[x]
        return result