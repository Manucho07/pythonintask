#Задача 5. Вариант 26.
#Напишите программу, которая бы при запуске случайным образом отображала имена двух братьев, легендарных основателей Рима.+

#Sosnovy M.S.
#16.03.2016
import random
A =int(random.randint(0,1))
one = " Ромул "
two = ' Рем '
if A == 0:
    print('Великие основатели Рима' + one + "и" + two)
else:
    print('Великие Основат5ли Рима' + two + "и" + one)
input("\n\nНажмите Enter для выхода.")
