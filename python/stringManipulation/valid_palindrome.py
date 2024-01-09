#https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        strs = []
        for char in s.lower():
            if char.isalnum():
                strs.append(char)
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True