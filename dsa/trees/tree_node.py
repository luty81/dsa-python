class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def insert(self, data) -> bool:
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            return True
        
        current_node = self.root
        while current_node:
            if data == current_node.data:
                return False

            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = TreeNode(data)
                    return True
                
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = TreeNode(data)
                    return True
                
                current_node = current_node.right

    def find(self, value) -> TreeNode | None:
        current = self.root
        while current:
            if current.data == value:
                return current

            current = current.left if value < current.data else current.right

        return None
                





        





