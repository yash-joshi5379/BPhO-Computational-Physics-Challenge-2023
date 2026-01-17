import pandas as pd
import matplotlib.pyplot as plt
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
import math
import numpy as np
from backend_kivyagg import FigureCanvasKivyAgg as FigureCanvas
import main as m


def position(theta_func, a, eps):
    r_func = a * (1 - eps ** 2) / (1 - eps * np.cos(theta_func))
    x_func = r_func * np.cos(theta_func)
    y_func = r_func * np.sin(theta_func)

    return r_func, x_func, y_func


def loop(i, speed, file):
    data = {}
    for j in range(1, 10):
        theta_func = (i * speed * np.pi) / (file["P"][j] * 180)
        e_temp = file["Epsilon"][j]
        r_func, x_func, y_func = position(theta_func, file["a"][j], e_temp)

        data[j] = {
            'x': [x_func],
            'y': [y_func],
            'colour': file["Colour"][j]
        }
    return data


class TaskSixScreen(RelativeLayout):

    def __init__(self, **kwargs):
        super(TaskSixScreen, self).__init__(**kwargs)
        self.ax = None
        self.fig = None
        self.event = None
        self.width, self.height = Window.system_size
        self.counter = 0
        self.selected_buttons = []
        self.file_planets = pd.read_excel("planets.xlsx")
        self.orientation = 'horizontal'
        self.create_screen()

    def create_screen(self):

        plt.style.use("default")

        title_text = "Task 6: Creating Spirographs"
        title = Label(text=title_text, font_size=60, padding=(10, 10), halign="center", valign='center')
        title.pos = (0, 4 * self.height / 5)
        self.add_widget(title)

        label_text = """Please select two planets from either the inner 4 planets or the 
outer 5 planets to create your spirograph with."""
        label = Label(text=label_text, font_size=40, padding=(10, 10), halign="center", valign="center")
        label.pos = (0, 7*self.height / 12)
        self.add_widget(label)

        inner_text = "Inner Planets"
        label_inner = Label(text=inner_text, font_size=50, padding=(10, 10), halign="center", valign="center")
        label_inner.pos = (-self.width/2, self.height/3)
        self.add_widget(label_inner)

        outer_text = "Outer Planets"
        label_outer = Label(text=outer_text, font_size=50, padding=(10, 10), halign="center", valign="center")
        label_outer.pos = (self.width/2, self.height/3)
        self.add_widget(label_outer)

        button1 = Button(text="Add Mercury", on_release=self.add_mercury, size_hint=(1/2, 1/8))
        button1.pos = (0, 8*self.height/8)
        self.add_widget(button1)

        button2 = Button(text="Add Venus", on_release=self.add_venus, size_hint=(1/2, 1/8))
        button2.pos = (0, 6*self.height/8)
        self.add_widget(button2)

        button3 = Button(text="Add Earth", on_release=self.add_earth, size_hint=(1/2, 1/8))
        button3.pos = (0, 4*self.height/8)
        self.add_widget(button3)

        button4 = Button(text="Add Mars", on_release=self.add_mars, size_hint=(1/2, 1/8))
        button4.pos = (0, 2*self.height/8)
        self.add_widget(button4)

        button5 = Button(text="Add Jupiter", on_release=self.add_jupiter, size_hint=(1/2, 1/8))
        button5.pos = (self.width, 8*self.height/8)
        self.add_widget(button5)

        button6 = Button(text="Add Saturn", on_release=self.add_saturn, size_hint=(1/2, 1/8))
        button6.pos = (self.width, 6*self.height/8)
        self.add_widget(button6)

        button7 = Button(text="Add Uranus", on_release=self.add_uranus, size_hint=(1/2, 1/8))
        button7.pos = (self.width, 4*self.height/8)
        self.add_widget(button7)

        button8 = Button(text="Add Neptune", on_release=self.add_neptune, size_hint=(1/2, 1/8))
        button8.pos = (self.width, 2*self.height/8)
        self.add_widget(button8)

        button9 = Button(text="Add Pluto", on_release=self.add_pluto, size_hint=(1/2, 1/8))
        button9.pos = (self.width, 0)
        self.add_widget(button9)

        home_button = Button(text='Go back', size_hint=(71/144, 1/9))
        home_button.bind(on_release=self.home_screen)
        home_button.pos = (0, 0)
        self.add_widget(home_button)

    def add_mercury(self, button):
        if 1 in self.selected_buttons:
            button.background_color = (1, 1, 1, 1)
            self.selected_buttons.remove(1)
        else:
            if len(self.selected_buttons) < 2:
                button.background_color = (0, 1, 0, 1)
                self.selected_buttons.append(1)

        if len(self.selected_buttons) == 2:
            self.create_spirograph()

    def add_venus(self, button):
        if 2 in self.selected_buttons:
            button.background_color = (1, 1, 1, 1)
            self.selected_buttons.remove(2)
        else:
            if len(self.selected_buttons) < 2:
                button.background_color = (0, 1, 0, 1)
                self.selected_buttons.append(2)

        if len(self.selected_buttons) == 2:
            self.create_spirograph()

    def add_earth(self, button):
        if 3 in self.selected_buttons:
            button.background_color = (1, 1, 1, 1)
            self.selected_buttons.remove(3)
        else:
            if len(self.selected_buttons) < 2:
                button.background_color = (0, 1, 0, 1)
                self.selected_buttons.append(3)

        if len(self.selected_buttons) == 2:
            self.create_spirograph()

    def add_mars(self, button):
        if 4 in self.selected_buttons:
            button.background_color = (1, 1, 1, 1)
            self.selected_buttons.remove(4)
        else:
            if len(self.selected_buttons) < 2:
                button.background_color = (0, 1, 0, 1)
                self.selected_buttons.append(4)

        if len(self.selected_buttons) == 2:
            self.create_spirograph()

    def add_jupiter(self, button):
        if 5 in self.selected_buttons:
            button.background_color = (1, 1, 1, 1)
            self.selected_buttons.remove(5)
        else:
            if len(self.selected_buttons) < 2:
                button.background_color = (0, 1, 0, 1)
                self.selected_buttons.append(5)

        if len(self.selected_buttons) == 2:
            self.create_spirograph()

    def add_saturn(self, button):
        if 6 in self.selected_buttons:
            button.background_color = (1, 1, 1, 1)
            self.selected_buttons.remove(6)
        else:
            if len(self.selected_buttons) < 2:
                button.background_color = (0, 1, 0, 1)
                self.selected_buttons.append(6)

        if len(self.selected_buttons) == 2:
            self.create_spirograph()

    def add_uranus(self, button):
        if 7 in self.selected_buttons:
            button.background_color = (1, 1, 1, 1)
            self.selected_buttons.remove(7)
        else:
            if len(self.selected_buttons) < 2:
                button.background_color = (0, 1, 0, 1)
                self.selected_buttons.append(7)

        if len(self.selected_buttons) == 2:
            self.create_spirograph()

    def add_neptune(self, button):
        if 8 in self.selected_buttons:
            button.background_color = (1, 1, 1, 1)
            self.selected_buttons.remove(8)
        else:
            if len(self.selected_buttons) < 2:
                button.background_color = (0, 1, 0, 1)
                self.selected_buttons.append(8)

        if len(self.selected_buttons) == 2:
            self.create_spirograph()

    def add_pluto(self, button):
        if 9 in self.selected_buttons:
            button.background_color = (1, 1, 1, 1)
            self.selected_buttons.remove(9)
        else:
            if len(self.selected_buttons) < 2:
                button.background_color = (0, 1, 0, 1)
                self.selected_buttons.append(9)

        if len(self.selected_buttons) == 2:
            self.create_spirograph()

    def create_spirograph(self):

        self.clear_widgets()
        self.selected_buttons = sorted(self.selected_buttons)

        num1 = self.selected_buttons[0]
        num2 = self.selected_buttons[1]

        if num1 in [1, 2] and num2 in [1, 2]:
            anim_speed = 4
        elif num1 in [1, 3] and num2 in [1, 3]:
            anim_speed = 5
        elif num1 in [1, 4] and num2 in [1, 4]:
            anim_speed = 6
        elif num1 in [2, 3] and num2 in [2, 3]:
            anim_speed = 7
        elif num1 in [2, 4] and num2 in [2, 4]:
            anim_speed = 10
        elif num1 in [3, 4] and num2 in [3, 4]:
            anim_speed = 1
        elif num1 in [5, 6] and num2 in [5, 6]:
            anim_speed = 200
        elif num1 in [5, 7] and num2 in [5, 7]:
            anim_speed = 400
        elif num1 in [5, 8] and num2 in [5, 8]:
            anim_speed = 600
        elif num1 in [5, 9] and num2 in [5, 9]:
            anim_speed = 800
        elif num1 in [6, 7] and num2 in [6, 7]:
            anim_speed = 700
        elif num1 in [6, 8] and num2 in [6, 8]:
            anim_speed = 900
        elif num1 in [6, 9] and num2 in [6, 9]:
            anim_speed = 1100
        elif num1 in [7, 8] and num2 in [7, 8]:
            anim_speed = 900
        elif num1 in [7, 9] and num2 in [7, 9]:
            anim_speed = 1200
        else:
            anim_speed = 1500

        def animate(i):

            years = round(1000 * self.counter * anim_speed / 360) / 1000

            data = loop(self.counter, anim_speed, self.file_planets)

            planet1.set_data(data[num1]['x'], data[num1]['y'])
            planet1.set_color(data[num1]['colour'])

            planet2.set_data(data[num2]['x'], data[num2]['y'])
            planet2.set_color(data[num2]['colour'])

            point1 = [data[num1]['x'], data[num1]['y']]
            point2 = [data[num2]['x'], data[num2]['y']]

            x_values = [point1[0], point2[0]]
            y_values = [point1[1], point2[1]]

            self.ax.plot(x_values, y_values, color="black")

            self.counter += 1
            self.fig.canvas.draw()

            title.set_text(u"Years: {}".format(years))
            return planet1, planet2, title

        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        plt.grid(False)
        plt.gca().set_aspect('equal')
        plt.axis("off")

        title = self.ax.text(0.5, 0.97, "", bbox={'facecolor': 'w', 'alpha': 0.0, 'pad': 5},
                             transform=self.ax.transAxes, ha="center")

        planet1_data_x = []
        planet1_data_y = []

        planet2_data_x = []
        planet2_data_y = []

        theta_planet1 = np.linspace(0, 2*math.pi, 1000)
        planet1, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][num1])
        r_planet1, x_planet1, y_planet1 = position(theta_planet1, self.file_planets["a"][num1],
                                                   self.file_planets["Epsilon"][num1])
        self.ax.plot(x_planet1, y_planet1, color=self.file_planets["Colour"][num1], linewidth=2,
                     label=self.file_planets["Object"][num1])
        planet1_data_x.append(x_planet1[0])
        planet1_data_y.append(y_planet1[0])

        theta_planet2 = np.linspace(0, 2*math.pi, 1000)
        planet2, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][num2])
        r_planet2, x_planet2, y_planet2 = position(theta_planet2, self.file_planets["a"][num2],
                                                   self.file_planets["Epsilon"][num2])
        self.ax.plot(x_planet2, y_planet2, color=self.file_planets["Colour"][num2], linewidth=2,
                     label=self.file_planets["Object"][num2])
        planet2_data_x.append(x_planet2[0])
        planet2_data_y.append(y_planet2[0])

        planet1.set_data(planet1_data_x, planet1_data_y)
        planet2.set_data(planet2_data_x, planet2_data_y)

        self.event = Clock.schedule_interval(animate, 1/60)

        figure_canvas = FigureCanvas(self.fig)
        self.add_widget(figure_canvas)

        plt.close()

        button = Button(text='Go back', size_hint=(1, None), height=100, padding=(10, 10))
        button.bind(on_press=self.options_screen)
        self.add_widget(button)

        if num1 > num2:
            temp = num1
            num1 = num2
            num2 = temp
        planet1_name = self.file_planets["Object"][num1]
        planet2_name = self.file_planets["Object"][num2]
        title_text = f"Task 6: Animating 2D Elliptical Orbits {planet1_name}-{planet2_name} Spirograph"
        title_widget = Label(text=title_text, font_size=50, padding=(10, 10), halign="center", valign='center',
                             color="black")
        title_widget.pos = (0,  5 * self.height / 12)
        self.add_widget(title_widget)

    def options_screen(self, instance):
        self.clear_widgets()
        self.event.cancel()
        self.add_widget(TaskSixScreen())

    def home_screen(self, instance):
        self.clear_widgets()
        self.add_widget(m.MainScreen())