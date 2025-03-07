
from tkinter import *
from decorators import DefaultTurtle, WidthDecorator, RedColorDecorator, BlueColorDecorator, GreenColorDecorator
from tkinter.messagebox import showinfo


def check_state(func):
    def wrapper(self):
        if self.get_state() is None:
            showinfo(title='No city', message='фигура не выбрана')
        else:
            self._canvas.delete("all")
            func(self)
    return wrapper


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.__title = "tkinter with turtle "
        self.geometry('1300x750')
        self.resizable(False, False)
        self.frame_for_buttons = Frame(borderwidth=0, height=750, width=250, background="red")
        self.frame_for_buttons.place(x=0, y=0)

        self._canvas = Canvas(width=1200, height=750, background="blue")
        self._canvas.place(x=250)

        self.__create_square_button = Button(self.frame_for_buttons, text="нарисовать квадрат", command=self.__create_square)
        self.__create_square_button.place(relx=0.01, rely=0.01)

        self.__create_circle_button = Button(self.frame_for_buttons, text="нарисовать круг", command=self.__create_circle)
        self.__create_circle_button.place(relx=0.01, rely=0.06)

        self.__width_label = Label(self.frame_for_buttons, background="red", text="толщина границы")
        self.__width_label.place(relx=0.01, rely=0.16)

        self.__add_width_pencil_button = Button(self.frame_for_buttons, text="+", command=self.__add_width)
        self.__add_width_pencil_button.place(relx=0.51, rely=0.16)

        self.__abate_width_pencil_button = Button(self.frame_for_buttons, text="-", command=self.__abate_width)
        self.__abate_width_pencil_button.place(relx=0.66, rely=0.16)

        self.__color_label = Label(self.frame_for_buttons, background="red", text="добавить цвет")
        self.__color_label.place(relx=0.01, rely=0.21)

        self.__red_label = Label(self.frame_for_buttons, background="red", text="красный")
        self.__red_label.place(relx=0.01, rely=0.26)

        self.__add_red_button = Button(self.frame_for_buttons, text="+", command=self.__add_red)
        self.__add_red_button.place(relx=0.51, rely=0.26)

        self.__abate_color_button = Button(self.frame_for_buttons, text="-", command=self.__abate_red)
        self.__abate_color_button.place(relx=0.66, rely=0.26)

        self.__abate_blue_button = Button(self.frame_for_buttons, text="-", command=self.__abate_blue)
        self.__abate_blue_button.place(relx=0.66, rely=0.31)

        self.__abate_green_button = Button(self.frame_for_buttons, text="-", command=self.__abate_green)
        self.__abate_green_button.place(relx=0.66, rely=0.36)

        self.__blue_label = Label(self.frame_for_buttons, background="red", text="синий")
        self.__blue_label.place(relx=0.01, rely=0.31)

        self.__add_blue_button = Button(self.frame_for_buttons, text="+", command=self.__add_blue)
        self.__add_blue_button.place(relx=0.51, rely=0.31)

        self.__green_label = Label(self.frame_for_buttons, background="red", text="зеленый")
        self.__green_label.place(relx=0.01, rely=0.36)

        self.__add_green_button = Button(self.frame_for_buttons, text="+", command=self.__add_green)
        self.__add_green_button.place(relx=0.51, rely=0.36)

        self.clean_button = Button(self.frame_for_buttons, text="очистить", command=self.__clean)
        self.clean_button.place(relx=0.36, rely=0.51)

        self.def_turtle = DefaultTurtle(self._canvas)

        self.__state = None

    def get_state(self):
        return self.__state

    @check_state
    def __add_width(self):
        self.def_turtle = WidthDecorator(self.def_turtle).add_width(self.__state)

    @check_state
    def __abate_width(self):
        result = WidthDecorator(self.def_turtle).abate_width(self.__state)
        if result is False:
            showinfo(title='No city', message='куда тоньше, а?')
        else:
            self.def_turtle = result

    @check_state
    def __add_red(self):
        result = RedColorDecorator(self.def_turtle).add_color(self.__state)
        if result is False:
            showinfo(title='No city', message='краснее не бывает')
        else:
            self.def_turtle = result

    @check_state
    def __abate_red(self):
        result = RedColorDecorator(self.def_turtle).abate_color(self.__state)
        if result is False:
            showinfo(title='No city', message='меньше не бывает')
        else:
            self.def_turtle = result

    @check_state
    def __abate_blue(self):
        result = BlueColorDecorator(self.def_turtle).abate_color(self.__state)
        if result is False:
            showinfo(title='No city', message='меньше не бывает')
        else:
            self.def_turtle = result

    @check_state
    def __abate_green(self):
        result = GreenColorDecorator(self.def_turtle).abate_color(self.__state)
        if result is False:
            showinfo(title='No city', message='меньше не бывает')
        else:
            self.def_turtle = result

    @check_state
    def __add_blue(self):
        result = BlueColorDecorator(self.def_turtle).add_color(self.__state)
        if result is False:
            showinfo(title='No city', message='голубее не бывает')
        else:
            self.def_turtle = result

    @check_state
    def __add_green(self):
        result = GreenColorDecorator(self.def_turtle).add_color(self.__state)
        if result is False:
            showinfo(title='No city', message='зеленей не будет')
        else:
            self.def_turtle = result

    def __clean(self):
        self._canvas.delete("all")
        self.__state = None

    def __create_square(self):
        self.__state = "square"
        self._canvas.delete("all")
        self.def_turtle = DefaultTurtle(self._canvas)
        self.def_turtle.draw_square()

    def __create_circle(self):
        self.__state = "circle"
        self._canvas.delete("all")
        self.def_turtle = DefaultTurtle(self._canvas)
        self.def_turtle.draw_circle()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    window = Window()
    window.run()





