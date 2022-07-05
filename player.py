from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


# PLAYER CONFIGURATIONS
class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.shape('shipy.gif')
		self.color("white")
		self.penup()
		self.setheading(90)
		self.goto(0, -230)

	def go_right(self):
		new_x = self.xcor() + 20
		self.goto(new_x, self.ycor())

	def go_left(self):
		new_x = self.xcor() - 20
		self.goto(new_x, self.ycor())


# PLAYER BULLET CONFIGURATIONS
class PlayerBullets(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.move_distance = 20
		self.all_bullets = []
		self.bullet_created = False

	def create_bullets(self, x_position, y_position):
		new_bullet = Turtle()
		new_bullet.shape("square")
		new_bullet.color("white")
		new_bullet.penup()
		new_bullet.setheading(90)
		new_bullet.shapesize(stretch_len=0.60, stretch_wid=0.20)
		new_bullet.goto(x_position, y_position+20)
		self.all_bullets.append(new_bullet)
		self.bullet_created = True

	def move_player_bullets(self):
		for bullet in self.all_bullets:
			bullet.forward(self.move_distance)