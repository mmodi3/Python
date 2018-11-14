num = 27
oddDict = {"1": True, "3":True, "5":True, "7": True, "9":True}
def hasOdd(num):
    val = str(num)
    for i in val:
        if i in oddDict:
            return True
    return False

def f(num):
    while hasOdd(num):
        num += int(str(num)[::-1])
        print(num)
    print(num)

if __name__ == "__main__":
    print(f(num))


