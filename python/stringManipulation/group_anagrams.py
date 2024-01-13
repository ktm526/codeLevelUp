#https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for str_ in strs:
            sorted_strs.append(''.join(sorted(str_)))
        #print(sorted_strs)
        str_dict = defaultdict(list)
        for i in range(len(sorted_strs)):
            str_dict[sorted_strs[i]].append(i)
        result = []
        for i in range(len(str_dict.keys())):
            #print(list(str_dict.keys())[0])
            result.append([])
            for num in str_dict[list(str_dict.keys())[i]]:
                #print(num)
                result[i].append(strs[num])
        #print(result)
        return result
    

    # class Solution:
    # def groupAnagrams(self, strs):
    #     str_dict = defaultdict(list)
    #     for str_ in strs:
    #         # Sorting the string and using it as a key in the dictionary
    #         sorted_str = ''.join(sorted(str_))
    #         str_dict[sorted_str].append(str_)

    #     # Generating the result list from the dictionary values
    #     result = list(str_dict.values())
    #     return result