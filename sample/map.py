"""
Serverside,
Saves and loads maps.
Must be able to hold a 'history' to allow for calculations on moveables
"""
import time
import turtle
# from agent import Cleaner
LAYOUT = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 0, 0, 5, 0, 0, 0, 1],
          [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

len(LAYOUT[0])
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("House Sim")
wn.setup(700,700)

def load_room(layout):
    for y in range(len(layout)):
        for x in range(len(layout[y])):
            tile = layout[y][x]
            screen_x = (x*24)
            screen_y = (y*24)

            # define perminant obstacles
            if tile == 1:
                pen.goto(screen_x, screen_y)
                pen.color("white")
                pen.stamp()
                # add coordinates to objects list for collision
                objects.append((screen_x, screen_y))

            if tile == 5:
                pen.color("grey")
                pen.stamp()
                cleaned.append((screen_x, screen_y))

            if tile == 0:
                pen.color("black")
                pen.stamp()
                dirty.append((screen_x, screen_y))

#Creates the visual mapper object
class Mapper(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(-1)

class Layouts:

    def __init__(name, layout):
        """
        Creates a new map
        """
        self.name = name
        self.layout = layout

    def __repr__():
        """
        Room
        """
        return self.name




objects = []
cleaned = []
dirty = []

def loop():
    delay=1
    while True:
        wn.update()
        time.sleep(delay)


if __name__ == '__main__':
    # create map
    pen = Mapper()
    load_room(LAYOUT)
    # create agent
    # vacuum = Cleaner()
    loop()
