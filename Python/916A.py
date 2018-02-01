

def main():
    minute: int = int(input())
    count: int = 0
    myTime: str = input()
    hh: int = int(myTime[0:myTime.find(' '):1])
    mm: int = int(myTime[myTime.find(' ')+1:len(myTime):1])
    if (myTime.find('7') == -1):
        while ((str(hh) + str(mm)).find('7') == -1):
            hh -= 0 if ((mm - minute) >= 0) else 1
            hh += 0 if (hh >= 0) else 24
            mm += - minute if((mm - minute) >= 0) else 60 - minute
            count += 1
    print("Переставить будильник ", count)
    return True

main()
