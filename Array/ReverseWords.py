# 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

# Problem Restatement
# Return the string reversing the order of the words. Remove spaces at the beginning and at the end of the string.

# Thought Process
# Trim leading and trailing spaces using .strip()
# Use .split() to split the words and store them in an array
# Reverse the list of words
# Join the words back together

# Time Complexity: O(n) - each operation (strip, split, join) goes through the entire string once
# Space Complexity: O(n) - additional space is required to store the list of words and the resulting string

def reverseWords(self, s):
    s.strip()
    words = s.split()
    new_string = []

    for i in range(len(words)-1, -1, -1):
        new_string.append(words[i])
    
    return ' '.join(new_string)
