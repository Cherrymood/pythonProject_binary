def add_child(self, data):
    if data == self.data:
        return
    if data < self.data:
        if self.left:
            self.left.add_child(data)
        else:
            self.left = BinarySearchTreeNode(data)
    else:
        if self.right:
            self.right.add_child(data)
        else:
            self.right = BinarySearchTreeNode(data)