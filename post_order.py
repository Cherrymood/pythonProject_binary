def post_order(self):
    elements = []

    if self.left:
        elements += self.left.post_order()
    if self.right:
        elements += self.right.post_order()
    elements.append(self.data)

    return elements