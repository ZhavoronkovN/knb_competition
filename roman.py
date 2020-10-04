import random as r
# Памятка по питону :
# random.seed(int) 
# random.randint(from,to)
# Больше ничего знать не нужно

def whoBeats(what): # возвращает фигуру, которая побеждает заданую 
	return (what+2)%3

def getanswer(lastOponentsAnswer): # -1 если новая игра, 0 -- камень, 1 -- ножницы, 2 -- бумага
	if lastOponentsAnswer == -1:
		# новая игра, можем почистить, если что то надо
		return 0 # или вернуть особую фигуру
	# тут ваш алгоритм
	return r.randint(0,2) # возвращаем 0, 1, 2 (см. выше)