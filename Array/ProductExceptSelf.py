# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Problem Restatement
# The output array should contain the product of all the elements of nums except nums[i]
# For Example 1 -> [2x3x4, 1x3x4, 1x2x4, 1x2x3] = [24, 12, 8, 6]
# For Example 2 -> [1x0x-3x3, -1x0x-3x3, -1x1x-3x3, -1x1x0x3, -1x1x0x-3] = [0, 0, 9, 0, 0]

# Thought Process
# Loop through the array, for each element split into prefix and suffix products
# anwer[i] = (product of elements to the left of i) x (product of elements to the right of i)

def productExceptSelf(self, nums):

    n = len(nums)
    left = [1] * n
    right = [1] * n
    result = [1] * n

    # Left Array
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    
    # Right Array
    for i in range(n-2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    # Combine left and right
    for i in range(n):
        result[i] = left[i] * right[i]
    
    return result