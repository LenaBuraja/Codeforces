

def Fibonachi(key: int):
    symbol: str = 's'
    name: str = symbol.upper()
    countEl: int = 1
    myList = [1, 1]
    for i in range(2, key + 1):
        if (myList[countEl - 1] + myList[countEl]) == i:
            myList.append(myList[countEl - 1] + myList[countEl])
            countEl += 1
            name += symbol.upper()
        else:
            name += symbol
    return name


def main():
    print("Введите число от 1 до 1000:")
    key: int = int(input())
    if 1 <= key <= 1000:
        print(Fibonachi(key))
    else:
        print("Введено неправильное число")
    return True

main()
