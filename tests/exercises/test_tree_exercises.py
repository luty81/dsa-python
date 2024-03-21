
from dsa.trees.tree_node import BinarySearchTree
from exercises.tree_exercises import *


def test_invert_bst():
    bst = BinarySearchTree(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(15)
    bst.insert(25)
    bst.insert(35)
    bst.insert(45)

    expected_bst = [30, 20, 40, 15, 25, 35, 45]
    expected_inverted_bst = [30, 40, 20, 45, 35, 25, 15]
    assert bst.to_array() == expected_bst
    assert invert_bst(bst).to_array() == expected_inverted_bst
    assert invert_bst(bst).to_array() == expected_bst
    assert invert_bst(bst).to_array() == expected_inverted_bst


def test_invert_bst_unbalanced():
    bst = BinarySearchTree(50)
    bst.insert(40)
    bst.insert(30)
    bst.insert(20)
    bst.insert(10)

    assert bst.to_array() == [50, 40, None, 30, None, 20, None, 10, None]
    invert_bst(bst).to_array() == [50, 40, None, 30, None, 20, None, 10, None] 

def test_invert_bst_only_root():
    assert invert_bst(BinarySearchTree(10)).to_array() == [10]

    bst = BinarySearchTree(10)
    bst.insert(5)
    bst.insert(8)
    initial_bst = bst.to_array()
    assert initial_bst == [10, 5, None, None, 8]
    assert invert_bst(bst).to_array() == [10, None, 5, 8, None]
    assert invert_bst(bst).to_array() == initial_bst

def test_bst_breadth_first_search():
    bst = _create_bst_from_([47, 21, 76, 18, 27, 53, 82])
    assert bst.to_array() == [47, 21, 76, 18, 27, 53, 82]

    assert search_bfs(bst) == [47, 21, 76, 18, 27, 53, 82]

def test_bst_depth_first_search_pre_order():
    bst = _create_bst_from_([47, 21, 76, 18, 27, 53, 82])
    assert dfs_in_pre_order(bst) == [47, 21, 18, 27, 76, 53, 82]
    assert dfs_in_post_order(bst) == [18, 27, 21, 53, 82, 76, 47]
    assert dfs_in_order(bst) == [18, 21, 27, 47, 53, 76, 82]

def _create_bst_from_(array: list) -> BinarySearchTree:
    bst = BinarySearchTree(array.pop(0))
    while any(array):
        bst.insert(array.pop(0))
    return bst


