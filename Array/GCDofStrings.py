# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
# Problem Restatement
# Return the largest string that divides both str1 and str2
#
# Thougt Process
# Go through both strings to find the common substrings
# For instance, in example 1, loop through both str1 and strw and count the characters that match
# 
# def gcdOfStrings(self, str1, str2):
#     temp = []
#
#     for i in range(min(len(str1), len(str2))):
#         if str1[i] == str2[i]:
#             temp.append(str1[i])
#             continue
#         else:
#             break
#
#     return "".join(temp)
#
# This method only collects the common prefix and does not necessarily give the greatest common divisor. (Example 2)
# 
# Check that str1 + str2 == str2 + str1, if not then there is no solution.
# Find the gcd of the lengths of two strings - the length of the divisor string can't be greater than this gcd
# Return the substring of length equal to the gcd
def gcdOfStrings(self, str1, str2):

    if (str1 + str2 != str2 + str1):
        return ""
    
    a = max(len(str1), len(str2))
    b = min(len(str1), len(str2))

    # find the gcd of the length two strings
    while (b != 0):
        temp = b
        remainder = a % b
        a = temp
        b = remainder
    
    return str1[:a]