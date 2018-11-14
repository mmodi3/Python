def closestValue(values, target):
    left = 0
    right = len(values)-1
    while left <= right:
        guess = (left+right)//2
        if values[guess] == target:
            return target
        elif values[guess] > target:
            right = guess - 1
        else:
            left = guess + 1
    if values[left] - target < target - values[right]:
        return values[left]
    else:
        return values[right]


if __name__ == '__main__':
    lst = []
    nums = ['1','2','3','4','5','6','7','8','9','0']
    while True:
        temp = input("Give sorted array of values from which to find closest value, type END to finish passing values: ")
        if temp == 'end' or 'END':
            break
        lst.append(int(temp))
    target = int(input("Give target value: "))
    print(closestValue(lst, target))