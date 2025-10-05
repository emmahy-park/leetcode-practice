# 1431. Kids With the Greatest Number of Candies
# There are n kids with candies. You are given an integer array candies, 
# where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, 
# denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, 
# they will have the greatest number of candies among all the kids, or false otherwise.

# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

# Example 2:
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

# Example 3:
# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]

# Problem Restatement
# Return a boolean array where it's true if candies[i] + extraCandies >= max candies

# Thought Process
# Find the maximum number of candies among all kids first. Then loop through each kid's candy count and calculate the total if they received the extraCandies.
# Compare the new total with the maximum number found. Return the list of boolean values corresponding to each kid's result.

# Time Complexity: O(n) for looping through the candies array (finding the max number of candies and comparing each kid's total with the max num)
# Space Complexity: O(n) for creating a new result list to store one boolean value per kid

def kidsWithCandies(self, candies, extraCandies):

    maxNum = 0
    result = []

    for n in candies:
        if n > maxNum:
            maxNum = n

    for c in candies:
        if c + extraCandies >= maxNum:
            result.append(True)
        else:
            result.append(False)
    
    return result