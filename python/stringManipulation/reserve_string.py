#https://leetcode.com/problems/reverse-string/
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)):
            s.insert(0, s.pop(i))
            