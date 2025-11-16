# 700. Search in a Binary Search Tree
# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
# If such a node does not exist, return null.

# Example 1:
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

# Example 2:
# Input: root = [4,2,7,1,3], val = 5
# Output: []

# Problem Restatement
# Return the subtree rooted with the node's value equal to given val

# Thought Process
# Since this is a binary search tree, the left subtree values is always smaller than the right subtree values
# If val is equal to the current node, subtree root is found - return the entire subtree
# If val is less than the current node's value, move left
# If val is greather, move right
# If the value doesn't exist, return null

# Time Complexity: O(h) time (h = tree height) - only one path is found and no need to look at all nodes
# Space Complexity: O(1) constant memory

def searchBST(self, root, val):
    while root:
        if val == root.val:
            return root
        elif val < root.val:
            root = root.left
        elif val > root.val:
            root = root.right
    
    return None
