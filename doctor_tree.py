# doctor_tree.py

class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def _find(self, node, name):
        """Helper function to locate a node by name."""
        if node is None:
            return None
        if node.name == name:
            return node
        left = self._find(node.left, name)
        if left:
            return left
        return self._find(node.right, name)

    def insert(self, parent_name, child_name, side):
        """Insert a new doctor under a parent on 'left' or 'right'."""
        parent = self._find(self.root, parent_name)
        if not parent:
            print(f"Parent '{parent_name}' not found.")
            return

        if side == "left":
            if parent.left is None:
                parent.left = DoctorNode(child_name)
            else:
                print(f"Left side of {parent_name} already occupied.")
        elif side == "right":
            if parent.right is None:
                parent.right = DoctorNode(child_name)
            else:
                print(f"Right side of {parent_name} already occupied.")
        else:
            print("Invalid side. Use 'left' or 'right'.")

    def preorder(self, node):
        """Root -> Left -> Right"""
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        """Left -> Root -> Right"""
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        """Left -> Right -> Root"""
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Example usage:
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
