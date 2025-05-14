from stack_linked_list import StackLinkedList as Stack, StackLinkedList


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.data = None

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.num_items = 0

    def search_node(self, key, node): # returns the node, if found
        current_node = node
        if current_node is None:
            return None
        if current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self.search_node(key, current_node.left)
        elif key > current_node.key:
            return self.search_node(key, current_node.right)

    def find(self, key, root):  # returns True if key is in a node of the tree, else False

        if self.root is None:
            return False

        while root: # root != None
            if root.key == key:
                return True
            elif key < root.key:
                root = root.left
            elif key > root.key:
                root = root.right

        return False

    def find_min(self): # returns min value in the tree
        if not(self.is_empty()):
            current = self.root

            while current.left:
                current = current.left

            return current.key
        else:
            return None

    def find_max(self):     # returns max value in the tree
        if not(self.is_empty()):
            current = self.root

            while current.right:
                current = current.right

            return current.key
        else:
            return None

    def insert(self, new_key):  # inserts a node with key into the correct position if not a duplicate.

        if self.root is None:
            self.root = TreeNode(new_key)
            self.num_items += 1
            return
        current = self.root
        while current is not None:
            if new_key < current.key:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(new_key)
                    break
            elif new_key > current.key:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(new_key)
                    break
        self.num_items += 1

    def delete(self, key):  # deletes the node containing key, assumes such a node exists
        if self.find(key, self.root):
            to_delete = None
            root = self.root
            parent_left = None
            parent_right = None
            while root: # root != None
                if root.key == key:
                    to_delete = root
                    break
                elif key < root.key:
                    parent_left = root
                    parent_right = None
                    root = root.left
                elif key > root.key:
                    parent_right = root
                    parent_left = None
                    root = root.right

            if to_delete.left is None and to_delete.right is None:
                if parent_left:
                    parent_left.left = None
                elif parent_right:
                    parent_right.right = None
            else:
                self.helper_delete(to_delete)

            self.num_items -= 1
        else:
            raise ValueError("Key not found")


    def helper_delete(self, node):
        left = False
        right = False
        while node.right or node.left:

            if node.left and node.right is None:
                node.key = node.left.key
                left = True
                parent = node
                node = node.left
            elif node.right and node.left is None:
                node.key = node.right.key
                right = True
                parent = node
                node = node.right
            else:
                original = node
                parent = node
                node = node.right
                left = False
                right = True
                while node.left:
                    parent = node
                    node = node.left
                    right = False
                    left = True
                original.key = node.key

        if left:
            parent.left = None
        elif right:
            parent.right = None


    def print_tree(self, root):  # print inorder the entire tree
        if root.left:
            self.print_tree(root.left)

        print(root.key)

        if root.right:
            self.print_tree(root.right)

    def is_empty(self):  # returns True if tree is empty, else False
        return self.root is None

    def inorder_print_tree(self, node): # print inorder the subtree of self
        self.print_tree(node)

    def print_levels(self, root, level = 0): # inorder traversal prints list of pairs, [key, level of the node] where root is level

        if root.left:
            self.print_levels(root.left, level + 1)

        print(f"({root.key}, {level})")

        if root.right:
            self.print_levels(root.right, level + 1)

    def count_right_nodes(self, root, c = 0):
        count = c
        if root.right is not None:
            count += 1
            count = self.count_right_nodes(root.right, count)

        if root.left is not None:
            count = self.count_right_nodes(root.left, count)

        return count


t1 = BinarySearchTree()


t1.insert(6)    # A, lvl 0
t1.insert(4)    # B, lvl 1
t1.insert(7)    # C, lvl 1
t1.insert(3)    # D, lvl 2
t1.insert(5)    # E, lvl 2
t1.insert(1)
t1.insert(2)
t1.insert(10)
t1.insert(9)

# inorder output = DBEAC (3, 4, 5, 6, 7)

t1.print_tree(t1.root)
# t1.inorder_print_tree(t1.root.left)
# t1.print_levels(t1.root)
print()
print(t1.count_right_nodes(t1.root))













