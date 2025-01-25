class AVLNode:
    def __init__(self, key):
        self.key = key  # Value of the node
        self.height = 1  # Height of the node
        self.left = None  # Left child
        self.right = None  # Right child


def find_sum(current):
    # Base case: if the node is None, return 0
    if current is None:
        return 0
    # Recursively calculate the sum of the current node, left subtree, and right subtree
    return current.key + find_sum(current.left) + find_sum(current.right)


def find_min(current):
    # If the tree is empty, return None
    if current is None:
        return None

    # Traverse to the leftmost node (smallest value in the tree)
    while current.left is not None:
        current = current.left

    return current.key  # Return the key of the leftmost node


def find_max(current):
    # If the tree is empty, return None
    if current is None:
        return None

    # Traverse to the rightmost node (largest value in the tree)
    while current.right is not None:
        current = current.right

    return current.key  # Return the key of the rightmost node


def get_height(node):
    # If the node is None, its height is 0
    if not node:
        return 0
    # Return the height of the node
    return node.height


def get_balance(node):
    # If the node is None, the balance factor is 0
    if not node:
        return 0
    # Calculate the balance factor: left subtree height - right subtree height
    return get_height(node.left) - get_height(node.right)


def left_rotate(z):
    # Perform a left rotation
    y = z.right  # Set y to the right child of z
    T2 = y.left  # Temporarily store the left subtree of y

    # Perform the rotation
    y.left = z
    z.right = T2

    # Update the heights of z and y
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y  # Return the new root after rotation


def right_rotate(y):
    # Perform a right rotation
    x = y.left  # Set x to the left child of y
    T3 = x.right  # Temporarily store the right subtree of x

    # Perform the rotation
    x.right = y
    y.left = T3

    # Update the heights of y and x
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x  # Return the new root after rotation


def insert(root, key):
    # If the tree is empty, create a new node
    if not root:
        return AVLNode(key)

    # Insert the key into the appropriate subtree
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
    if balance > 1:  # Left-heavy case
        if key < root.left.key:
            return right_rotate(root)  # Left-Left case
        else:
            root.left = left_rotate(root.left)  # Left-Right case
            return right_rotate(root)

    if balance < -1:  # Right-heavy case
        if key > root.right.key:
            return left_rotate(root)  # Right-Right case
        else:
            root.right = right_rotate(root.right)  # Right-Left case
            return left_rotate(root)

    return root  # Return the (possibly updated) root


# Create an empty AVL tree
root = None

# List of values to insert into the AVL tree
values = [50, 30, 70, 60, 90, 100]

# Insert each value from the list into the tree
for value in values:
    root = insert(root, value)

# Find and print the maximum value in the AVL tree
print("Maximum value in the AVL tree:", find_max(root))

# Find and print the minimum value in the AVL tree
print("Minimum value in the AVL tree:", find_min(root))

# Calculate and print the sum of all values in the AVL tree
print("Total amount of all values:", find_sum(root))