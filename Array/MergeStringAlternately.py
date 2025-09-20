# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
#
# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
#
# Problem Restatement
# We are given two strings, word1 and word2. We need to merge them by alternating characters, always starting with word1.
# If one string is longer, after the shorter one is exhausted, we append the remaining characters of the longer string.
#
# Thought Process
# 1. Edge Cases
# - If one of the strings is empty, the merged string is just the other string
# 2. Alternating Characters
# - While both strings have characters left, alternate between taking one from word1 and one from word2
# 3. Handling Different Lengths
# - Once the shorter string is fully used, append the leftover characters from the longer string.
# 4. Time Complexity
# - We touch each character once, so the algorithm runs in O(n+m) time, where n and m are the lengths of the two strings
# - Space complexity is also O(m+n) for the result string

def mergeAlternately(self, word1, word2):

    temp = []

    # Iterate through both words until one runs out
    for i in range(min(len(word1), len(word2))):
        temp.append(word1[i])
        temp.append(word2[i])
    
    # Add leftovers
    if len(word1) > len(word2):
        temp.append(word1[len(word2):])
    else:
        temp.append(word2[len(word1):])
    
    return "".join(temp)
