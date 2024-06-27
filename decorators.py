from __future__ import annotations
from abc import ABC, abstractmethod
from turtle import *
import parser


def draw(fun):
    def wrapper(self, state):
        result = fun(self, state)
        self.begin_fill()

        if state == "circle":
            self.circle(100)
            self.end_fill()

        elif state == "square":
            for i in range(4):
                self.forward(100)
                self.left(90)
            self.end_fill()

        return self if result is None else False

    return wrapper


class ATurtle(ABC):

    @abstractmethod
    def draw_square(self): pass

    @abstractmethod
    def draw_circle(self): pass


class DefaultTurtle(ATurtle, RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas=canvas)
        self.speed(10)
        self.fillcolor('white')

    def draw_square(self):
        for i in range(4):
            self.forward(100)
            self.left(90)

    def draw_circle(self):
        self.circle(100)


class ATurtleDecorator(ABC):
    def get_back(self, state): pass

    def add_width(self, state): pass

    def abate_width(self, state): pass

    def add_red(self, state): pass

    def remove_red(self, state): pass


class WidthDecorator(RawTurtle, ATurtleDecorator):
    def __init__(self, turtle: DefaultTurtle):
        super().__init__(canvas=turtle.screen)
        self.state = turtle
        self.pen(speed=turtle.speed())
        self.pen(pensize=turtle.width())
        self.pen(fillcolor=turtle.fillcolor())

    @draw
    def add_width(self, state):
        self.pen(pensize=(self.width()+1))

    @draw
    def abate_width(self, state):
        if self.width() == 1:
            return False
        self.pen(pensize=(self.width() - 1))


class RedColorDecorator(RawTurtle, ATurtleDecorator):
    def __init__(self, turtle: DefaultTurtle):
        super().__init__(canvas=turtle.screen)
        self.state = turtle
        self.pen(turtle.pen())

    @draw
    def add_red(self, state):
        colors = parser.red_parser(self.fillcolor())
        if colors is False:
            return False
        else:
            self.fillcolor(colors)

    @draw
    def abate_red(self, state):
        colors = parser.red_abate_parser(self.fillcolor())
        if colors is False:
            return False
        else:
            self.fillcolor(colors)


class BlueColorDecorator(RawTurtle, ATurtleDecorator):
    def __init__(self, turtle: DefaultTurtle):
        super().__init__(canvas=turtle.screen)
        self.state = turtle
        self.pen(turtle.pen())

    @draw
    def add_blue(self, state):
        colors = parser.blue_parser(self.fillcolor())
        if colors is False:
            return False
        else:
            self.fillcolor(colors)

    @draw
    def abate_blue(self, state):
        colors = parser.blue_abate_parser(self.fillcolor())
        if colors is False:
            return False
        else:
            self.fillcolor(colors)


class GreenColorDecorator(RawTurtle, ATurtleDecorator):
    def __init__(self, turtle: DefaultTurtle):
        super().__init__(canvas=turtle.screen)
        self.state = turtle
        self.pen(turtle.pen())

    @draw
    def add_green(self, state):
        colors = parser.green_parser(self.fillcolor())
        if colors is False:
            return False
        else:
            self.fillcolor(colors)

    @draw
    def abate_green(self, state):
        colors = parser.green_abate_parser(self.fillcolor())
        if colors is False:
            return False
        else:
            self.fillcolor(colors)
