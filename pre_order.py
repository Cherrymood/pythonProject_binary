def pre_order(self):
    elements = []

    elements.append(self.data)
    if self.left:
        elements += self.left.pre_order()
    if self.right:
        elements += self.right.pre_order()

    return elements