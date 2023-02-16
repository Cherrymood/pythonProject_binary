class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

    def in_order_traversal(self):
        elements = []

        #elements.append(self.data)
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        #elements.append(self.data)

        return elements

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

    def search_max(self):
        if self.right:
            return self.right.search_max()

        return self.data

    def search_min(self):
        if self.left:
            return self.left.search_min()

        return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def post_order(self):
        elements = []

        if self.left:
            elements += self.left.post_order()
        if self.right:
            elements += self.right.post_order()
        elements.append(self.data)

        return elements

    def pre_order(self):
        elements = []

        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order()
        if self.right:
            elements += self.right.pre_order()

        return elements
1
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for index in range(1, len(elements)):
        root.add_child(elements[index])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(6))
    print(numbers_tree.search(9))
    print(numbers_tree.search_max())
    print(numbers_tree.search_min())
    print(numbers_tree.calculate_sum())
    print(numbers_tree.post_order())
    print(numbers_tree.pre_order())
