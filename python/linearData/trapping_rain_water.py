#https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        for i in range(0, max(height)):
            print(height)
            pos1 = 0
            pos2 = 0
            for x in range(0, len(height)):
                if(height[x] != 0):
                    pos1 = x
                    break
            for x in range(len(height)-1, 0, -1):
                if(height[x] != 0):
                    pos2 = x
                    break

            for x in range(pos1, pos2):
                if(height[x] == 0):
                    result += 1

            for x in range(0, len(height)):
                height[x] = max([0, height[x]-1])

        return result