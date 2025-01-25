class AVLNode:
    def __init__(self, key):
        self.key = key  # Value of the node
        self.height = 1  # Height of the node
        self.left = None  # Left child
        self.right = None  # Right child

def find_max(current):
    if current is None:
        return None  # If the tree is empty, return None

    while current.right is not None:  # Traverse to the rightmost node
        current = current.right

    return current.key  # Return the key of the rightmost node

def get_height(node):
    if not node:
        return 0  # Return 0 if the node is None
    return node.height  # Return the height of the node

def get_balance(node):
    if not node:
        return 0  # Balance factor is 0 for None
    return get_height(node.left) - get_height(node.right)  # Left height - Right height

def left_rotate(z):
    y = z.right  # Set y to the right child of z
    T2 = y.left  # Temporarily store the left subtree of y

    # Perform rotation
    y.left = z
    z.right = T2

    # Update heights
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y  # Return the new root

def right_rotate(y):
    x = y.left  # Set x to the left child of y
    T3 = x.right  # Temporarily store the right subtree of x

    # Perform rotation
    x.right = y
    y.left = T3

    # Update heights
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x  # Return the new root

def insert(root, key):
    if not root:
        return AVLNode(key)  # If the tree is empty, create a new node

    if key < root.key:
        root.left = insert(root.left, key)  # Insert into the left subtree
    elif key > root.key:
        root.right = insert(root.right, key)  # Insert into the right subtree
    else:
        return root  # Duplicate keys are not allowed

    # Update the height of the current node
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Get the balance factor to check if the node is balanced
    balance = get_balance(root)

    # Perform rotations to balance the tree
    if balance > 1:  # Left-heavy
        if key < root.left.key:
            return right_rotate(root)  # Left-Left case
        else:
            root.left = left_rotate(root.left)  # Left-Right case
            return right_rotate(root)

    if balance < -1:  # Right-heavy
        if key > root.right.key:
            return left_rotate(root)  # Right-Right case
        else:
            root.right = right_rotate(root.right)  # Right-Left case
            return left_rotate(root)

    return root  # Return the (possibly updated) root

# Create an empty AVL tree
root = None

# Insert nodes into the AVL tree
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 90)
root = insert(root, 100)

# Find and print the maximum value in the AVL tree
print("Maximum value in the AVL tree:", find_max(root))