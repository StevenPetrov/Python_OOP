class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_num = start
    def __iter__(self):
        return self

    def __next__(self):
        value = self.current_num
        self.current_num += 1
        if value > self.end: raise StopIteration
        return value


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
