# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Project Restatement
# Reverse only the vowels of a string

def reverseVowels(self, s):
    vowels = set("aeiouAEIOU")
    vowel = []
    
    # Find all vowels in the string and reverse them
    for char in s:
        if char in vowels:
            vowel.append(char)
    vowel.reverse()

    result = []
    index = 0

    for char in s:
        if char in vowels:
            result.append(vowel[index])
            index += 1
        else:
            result.append(char)

    return ''.join(result)