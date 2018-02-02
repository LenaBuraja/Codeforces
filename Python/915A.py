

def main():
    [n, k], a = map(int, input().split(' ')), list(map(int, input().split(' ')))
    r = list(map(lambda x: int(k/x), filter(lambda y: k%y==0, a)))
    print(min(r))
    return True

main()
