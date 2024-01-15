#https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = ""
        result = ""
        for x in range(len(s), 0, -1):
            for y in range(0, len(s) - x + 1):
                part_s = s[y:y+x]
                reverse_part = ''.join(reversed(list(part_s)))
                if part_s == reverse_part:
                    temp = part_s
                    print("temp", temp)
            if len(temp) > len(result):
                result = temp
            print(temp, result)
        return result