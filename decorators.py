from __future__ import annotations
from abc import ABC, abstractmethod
from turtle import *


def draw(fun):
    def wrapper(self, state):
        if fun(self, state) is False:
            return False
        else:
            if state == "circle":
                self.circle(100)
            else:
                for i in range(4):
                    self.forward(100)
                    self.left(90)
            return self
    return wrapper


def end_fill(fun):
    def wrapper(self, state):
        fun(self, state)
        self.end_fill()
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
        self.pen(pensize=(turtle.width()))
        self.pen(speed=turtle.speed())

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
        self.pen(pensize=(turtle.width()))
        self.pen(speed=turtle.speed())

    @end_fill
    @draw
    def add_red(self, state):
        self.fillcolor('#A60000')
        self.begin_fill()

    @draw
    def abate_red(self, state):
        self.pen(fillcolor=(self.state.fillcolor()))


class BlueColorDecorator(RawTurtle, ATurtleDecorator):
    def __init__(self, turtle: DefaultTurtle):
        super().__init__(canvas=turtle.screen)
        self.state = turtle
        self.pen(pensize=(turtle.width()))
        self.pen(speed=turtle.speed())

    @end_fill
    @draw
    def add_red(self, state):
        self.fillcolor('#5490f0')
        self.begin_fill()

    @draw
    def abate_red(self, state):
        self.pen(fillcolor=(self.state.fillcolor()))


class GreenColorDecorator(RawTurtle, ATurtleDecorator):
    def __init__(self, turtle: DefaultTurtle):
        super().__init__(canvas=turtle.screen)
        self.state = turtle
        self.pen(pensize=(turtle.width()))
        self.pen(speed=turtle.speed())

    @end_fill
    @draw
    def add_red(self, state):
        self.fillcolor('#227307')
        self.begin_fill()

    @draw
    def abate_red(self, state):
        self.pen(fillcolor=(self.state.fillcolor()))