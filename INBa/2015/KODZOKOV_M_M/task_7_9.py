#Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы 
#большее количество баллов за меньшее количество попыток.

# Кодзоков М.М., 26.05.2016
import random
pigs=("Ниф-ниф","Наф-наф","Нуф-нуф")
choice=random.choice(pigs)
pg=input("Угадайте одного из трех поросят: ")
points=1000
while pg != choice:
	pg=input("Не угадали. Попробуйте еще: ")
	points-=100
	if points <=0:
		break
if points <=0:
	print("К сожалению, у вас 0 очков, и вы проиграли. А это был поросенок по имени",choice)
else: print("Вы угадали. Это",choice,"! У вас",points,"очков!")
input("Нажмите ENTER для продолжения")
