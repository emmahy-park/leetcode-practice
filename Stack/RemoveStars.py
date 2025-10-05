# 2390. Removing Stars From a String
# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Example 1:
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".

# Example 2:
# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.

# Problem Restatement
# Remove the closest non-star character to its left and the star till all stars are removed

# Thought Process
# Initialize an empty stack.
# Iterace through each character in the string - if the character is not a * push it onto the stack,
# and if it's a *, pop the most recent character from the stack.
# After processing all characters, return the joined characters in stack.

# Time Complexity: O(n) for looping through the string
# Space Complexity: O(n) for storing characters in the stack (in the worst case every character is stored)

def removeStars(self, s):

    stack = []

    for char in s:
        if char != '*':
            stack.push(char)
        else:
            stack.pop()
    
    return "".join(stack)