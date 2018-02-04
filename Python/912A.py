

def main():
    k, s = list(map(int, input().split(' '))), list(map(int, input().split(' ')))
    t: list = [s[0] * 2 + s[1], s[1] + s[2] * 3]
    r: int = sum(map(lambda x, y: y-x if (y-x) > 0 else 0, k, t))
    print(r)
    return True


main()
