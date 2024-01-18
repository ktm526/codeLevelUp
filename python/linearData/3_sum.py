#https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for x in range(0, len(nums)-2):
            for y in range(x+1, len(nums)-1):
                for z in range(y+1, len(nums)):
                    #print(x,y,z)
                    if (nums[x]+nums[y]+nums[z]) is 0: #and nums[x]!= nums[y] and nums[y] != nums[z] and nums[z] != nums[x]:
                        temp = [nums[x],nums[y],nums[z]]
                        temp = sorted(temp)
                        print(temp)

                        if(temp not in result): 
                            result.append(temp)
            
        return result