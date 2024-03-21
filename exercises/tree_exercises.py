
from dsa.trees.tree_node import BinarySearchTree, TreeNode


def invert_bst(bst: BinarySearchTree) -> BinarySearchTree:
    _invert_node_children(bst.root)
    return bst

def search_bfs(bst: BinarySearchTree) -> list:
    queue, result = [], []
    if bst.root is not None:
        queue.append(bst.root)
        while any(queue):
            visited = queue.pop(0)
            result.append(visited.data)
            if visited.left:
                queue.append(visited.left)
            if visited.right:
                queue.append(visited.right)
    
    return result

def dfs_in_pre_order(bst: BinarySearchTree) -> list:
    result = []
    def traverse(node: TreeNode):
        result.append(node.data)

        if node.left:
            traverse(node.left)
        
        if node.right:
            traverse(node.right)
        
    traverse(bst.root)
    return result


def dfs_in_post_order(bst: BinarySearchTree) -> list:
    result = []
    def traverse(node: TreeNode):
        if node.left:
            traverse(node.left)

        if node.right:
            traverse(node.right)
        
        result.append(node.data)
    
    traverse(bst.root)
    return result

def dfs_in_order(bst: BinarySearchTree) -> list:
    result = []
    def traverse(node: TreeNode):
        if node.left:
            traverse(node.left)

        result.append(node.data)
        
        if node.right:
            traverse(node.right)
    
    traverse(bst.root)
    return result


def _invert_node_children(node: TreeNode):
    if node and node.is_leaf():
        return

    node.left, node.right = node.right, node.left
    if node.left:
        _invert_node_children(node.left)
    if node.right:
        _invert_node_children(node.right)
