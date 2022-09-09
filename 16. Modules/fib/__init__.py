def fib_gen(number, looking_number):
    a, b = 0, 1
    l = [0]
    for _ in range(number-1):
        l.append(b)
        a, b = b, a + b
    print(*l)
    if looking_number in l:
        looking_number_index = l.index(looking_number)
        print(f'The number {looking_number} is at index {looking_number_index}')
    else:
        print(f'The number {looking_number} is not in the sequence')

