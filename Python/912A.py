

def main():
    k, s = list(map(int, input().split(' '))), list(map(int, input().split(' ')))
    r: int = sum(map(lambda x, y: x*y, s, [2, 2, 3])) - sum(k)
    print(r)
    return True


main()