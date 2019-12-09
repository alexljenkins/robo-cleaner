"""
The Vacuum Cleaner 1337
"""

class Cleaner(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.node = "entrance"
        self.shape("square")
        self.color("blue")
        # self.penup()
        self.speed(6)
        self.goto((24*1),(24*-1))

    """
    Note to self:
        will also need to add turning in here eventually.
    """
    def up(self):
        # moves the agent up
        self.goto(self.xcor(), self.ycor() + 24)

    def down(self):
        # moves the agent up
        self.goto(self.xcor(), self.ycor() - 24)

    def left(self):
        # moves the agent up
        self.goto(self.xcor() - 24, self.ycor())

    def right(self):
        # moves the agent up
        self.goto(self.xcor() + 24, self.ycor())
