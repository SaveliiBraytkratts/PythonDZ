a = int(input("введите трёхзначное число:"))
b = a % 10
c = (a % 100) // 10
d = a // 100
summa = b + c + d 
print(summa)