class reverse_iter:
    def __init__(self, values):
        self.index = -1
        self.values = list(values)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = self.values[self.index]
            self.index -= 1
            return value
        except IndexError:
            raise StopIteration




reversed_list = reverse_iter({1, 2, 3, 4})
for item in reversed_list:
    print(item)
