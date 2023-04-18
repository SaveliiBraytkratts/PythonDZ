k = int(input('Видите кол-во элементов в строке: '))
m_list = []
number = 0
for i in range(k):
    r = int(input('Видите элемент : '))
    m_list.append(r)
print(m_list)
x = int(input('Видите элемент x: '))
for j in range(k):
    if m_list[j] == x:
        number += 1
print(number)
