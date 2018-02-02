

import math


def main():
    n, a = int(input()), list(map(int, input().split(' ')))
    r = max(list(filter(lambda y: int(math.sqrt(y))**2 != y, a)))
    print(r)
    return True


main()
