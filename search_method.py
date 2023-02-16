def search(self, val):
    if self.data == val:
        return True

    if val < self.data:
        if self.left:
            return self.left.search(val)
        else:
            return False

    if val > self.data:
        if self.right:
            return self.right.search(val)
        else:
            return False