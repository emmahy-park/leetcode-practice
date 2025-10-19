# 605. Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

# Problem Restatement
# Return true if at least n number of flowers can be planted in the flowerbed, where flowers cannot be planted in adjacent plots.

# Thougt Process
# Case 1:
# [1, 0, 0, 0, 1, 0, 0], n = 2

# Check the first plot -> not empty

# Check the second plot -> empty 
# Check the third plot -> empty
# Check the fourth plot -> empty -> plant flower at flowerbed[2]

# Check the fifth plot -> not empty

# Check the sixth plot -> empty 
# Check the last plot -> empty -> plant flower at flowerbed[6]

# return true

# Case 2:
# [0, 0, 0, 0, 1, 0] n = 2
# Check the first plot -> empty
# Check the second plot -> empty -> plant flower at flowerbed[0]

# Check the third plot -> empty
# Check the fourth plot -> empty -> plant flower at flowerbed[2]

# Check the fifth plot -> not empty

# Check the sixth plot -> empty 

# return true

# Case 3:
# [0, 0, 0, 1, 0, 0] n = 2
# Check the first plot -> empty
# Check the second plot -> empty -> plant flower at flowerbed[0]

# Check the third plot -> empty
# Check the fourth plot -> not empty

# Check the fifth plot -> empty
# Check the last plot -> empty -> plant flower at flowerbed[5]

# return true

# - To decide whether a flower can be planted at position i, check three plots: previous, current, and next
# - A flower can be planted at i only if all three are empty
# - For the first plot, assume there's no left neighbour (previous = empty)
# - For the last plot, assume there's no right neighbour (next = empty)
# - Each time a flower is planted, mark the spot as filled to avoid violating adjacency for future checks
# - Continue looping through the array, planting where valid, and count how many flowers are planted
# - Return True if the total planted flowers >= n; otherwise return Fasle

# Time Complexity: 
# - Check for edge cases: O(1)
# - O(n) for looping through the entire flowerbed array; max n if not returned earlier
# Space Complexity: O(1) for not creating any new array

def canPlaceFlowers(self, flowerbed, n):

    counter = 0

    if len(flowerbed) > 2:
        if flowerbed[0] == flowerbed[1] == 0:
            counter += 1
            flowerbed[0] = 1

        if flowerbed[len(flowerbed) - 1] == flowerbed[len(flowerbed)-2] == 0:
            counter += 1
            flowerbed[len(flowerbed) - 1] = 1
    else:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n == 0
        elif len(flowerbed) == 2:
            if flowerbed[0] == flowerbed[1] == 0:
                return n <= 1
            else:
                return n == 0

    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] == flowerbed[i+1] == flowerbed[i+2] == 0:
            counter += 1
            flowerbed[i+1] = 1

            if counter == n:
                return True
    
    return counter >= n

# More elegant O(n) / O(1) implementations by ChatGPT
def canPlanceFlowers(self, flowerbed, n):
    count = 0
    length = len(flowerbed)

    for i in range(length):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i-1] == 0)
            empty_right = (i == length - 1) or (flowerbed[i+1] == 0)

            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1

                if count >= n:
                    return True
    
    return count >= n

