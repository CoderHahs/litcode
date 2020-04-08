# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if (sorted_str in anagrams.keys()):
                anagrams[sorted_str].append(strs[i])
            else:
                anagrams[sorted_str] = []
                anagrams[sorted_str].append(strs[i])

        output = []
        for key in anagrams.keys():
            output.append(anagrams[key])

        return output
