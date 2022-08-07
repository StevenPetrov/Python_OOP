class vowels:
    vowels = ['a','e','o','u','i','y']
    def __init__(self, word):
        self.word = word
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.word):
            chr = self.word[self.index]
            self.index += 1
            if chr.lower() in self.vowels:
                return chr
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
