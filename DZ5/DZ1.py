def summ(a, b):
    number = a
    for i  in range(b - 1):
        number = number * a
    print(number)

elevate = int(input("введите число:"))
multiplier = int(input("введите в какую степинь возвести:"))
summ(elevate, multiplier)