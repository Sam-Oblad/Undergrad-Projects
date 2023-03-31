'''BST'''
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.treeSize = 0

    def size(self):
        return self.treeSize

    def is_empty(self):
        return self.treeSize == 0

    def height(self):
        if self.root == None:
            return -1
        return self._height(self.root)

    def _height(self, node):
        if node == None:
            return -1
        leftHeight = self._height(node.left)
        rightHeight = self._height(node.right)
        return 1 + max(leftHeight, rightHeight)

    def add(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._add(value, self.root)
        self.treeSize += 1

    def _add(self, value, node):
        if value < node.val:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._add(value, node.left)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._add(value, node.right)

    def remove(self, item):
        self.root = self._remove(self.root, item)
        self.treeSize -= 1
        return self

    def _remove(self, node, item):
        if node is None:
            return node
        if item < node.val:
            node.left = self._remove(node.left, item)
        elif item > node.val:
            node.right = self._remove(node.right, item)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self._min(node.right)
            node.val = min_node.val
            node.right = self._remove(node.right, min_node.val)

        return node

    def _min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find(self, item):
        if self.is_empty():
            raise ValueError("Tree is empty")
        else:
            node = self.root
            while node is not None:
                if node.val == item:
                    return node.val
                elif node.val > item:
                    node = node.left
                else:
                    node = node.right
            raise ValueError("Item not found in tree")

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

    def preorder(self):
        def helper(node):
            if node is None:
                return []
            else:
                result = []
                result.append(node.val)
                result += helper(node.left)
                result += helper(node.right)
                return result
        
        return helper(self.root)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node is not None:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.val)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            print(node.val)
            self._print_tree(node.left)
            self._print_tree(node.right)
