import turtle
from turtle import *
from player import Player, PlayerBullets
from bots import Bots, BotBullets
from scoreboard import ScoreBoard
import keyboard
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Space Invaders")
screen.bgcolor("black")
screen.tracer(0, 0)  # TURN OFF THE ANIMATION

screen.register_shape("shipy.gif")
screen.register_shape("bot.gif")

player = Player()
player_bullets = PlayerBullets()
bots = Bots()
bots.bots_first_row()
bots.bots_second_row()
bots_bullets = BotBullets()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
game_is_on = True

while game_is_on:
	time.sleep(0.1)
	screen.update()
	scoreboard.show_score()

	# if space is pressed, then create bullets
	if keyboard.is_pressed("space"):
		current_xcor = player.xcor()
		current_ycor = player.ycor()
		player_bullets.create_bullets(current_xcor, current_ycor)

	# move player bullets forward
	player_bullets.move_player_bullets()

	# get random bot and make it attack
	random_bot = random.choice(bots.all_bots)
	random_bot_xcor = random_bot.xcor()
	random_bot_ycor = random_bot.ycor() - 10
	bots_bullets.move_bot_bullets()

	# check if player bullets hit any bots
	# if there is a hit, make bot disappear
	for bullet in player_bullets.all_bullets:
		for bot in bots.all_bots:
			if bullet.distance(bot) < 20:
				# bot.goto(100000000000, 100000000000)
				# bullet.goto(100000000000, 100000000000)
				bot.reset()
				bot.hideturtle()
				bots.all_bots.remove(bot)
				scoreboard.clear()
				scoreboard.score_up()
				if scoreboard.score == 15:
					game_is_on = False
					scoreboard.clear()
					scoreboard.game_over()


	# check if bot bullets hit the player
	# if there is a hit, player loses the game
	# for bot_bullet in bots_bullets.all_bullets:
	# 	if bot_bullet.distance(player) < 15:
	# 		turtle.write("Game is Over", align="center", font=("Courier", 30, "normal"))
	# 		game_is_on = False
	# 		scoreboard.clear()
	# 		scoreboard.game_over()

	# if bots pass the player, game is over
	for bot in bots.all_bots:
		if bot.ycor() < -260:
			game_is_on = False
			scoreboard.clear()
			scoreboard.game_over()


	bots.move_bots()
screen.mainloop()
