class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < data.self:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements1 = []

        if self.left:
            elements1 += self.left.in_order_traversal()
        if self.right:
            elements1 += self.right.in_order_traversal()
        elements1.append(self.data)
        return elements1

    def pre_order_traversal(self):
            elements2 = []

            elements2.append(self.data)
            if self.left:
                elements2 += self.left.in_order_traversal()
            if self.right:
                elements2 += self.right.in_order_traversal()
            elements2.append(self.data)

            return elements2

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for index in range(1, len(elements)):
        root.add_child(elements[index])
        return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())



