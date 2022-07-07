from turtle import Turtle


# BOT CONFIGURATIONS
class Bots(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.move_distance = 2
        self.all_bots = []

    def bots_first_row(self):
        x = -300
        y = 250
        for i in range(7):
            bot = Turtle()
            bot.shape("bot.gif")
            bot.penup()
            bot.setheading(270)
            bot.goto(x, y)
            x += 100
            self.all_bots.append(bot)

    def bots_second_row(self):
        x = -350
        y = 180
        for i in range(8):
            bot = Turtle()
            bot.shape("bot.gif")
            bot.penup()
            bot.setheading(270)
            bot.goto(x, y)
            x += 100
            self.all_bots.append(bot)

    def move_bots(self):
        for bot in self.all_bots:
            bot.forward(self.move_distance)


# BOT BULLET CONFIGURATIONS
class BotBullets(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.move_distance = 20
        self.all_bullets = []

    def create_bullets(self, x_position, y_position):
        new_bullet = Turtle()
        new_bullet.shape("square")
        new_bullet.color("red")
        new_bullet.penup()
        new_bullet.setheading(270)
        new_bullet.shapesize(stretch_len=0.60, stretch_wid=0.20)
        new_bullet.goto(x_position, y_position + 20)
        self.all_bullets.append(new_bullet)

    def move_bot_bullets(self):
        for bullet in self.all_bullets:
            bullet.forward(self.move_distance)
