# 383. Ransom Note
# Easy

# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# You may assume that both strings contain only lowercase letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = dict()
        for l in magazine:
            if l in letters.keys():
                letters[l] += 1
            else:
                letters[l] = 1
        for l in ransomNote:
            if l not in letters.keys():
                return False
            letters[l] -= 1

        for key in letters.keys():
            if letters[key] < 0:
                return False
        return True
