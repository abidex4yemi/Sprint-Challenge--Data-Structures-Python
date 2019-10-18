class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If value to insert is equal to root node
        if self.value == value:
            return False
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
                return True
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                return True

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)

        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        if not self.right:
            return self.value
        return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
