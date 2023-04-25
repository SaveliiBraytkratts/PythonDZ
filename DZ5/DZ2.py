def summ(a, b):
    if a == 0:
        return b
    else:
        return summ(a - 1, b + 1)

addend1 = int(input("введите число:"))
addend2 = int(input("введите в какую степинь возвести:"))
print(summ(addend1, addend2))