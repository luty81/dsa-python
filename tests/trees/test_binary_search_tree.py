

from dsa.trees.tree_node import BinarySearchTree, TreeNode


def test_bst_init():
    bst = BinarySearchTree(10)
    assert bst.root.data == 10
    assert bst.root.left is None
    assert bst.root.right is None

def test_insert():
    bst = BinarySearchTree(30)
    bst.insert(50)
    bst.insert(10)

    assert bst.root.data == 30
    assert _is_leaf_(bst.root.left, 10)
    assert _is_leaf_(bst.root.right, 50)

    bst.insert(75)
    assert bst.root.data == 30
    assert _is_leaf_(bst.root.left, 10)
    assert bst.root.right.data == 50
    assert bst.root.right.left is None
    assert _is_leaf_(bst.root.right.right, 75)

    bst.insert(40)
    assert bst.root.data == 30
    assert _is_leaf_(bst.root.left, 10)
    assert bst.root.right.data == 50
    assert _is_leaf_(bst.root.right.left, 40)
    assert _is_leaf_(bst.root.right.right, 75)

    bst.insert(5)
    assert bst.root.data == 30
    assert bst.root.left.data == 10
    assert _is_leaf_(bst.root.left.left, 5)
    assert bst.root.left.right is None

    bst.insert(15)
    assert bst.root.data == 30
    assert bst.root.left.data == 10
    assert _is_leaf_(bst.root.left.left, 5)
    assert _is_leaf_(bst.root.left.right, 15)

def test_find():
    bst = BinarySearchTree(30)
    bst.insert(25)
    bst.insert(20)
    bst.insert(15)
    bst.insert(10)
    bst.insert(5)

    assert bst.find(50) is None
    assert bst.find(1) is None
    for key in range(5, 31, 5):
        assert bst.find(key).data == key


def test_r_find():
    bst = BinarySearchTree(30)
    bst.insert(25)
    bst.insert(20)
    bst.insert(15)
    bst.insert(10)
    bst.insert(5)

    assert bst.r_find(50) is None
    assert bst.r_find(1) is None
    for key in range(5, 31, 5):
         assert bst.r_find(key).data == key


    bst = BinarySearchTree(None)
    assert bst.r_find(1) is None
    bst = BinarySearchTree(1)
    assert bst.r_find(1).data == 1

def _is_leaf_(node: TreeNode, excepted_value):
    assert node.data == excepted_value
    assert node.left is None
    assert node.right is None
    return True
