def search_min(self):
    min_val = self.data

    if self.left:
        return self.left.search_min()
    else:
        return min_val