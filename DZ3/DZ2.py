k = int(input('Видите кол-во элементов в строке: '))
m_list = []
for i in range(k):
    r = int(input('Видите элемент : '))
    m_list.append(r)
print(m_list)
x = int(input('Видите элемент x: '))
min = (x - m_list[0])
index = 0
for i in range(1, k):
    count = abs(x - m_list[i])
    if count < min:
        min = count
        index = i
print(f'Число {m_list[index]} в списке A наиболее близко по величине к числу {x}, их разница составляет {abs(x - m_list[index])}')