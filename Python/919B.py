

def main():
    s = input()
    c = sum(list(map(int, ''.join(s))))
    f = s + str(0 if (c == 10) else 10 - c)
    print(f)
    return True


main()
