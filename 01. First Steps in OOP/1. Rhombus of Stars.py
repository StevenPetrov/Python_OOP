def building_stars(i, n):
    spaces = n - 1 - i
    stars = i + 1
    return ' ' * spaces + "* " * stars


def print_rhombus(n):
    for i in range(0, n, 1):
        print(building_stars(i, n))
    for i in range(n - 2, -1, -1):
        print(building_stars(i, n))


print_rhombus(1)
