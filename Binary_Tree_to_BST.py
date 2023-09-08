# Given a Binary Tree, convert it to Binary Search Tree in such a way that keeps the original structure of Binary Tree intact.

def inorder(node, result_list):
    if not node:
        return
    inorder(node.left, result_list)
    result_list.append(node.data)
    inorder(node.right, result_list)

def replace_with_sorted_values(node, sorted_values, index):
    if not node:
        return
    
    replace_with_sorted_values(node.left, sorted_values, index)

    node.data = sorted_values[index[0]]
    index[0] += 1

    replace_with_sorted_values(node.right, sorted_values, index)

class Solution:
    
    def binaryTreeToBST(self, root):
        values = []
    
        inorder(root, values)
        values.sort()
        current_index = [0]
        replace_with_sorted_values(root, values, current_index)
        return root
