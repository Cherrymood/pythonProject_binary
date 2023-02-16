def in_order_traversal(self):
    elements = []

    # elements.append(self.data)
    if self.left:
        elements += self.left.in_order_traversal()

    elements.append(self.data)

    if self.right:
        elements += self.right.in_order_traversal()

    # elements.append(self.data)

    return elements