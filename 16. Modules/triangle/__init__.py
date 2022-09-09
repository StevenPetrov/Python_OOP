def print_triangle(nums):
    nums +=1
    for x in range(nums):
        for y in range(x):
            print(y+1, end= ' ')
        print()
    for x in range(nums-2,-1,-1):
        for y in range(x):
            print(y+1, end= ' ')
        print()