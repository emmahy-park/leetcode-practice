# 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]

# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 4:
# Input: root = []
# Output: []

# Problem Restatement
# Return the values of the nodes you can see ordered from top to bottom from the right side

# Thought Process
# To use BFS, perform a level-order traversal using a queue.
# For each level, process all nodes in that level.
# The last node processed in each level is the one visible from the right side.

# Time Complexity: O(n) - the total number of operations inside the inner for loop is n - the number of nodes in the tree
# Space Complexity: O(n) - for storing up to n value in total

from collections import deque

def rightSideView(self, root):
    if root is None:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        currentLevelSize = len(queue)

        for i in range (currentLevelSize):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            if i == currentLevelSize -1:
                result.append(node.val)
    
    return result