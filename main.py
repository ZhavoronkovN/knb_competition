import nikita
import roman
import petro
import oleh

def whoBeats(what): # возвращает фигуру, которая побеждает заданую 
	return (what+2)%3

TRIES = 1000 * 1000

users = set(["nikita","roman","oleh","petro"])
scoreboard = dict.fromkeys(users,0)
funcs = {'nikita': nikita.getanswer, 'roman': roman.getanswer, 'oleh': oleh.getanswer, 'petro': petro.getanswer}

for player1 in users:
	for player2 in (users - set(player1)):
		player1_answer = -1
		player2_answer = -1
		for i in range(TRIES):
			tempPlayer1_answer = player1_answer
			player1_answer = funcs[player1](player2_answer)
			player2_answer = funcs[player2](tempPlayer1_answer)
			if player1_answer == player2_answer:
				scoreboard[player1] += 1
				scoreboard[player2] += 1
			elif whoBeats(player1_answer) == player2_answer:
				scoreboard[player2] += 2
			elif whoBeats(player2_answer) == player1_answer:
				scoreboard[player1] += 2
			else:
				raise Exception("Smth went wrong! {0} answer : {1}; {2} answer : {3}".format(player1, player1_answer, player2, player2_answer))

print("Results")
for result in sorted(scoreboard.items(), key = lambda x: x[1], reverse=True):
	print("{0} : {1}".format(result[0], result[1]))
	print("/\\" * (result[1] // (TRIES//5)))