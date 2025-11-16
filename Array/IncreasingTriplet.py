# 334. Increasing Triplet Subsequence
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k 
# and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.

# Problem Restatement
# Return True if there's a triplet of indices (i, j, k) where i < j < k
# Return False otherwise

# Thought Process
# Going from left to right, keep track of two values - smallest so far, and the second smallest so far that is greater than the first
# If the next number is smaller or equal to the first, update the first
# Else if the next number is greater than the first but smaller or equal to the second, update the second
# Else if the next number is greater than the second, return True
# If the loop completes without returning True, then return False at the end

# Time Complexity: O(n) for going through the entire nums
# Space Complexity: O(1) - memory usage doesn't grow with input size

def increasingTriplet(self, nums):
    first = float('inf')
    second = float('inf')

    for n in nums:
        if n <= first:
            first = n
        elif n > first and n <= second:
            second = n
        elif n > first and n > second:
            return True
        
    return False

