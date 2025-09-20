# 88. Merge Sorted Array
#
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#
# The arrays are sorted in non-decreasing order
# nums1 stores the final sorted array
#
# Test Cases
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
#
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# 
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
#
# Solution:
# Copy nums1's valid elements to temp array
# Merge temp and nums2 into nums1
# If temp or nums2 still have leftovers move them to nums1

def merge(self, nums1, m, nums2, n):

    temp = nums1[:m]
    i = 0 # temp indices
    j = 0 # nums2 indices
    k = 0 # nums1 indices

    while i < m and j < n:
        if temp[i] < nums2[j]:
            nums1[k] = temp[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    while i < m:
        nums1[k] = temp[i]
        i += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1
    
    return nums1

# Time complexity is O(m+n) for merging temp and nums2 into nums1, since we compare elements one by one until all m+n elements are processed
# Space complexity is O(m) for allocating temp to store the first m elements of nums1