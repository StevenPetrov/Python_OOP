def reverse_text(text):
    index = -1
    while abs(index) < len(text) + 1:
        yield text[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
