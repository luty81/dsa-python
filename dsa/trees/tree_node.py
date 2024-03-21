class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None
    

class BinarySearchTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data) if root_data else None

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
    
    def r_insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            
        return self.__r_insert(self.root, data)

    def r_find(self, value) -> TreeNode | None:
        return self.__r_find(self.root, value) if self.root is not None else None

    def to_array(self):
        if self.root is None:
            return self.root
        
        return [self.root.data] + self.__to_heap_array(self.root)



    def __r_find(self, node: TreeNode, value): 
        if node.data == value:
            return node
        
        if node.left:
            return self.__r_find(node.left, value)
        
        if node.right:
            return self.__r_find(node.right, value)

        return None
    
    def __r_insert(self, node: TreeNode, data) -> bool:
        if node.data == data:
            return False

        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
                return True
            
            return self.__r_insert(node.left, data)        

        if data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
                return True
            
            return self.__r_insert(node.right, data)

    def __to_heap_array(self, node: TreeNode, result=None):     
        if result is None:
            result = []

        if node is None or node.is_leaf():
            return result
        

        result.append(node.left.data if node.left else None)
        result.append(node.right.data if node.right else None)
        self.__to_heap_array(node.left, result)
        self.__to_heap_array(node.right, result)
        return result




