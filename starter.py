# -*-coding:Utf-8 -*

from game import Game


width = ""
height = ""
start = "no"
while start.lower() == "no":
	while type(width) is not int or int(width) > 100 or int(width) < 5:
		width = input('How wide do you want your maze to be? Choose a number between 5 and 100: \n > ')
		width = int(width)

	while type(height) is not int or int(height) > 100 or int(height) < 5:
		height = input('And what about your maze\'s height? Once again, something between 5 and 100: \n > ')
		height = int(height)

	game = Game(height, width)

	print(game)

	start = input('That\'s the maze game you\'re going to play. You good with that? Say yes or no. \n >')

game.initiate()
print(game)
print('Use your arrows to control your robot. \n Use w to go up \n Use s to go down \n Use a to go left \n une d to go right.')

while not game.over:
	move = input('>')
	game.analyse(move)
	print(game)



