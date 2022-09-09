from fib import fib_gen
while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split()
    num = int(command[2])
    command = input()
    command = command.split()
    locate = int(command[1])
    fib_gen(num,locate)

