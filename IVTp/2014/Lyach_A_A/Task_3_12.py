# Задача 3, Вариант 12
# Напишите программу , которая выводит	имя	"Тициано Вечеллио",	и запрашивает его псевдоним.	
#Программа	должна	сцеплять две эти строки	и выводить полученную строку , разделяя	имя	и псевдоним	с помощью	тире.

# Лях А. А.
# 21.05.2016
name = "Тициано Вечеллио"
psname = "Тициан"
print(name, " - настоящее имя итальянского живописца.")
answer = input("\nВведите имя под которым прославился живописец: ")
while answer.find(psname) == -1 and answer.find("0") == -1:
    print(answer, "- неверный ответ.", name, "известен под другим именем.")
    answer = input("\nПопробуйте ещё раз (или введите \"0\" для выхода): ")
if answer.find(psname) != -1:
    print(answer, "- правильный ответ!")
print("\nЗавершение программы.")
input("\n\nНажмите Enter для выхода.")