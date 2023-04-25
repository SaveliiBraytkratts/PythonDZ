def summ(a, b):
    if b == 0:
        return 1

    return a * summ(a, b - 1)

elevate = int(input("введите число:"))
multiplier = int(input("введите в какую степинь возвести:"))
print(summ(elevate, multiplier))