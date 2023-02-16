def search_max(self):
    val = self.data

    if self.right:
        return self.right.search_max()
    else:
        return val