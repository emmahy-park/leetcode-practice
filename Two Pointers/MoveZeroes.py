# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
# Problem Restatement
# Using two pointers, move all 0's in a given integer array to the end, while keeping the relative order or non-zero elements the same.
#
# Thought Process
# Using two pointers, we have one pointer tracking the position where the next non-zero element should go (p1). This pointer only advances when we place a non-zero value at that position.
# The second pointer (p2) iterates through the array, looking for non-zero elements. When a non-zero element is found, it's swaped with the element at position p1, then p1 is incremented.
#
# Time Complexity: O(n) for iterating through the array once with p2
# Space Complexity: O(1) for using a single integer temp for swapping

def moveZeroes(self, nums):
    p1 = 0
    temp = []
    
    for p2 in range(len(nums)):
        if nums[p2] != 0:
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp
            p1 += 1
    
    return nums