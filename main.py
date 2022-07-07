import turtle
from turtle import *
from player import Player, PlayerBullets
from bots import Bots, BotBullets
from scoreboard import ScoreBoard
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
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
game_is_on = True

while game_is_on:
	time.sleep(0.1)
	screen.update()
	scoreboard.show_score()

	current_xcor = player.xcor()
	current_ycor = player.ycor()
	screen.onkey(lambda: player_bullets.create_bullets(current_xcor, current_ycor), "space")

	# move player bullets forward
	player_bullets.move_player_bullets()

	# get random bot coordination for bullets
	random_bot = random.choice(bots.all_bots)
	random_bot_xcor = random_bot.xcor()
	random_bot_ycor = random_bot.ycor() - 10

	# this 3 line of code below is for appropriate amount of bullets that bots shoot
	# otherwise, since bullets stack up in bots_bullets.all_bullets list,
	# the last 2 3 bot shoots too fast this gives player no chance to hit it directly
	# this below code keeps the track of len of bots and allows bots to shoot bullets equal to the bot count
	# this gives player an equal chance to play the game
	bot_num = len(bots.all_bots)
	if len(bots_bullets.all_bullets) < bot_num:
		bots_bullets.create_bullets(random_bot_xcor, random_bot_ycor)

	bots_bullets.move_bot_bullets()

	# if bot bullets go beyond the game screen, they disappear, and they are removed from all_bullets list
	for bot_bullet in bots_bullets.all_bullets:
		if bot_bullet.ycor() < -260:
			bots_bullets.all_bullets.remove(bot_bullet)
			bot_bullet.hideturtle()

	# check if player bullets hit any bots
	# if there is a hit, make bot disappear
	for bullet in player_bullets.all_bullets:
		for bot in bots.all_bots:
			if bullet.distance(bot) < 20:
				bot.reset()
				bot.hideturtle()
				bots.all_bots.remove(bot)
				scoreboard.clear()
				scoreboard.score_up()
				if scoreboard.score == 15:
					game_is_on = False
					scoreboard.clear()
					scoreboard.show_score()

	# check if bot bullets hit the player
	# if there is a hit, player loses the game
	for bot_bullet in bots_bullets.all_bullets:
		if bot_bullet.distance(player) < 15:
			turtle.write("Game is Over", align="center", font=("Courier", 30, "normal"))
			game_is_on = False
			scoreboard.clear()
			scoreboard.show_score()

	# if bots pass the player, game is over
	for bot in bots.all_bots:
		if bot.ycor() < -260:
			game_is_on = False
			scoreboard.clear()
			scoreboard.show_score()

	bots.move_bots()
screen.mainloop()
