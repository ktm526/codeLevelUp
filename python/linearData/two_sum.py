#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0,0]
        for num in nums:
            if (target - num) in nums[ (nums.index(num))+1:]:
                temp = nums[nums.index(num)+1:].index(target-num)
                result = [ nums.index(num), nums.index(num)+temp+1 ]
                break
        return result