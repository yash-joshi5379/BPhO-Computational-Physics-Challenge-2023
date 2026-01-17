from kivy.uix.button import Button
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
import math
import numpy as np
from kivy.clock import Clock
from backend_kivyagg import FigureCanvasKivyAgg as FigureCanvas
#from garden.backend_kivyagg import FigureCanvasKivyAgg as FigureCanvas
import main as m

matplotlib.use("Agg")


def position_2d(theta_func, a, eps):
    r_func = a * (1 - eps ** 2) / (1 - eps * np.cos(theta_func))
    x_func = r_func * np.cos(theta_func)
    y_func = r_func * np.sin(theta_func)

    return r_func, x_func, y_func


def loop_2d(i, speed, file):
    data = {}
    if speed == 2.125:
        x = 1
        y = 5
    else:
        x = 5
        y = 10
    for j in range(x, y):
        theta_func = (i * speed * np.pi) / (file["P"][j] * 180)
        e_temp = file["Epsilon"][j]
        r_func, x_func, y_func = position_2d(theta_func, file["a"][j], e_temp)

        data[j] = {
            'x': [x_func],
            'y': [y_func],
            'colour': file["Colour"][j]
        }
    return data


def position_3d(theta_func, a, eps, inclination):
    inclination_rad = math.radians(inclination)

    r_func = a * (1 - eps ** 2) / (1 - eps * np.cos(theta_func))
    x_func = r_func * np.cos(theta_func) * np.cos(inclination_rad)
    y_func = r_func * np.sin(theta_func)
    z_func = r_func * np.cos(theta_func) * np.sin(inclination_rad)

    return r_func, x_func, y_func, z_func


def loop_3d(i, speed, file):
    data = {}
    if speed == 2.125:
        x = 1
        y = 5
    else:
        x = 5
        y = 10
    for j in range(x, y):
        theta_func = (i * speed * np.pi) / (file["P"][j] * 180)
        e_temp = file["Epsilon"][j]
        inclination = file["Inclination"][j]
        r_func, x_func, y_func, z_func = position_3d(theta_func, file["a"][j], e_temp, inclination)

        data[j] = {
            'x': [x_func],
            'y': [y_func],
            'z': [z_func],
            'colour': file["Colour"][j]
        }
    return data


class TaskSevenScreen(RelativeLayout):

    def __init__(self, **kwargs):
        super(TaskSevenScreen, self).__init__(**kwargs)
        self.ax = None
        self.fig = None
        self.event = None
        self.width, self.height = Window.system_size
        self.counter = 0
        self.planet_centre = 0
        self.buttons = []
        self.dimension = 0
        self.file_planets = pd.read_excel("planets.xlsx")
        self.orientation = 'horizontal'
        self.create_screen()

    def create_screen(self):

        plt.style.use("dark_background")

        title_text = "Task 7: Animating 2D and 3D Elliptical Orbits Relative to Planets"
        title = Label(text=title_text, font_size=50, padding=(10, 10), halign="center", valign='center')
        title.pos = (0, 4 * self.height / 5)
        self.add_widget(title)

        label_text = "Please select the dimension and a planet to put at the centre of the solar system."
        label = Label(text=label_text, font_size=40, padding=(10, 10), halign="center", valign="center")
        label.pos = (0, 7 * self.height / 11)
        self.add_widget(label)

        inner_text = "Inner Planets"
        label_inner = Label(text=inner_text, font_size=50, padding=(10, 10), halign="center", valign="center")
        label_inner.pos = (-self.width / 2, self.height / 5)
        self.add_widget(label_inner)

        outer_text = "Outer Planets"
        label_outer = Label(text=outer_text, font_size=50, padding=(10, 10), halign="center", valign="center")
        label_outer.pos = (self.width / 2, self.height / 5)
        self.add_widget(label_outer)

        self.button_2d = Button(text='2D', on_release=self.add_2d, size_hint=(1/2, 1/9))
        self.button_2d.pos = (0, 4*self.height/3)
        self.add_widget(self.button_2d)

        self.button_3d = Button(text='3D', on_release=self.add_3d, size_hint=(1/2, 1/9))
        self.button_3d.pos = (self.width, 4*self.height/3)
        self.add_widget(self.button_3d)

        self.button1 = Button(text="Mercury", on_release=self.centre_mercury, size_hint=(1/2, 1/9))
        self.button1.pos = (0, 8 * self.height / 9)
        self.buttons.append(self.button1)
        self.add_widget(self.button1)

        self.button2 = Button(text="Venus", on_release=self.centre_venus, size_hint=(1/2, 1/9))
        self.button2.pos = (0, 6 * self.height / 9)
        self.buttons.append(self.button2)
        self.add_widget(self.button2)

        self.button3 = Button(text="Earth", on_release=self.centre_earth, size_hint=(1/2, 1/9))
        self.button3.pos = (0, 4 * self.height / 9)
        self.buttons.append(self.button3)
        self.add_widget(self.button3)

        self.button4 = Button(text="Mars", on_release=self.centre_mars, size_hint=(1/2, 1/9))
        self.button4.pos = (0, 2 * self.height / 9)
        self.buttons.append(self.button4)
        self.add_widget(self.button4)

        self.button5 = Button(text="Jupiter", on_release=self.centre_jupiter, size_hint=(1/2, 1/9))
        self.button5.pos = (self.width, 8*self.height/9)
        self.buttons.append(self.button5)
        self.add_widget(self.button5)

        self.button6 = Button(text="Saturn", on_release=self.centre_saturn, size_hint=(1/2, 1/9))
        self.button6.pos = (self.width, 6*self.height/9)
        self.buttons.append(self.button6)
        self.add_widget(self.button6)

        self.button7 = Button(text="Uranus", on_release=self.centre_uranus, size_hint=(1/2, 1/9))
        self.button7.pos = (self.width, 4*self.height/9)
        self.buttons.append(self.button7)
        self.add_widget(self.button7)

        self.button8 = Button(text="Neptune", on_release=self.centre_neptune, size_hint=(1/2, 1/9))
        self.button8.pos = (self.width, 2*self.height/9)
        self.buttons.append(self.button8)
        self.add_widget(self.button8)

        self.button9 = Button(text="Pluto", on_release=self.centre_pluto, size_hint=(1/2, 1/9))
        self.button9.pos = (self.width, 0)
        self.buttons.append(self.button9)
        self.add_widget(self.button9)

        home_button = Button(text='Go back', size_hint=(89/180, 1/10))
        home_button.bind(on_release=self.home_screen)
        home_button.pos = (0, 0)
        self.add_widget(home_button)

    def add_2d(self, button):
        if self.dimension == 2:
            self.button_2d.background_color = (1, 1, 1, 1)
            self.dimension = 0
        else:
            self.button_2d.background_color = (0, 1, 0, 1)
            self.button_3d.background_color = (1, 1, 1, 1)
            self.dimension = 2

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def add_3d(self, button):
        if self.dimension == 3:
            self.button_3d.background_color = (1, 1, 1, 1)
            self.dimension = 0
        else:
            self.button_3d.background_color = (0, 1, 0, 1)
            self.button_2d.background_color = (1, 1, 1, 1)
            self.dimension = 3

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def centre_mercury(self, button):
        if self.planet_centre == 1:
            self.button1.background_color = (1, 1, 1, 1)
            self.planet_centre = 0
        else:
            for button in self.buttons:
                button.background_color = (1, 1, 1, 1)
            self.button1.background_color = (0, 1, 0, 1)
            self.planet_centre = 1

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def centre_venus(self, button):
        if self.planet_centre == 2:
            self.button2.background_color = (1, 1, 1, 1)
            self.planet_centre = 0
        else:
            for button in self.buttons:
                button.background_color = (1, 1, 1, 1)
            self.button2.background_color = (0, 1, 0, 1)
            self.planet_centre = 2

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def centre_earth(self, button):
        if self.planet_centre == 3:
            self.button3.background_color = (1, 1, 1, 1)
            self.planet_centre = 0
        else:
            for button in self.buttons:
                button.background_color = (1, 1, 1, 1)
            self.button3.background_color = (0, 1, 0, 1)
            self.planet_centre = 3

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def centre_mars(self, button):
        if self.planet_centre == 4:
            self.button4.background_color = (1, 1, 1, 1)
            self.planet_centre = 0
        else:
            for button in self.buttons:
                button.background_color = (1, 1, 1, 1)
            self.button4.background_color = (0, 1, 0, 1)
            self.planet_centre = 4

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def centre_jupiter(self, button):
        if self.planet_centre == 5:
            self.button5.background_color = (1, 1, 1, 1)
            self.planet_centre = 0
        else:
            for button in self.buttons:
                button.background_color = (1, 1, 1, 1)
            self.button5.background_color = (0, 1, 0, 1)
            self.planet_centre = 5

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def centre_saturn(self, button):
        if self.planet_centre == 6:
            self.button6.background_color = (1, 1, 1, 1)
            self.planet_centre = 0
        else:
            for button in self.buttons:
                button.background_color = (1, 1, 1, 1)
            self.button6.background_color = (0, 1, 0, 1)
            self.planet_centre = 6

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def centre_uranus(self, button):
        if self.planet_centre == 7:
            self.button7.background_color = (1, 1, 1, 1)
            self.planet_centre = 0
        else:
            for button in self.buttons:
                button.background_color = (1, 1, 1, 1)
            self.button7.background_color = (0, 1, 0, 1)
            self.planet_centre = 7

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def centre_neptune(self, button):
        if self.planet_centre == 8:
            self.button8.background_color = (1, 1, 1, 1)
            self.planet_centre = 0
        else:
            for button in self.buttons:
                button.background_color = (1, 1, 1, 1)
            self.button8.background_color = (0, 1, 0, 1)
            self.planet_centre = 8

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def centre_pluto(self, button):
        if self.planet_centre == 9:
            self.button9.background_color = (1, 1, 1, 1)
            self.planet_centre = 0
        else:
            for button in self.buttons:
                button.background_color = (1, 1, 1, 1)
            self.button9.background_color = (0, 1, 0, 1)
            self.planet_centre = 9

        if self.dimension != 0 and self.planet_centre != 0:
            self.create_sketch()

    def create_sketch(self):
        self.clear_widgets()
        if self.dimension == 2 and self.planet_centre in [1, 2, 3, 4]:
            self.sketch_2d_inner(self.planet_centre)
        elif self.dimension == 2:
            self.sketch_2d_outer(self.planet_centre)
        elif self.planet_centre in [1, 2, 3, 4]:
            self.sketch_3d_inner(self.planet_centre)
        else:
            self.sketch_3d_outer(self.planet_centre)

    def sketch_2d_inner(self, centre):
        anim_speed = 2.125
        planet_nums = [1, 2, 3, 4]
        planet_nums.remove(centre)
        p1 = planet_nums[0]
        p2 = planet_nums[1]
        p3 = planet_nums[2]

        def animate(i):
            years = round(1000 * self.counter * anim_speed / 360) / 1000
            data = loop_2d(self.counter, anim_speed, self.file_planets)
            data_previous = loop_2d(self.counter-1, anim_speed, self.file_planets)

            centre_planet.set_data(0, 0)
            centre_planet.set_color(data[centre]["colour"])

            sun.set_data(-data[centre]['x'], -data[centre]['y'])
            sun.set_color("yellow")
            self.ax.plot([-data_previous[centre]['x'], -data[centre]['x']],
                         [-data_previous[centre]['y'], -data[centre]['y']],
                         color="yellow", linewidth=2)

            planet1_x = data[p1]['x'] - data[centre]['x']
            planet1_y = data[p1]['y'] - data[centre]['y']
            planet1_prev_x = data_previous[p1]['x'] - data_previous[centre]['x']
            planet1_prev_y = data_previous[p1]['y'] - data_previous[centre]['y']
            planet1.set_data(planet1_x, planet1_y)
            planet1.set_color(data[p1]["colour"])
            self.ax.plot([planet1_prev_x, planet1_x], [planet1_prev_y, planet1_y],
                         color=data[p1]["colour"], linewidth=2)

            planet2_x = data[p2]['x'] - data[centre]['x']
            planet2_y = data[p2]['y'] - data[centre]['y']
            planet2_prev_x = data_previous[p2]['x'] - data_previous[centre]['x']
            planet2_prev_y = data_previous[p2]['y'] - data_previous[centre]['y']
            planet2.set_data(planet2_x, planet2_y)
            planet2.set_color(data[p2]["colour"])
            self.ax.plot([planet2_prev_x, planet2_x], [planet2_prev_y, planet2_y],
                         color=data[p2]["colour"], linewidth=2)

            planet3_x = data[p3]['x'] - data[centre]['x']
            planet3_y = data[p3]['y'] - data[centre]['y']
            planet3_prev_x = data_previous[p3]['x'] - data_previous[centre]['x']
            planet3_prev_y = data_previous[p3]['y'] - data_previous[centre]['y']
            planet3.set_data(planet3_x, planet3_y)
            planet3.set_color(data[p3]["colour"])
            self.ax.plot([planet3_prev_x, planet3_x], [planet3_prev_y, planet3_y],
                         color=data[p3]["colour"], linewidth=2)

            title.set_text(u"Years: {}".format(years))

            self.counter += 1
            self.fig.canvas.draw()

            return centre_planet, sun, planet1, planet2, planet3, title

        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        plt.grid(True)


        title = self.ax.text(0.5, 0.97, "", bbox={'facecolor': 'w', 'alpha': 0.0, 'pad': 5},
                             transform=self.ax.transAxes, ha="center", fontsize=20)

        centre_planet_data_x = []
        centre_planet_data_y = []

        sun_data_x = []
        sun_data_y = []

        planet1_data_x = []
        planet1_data_y = []

        planet2_data_x = []
        planet2_data_y = []

        planet3_data_x = []
        planet3_data_y = []

        theta_centre_planet = np.linspace(0, 2 * math.pi, 1000)
        centre_planet, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][centre])
        r_centre_planet, x_centre_planet, y_centre_planet = position_2d(theta_centre_planet,
                                                                        self.file_planets["a"][centre],
                                                                        self.file_planets["Epsilon"][centre])
        centre_planet_data_x.append(x_centre_planet[0])
        centre_planet_data_y.append(y_centre_planet[0])

        theta_sun = np.linspace(0, 2 * math.pi, 1000)
        sun, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][0])
        r_sun, x_sun, y_sun = position_2d(theta_sun, self.file_planets["a"][0], self.file_planets["Epsilon"][0])
        sun_data_x.append(x_sun[0] - x_centre_planet[0])
        sun_data_y.append(y_sun[0] - y_centre_planet[0])

        theta_planet1 = np.linspace(0, 2 * math.pi, 1000)
        planet1, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][p1])
        r_planet1, x_planet1, y_planet1 = position_2d(theta_planet1, self.file_planets["a"][p1],
                                                      self.file_planets["Epsilon"][p1])
        planet1_data_x.append(x_planet1[0] - x_centre_planet[0])
        planet1_data_y.append(y_planet1[0] - y_centre_planet[0])

        theta_planet2 = np.linspace(0, 2 * math.pi, 1000)
        planet2, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][p2])
        r_planet2, x_planet2, y_planet2 = position_2d(theta_planet2, self.file_planets["a"][p2],
                                                      self.file_planets["Epsilon"][p2])
        planet2_data_x.append(x_planet2[0] - x_centre_planet[0])
        planet2_data_y.append(y_planet2[0] - y_centre_planet[0])

        theta_planet3 = np.linspace(0, 2 * math.pi, 1000)
        planet3, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][p3])
        r_planet3, x_planet3, y_planet3 = position_2d(theta_planet3, self.file_planets["a"][p3],
                                                      self.file_planets["Epsilon"][p3])
        planet3_data_x.append(x_planet3[0] - x_centre_planet[0])
        planet3_data_y.append(y_planet3[0] - y_centre_planet[0])

        centre_planet.set_data(0, 0)
        sun.set_data(sun_data_x, sun_data_y)
        planet1.set_data(planet1_data_x, planet1_data_y)
        planet2.set_data(planet2_data_x, planet2_data_y)
        planet3.set_data(planet3_data_x, planet3_data_y)

        plt.legend(labels=[f"{self.file_planets['Object'][centre]}",
                           "Sun",
                           f"{self.file_planets['Object'][p1]}",
                           f"{self.file_planets['Object'][p2]}",
                           f"{self.file_planets['Object'][p3]}"],
                   fontsize=20, loc="upper left")

        self.event = Clock.schedule_interval(animate, 1 / 100)

        figure_canvas = FigureCanvas(self.fig)
        self.add_widget(figure_canvas)

        plt.close()

        button = Button(text='Go back', size_hint=(1, None), height=100, padding=(10, 10))
        button.bind(on_press=self.options_screen)
        self.add_widget(button)

        title_text = f"Task 7: Animating the Inner Orbits Relative to {self.file_planets['Object'][centre]} in 2D"
        title_widget = Label(text=title_text, font_size=50, padding=(10, 10), halign="center", valign='center')
        title_widget.pos = (0, 5 * self.height / 12)
        self.add_widget(title_widget)

    def sketch_2d_outer(self, centre):
        anim_speed = 200
        planet_nums = [5, 6, 7, 8, 9]
        planet_nums.remove(centre)
        p1 = planet_nums[0]
        p2 = planet_nums[1]
        p3 = planet_nums[2]
        p4 = planet_nums[3]

        def animate(i):
            years = round(1000 * self.counter * anim_speed / 360) / 1000
            data = loop_2d(self.counter, anim_speed, self.file_planets)
            data_previous = loop_2d(self.counter - 1, anim_speed, self.file_planets)

            centre_planet.set_data(0, 0)
            centre_planet.set_color(data[centre]["colour"])

            sun.set_data(-data[centre]['x'], -data[centre]['y'])
            sun.set_color("yellow")
            self.ax.plot([-data_previous[centre]['x'], -data[centre]['x']],
                         [-data_previous[centre]['y'], -data[centre]['y']],
                         color="yellow", linewidth=2)

            planet1_x = data[p1]['x'] - data[centre]['x']
            planet1_y = data[p1]['y'] - data[centre]['y']
            planet1_prev_x = data_previous[p1]['x'] - data_previous[centre]['x']
            planet1_prev_y = data_previous[p1]['y'] - data_previous[centre]['y']
            planet1.set_data(planet1_x, planet1_y)
            planet1.set_color(data[p1]["colour"])
            self.ax.plot([planet1_prev_x, planet1_x], [planet1_prev_y, planet1_y],
                         color=data[p1]["colour"], linewidth=2)

            planet2_x = data[p2]['x'] - data[centre]['x']
            planet2_y = data[p2]['y'] - data[centre]['y']
            planet2_prev_x = data_previous[p2]['x'] - data_previous[centre]['x']
            planet2_prev_y = data_previous[p2]['y'] - data_previous[centre]['y']
            planet2.set_data(planet2_x, planet2_y)
            planet2.set_color(data[p2]["colour"])
            self.ax.plot([planet2_prev_x, planet2_x], [planet2_prev_y, planet2_y],
                         color=data[p2]["colour"], linewidth=2)

            planet3_x = data[p3]['x'] - data[centre]['x']
            planet3_y = data[p3]['y'] - data[centre]['y']
            planet3_prev_x = data_previous[p3]['x'] - data_previous[centre]['x']
            planet3_prev_y = data_previous[p3]['y'] - data_previous[centre]['y']
            planet3.set_data(planet3_x, planet3_y)
            planet3.set_color(data[p3]["colour"])
            self.ax.plot([planet3_prev_x, planet3_x], [planet3_prev_y, planet3_y],
                         color=data[p3]["colour"], linewidth=2)

            planet4_x = data[p4]['x'] - data[centre]['x']
            planet4_y = data[p4]['y'] - data[centre]['y']
            planet4_prev_x = data_previous[p4]['x'] - data_previous[centre]['x']
            planet4_prev_y = data_previous[p4]['y'] - data_previous[centre]['y']
            planet4.set_data(planet4_x, planet4_y)
            planet4.set_color(data[p4]["colour"])
            self.ax.plot([planet4_prev_x, planet4_x], [planet4_prev_y, planet4_y],
                         color=data[p4]["colour"], linewidth=2)

            title.set_text(u"Years: {}".format(years))

            self.counter += 1
            self.fig.canvas.draw()

            return centre_planet, sun, planet1, planet2, planet3, planet4, title

        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        plt.grid(True)

        title = self.ax.text(0.5, 0.97, "", bbox={'facecolor': 'w', 'alpha': 0.0, 'pad': 5},
                             transform=self.ax.transAxes, ha="center", fontsize=20)

        centre_planet_data_x = []
        centre_planet_data_y = []

        sun_data_x = []
        sun_data_y = []

        planet1_data_x = []
        planet1_data_y = []

        planet2_data_x = []
        planet2_data_y = []

        planet3_data_x = []
        planet3_data_y = []

        planet4_data_x = []
        planet4_data_y = []

        theta_centre_planet = np.linspace(0, 2 * math.pi, 1000)
        centre_planet, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][centre])
        r_centre_planet, x_centre_planet, y_centre_planet = position_2d(theta_centre_planet,
                                                                        self.file_planets["a"][centre],
                                                                        self.file_planets["Epsilon"][centre])
        centre_planet_data_x.append(x_centre_planet[0])
        centre_planet_data_y.append(y_centre_planet[0])

        theta_sun = np.linspace(0, 2 * math.pi, 1000)
        sun, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][0])
        r_sun, x_sun, y_sun = position_2d(theta_sun, self.file_planets["a"][0], self.file_planets["Epsilon"][0])
        sun_data_x.append(x_sun[0] - x_centre_planet[0])
        sun_data_y.append(y_sun[0] - y_centre_planet[0])

        theta_planet1 = np.linspace(0, 2 * math.pi, 1000)
        planet1, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][p1])
        r_planet1, x_planet1, y_planet1 = position_2d(theta_planet1, self.file_planets["a"][p1],
                                                      self.file_planets["Epsilon"][p1])
        planet1_data_x.append(x_planet1[0] - x_centre_planet[0])
        planet1_data_y.append(y_planet1[0] - y_centre_planet[0])

        theta_planet2 = np.linspace(0, 2 * math.pi, 1000)
        planet2, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][p2])
        r_planet2, x_planet2, y_planet2 = position_2d(theta_planet2, self.file_planets["a"][p2],
                                                      self.file_planets["Epsilon"][p2])
        planet2_data_x.append(x_planet2[0] - x_centre_planet[0])
        planet2_data_y.append(y_planet2[0] - y_centre_planet[0])

        theta_planet3 = np.linspace(0, 2 * math.pi, 1000)
        planet3, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][p3])
        r_planet3, x_planet3, y_planet3 = position_2d(theta_planet3, self.file_planets["a"][p3],
                                                      self.file_planets["Epsilon"][p3])
        planet3_data_x.append(x_planet3[0] - x_centre_planet[0])
        planet3_data_y.append(y_planet3[0] - y_centre_planet[0])

        theta_planet4 = np.linspace(0, 2 * math.pi, 1000)
        planet4, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][p4])
        r_planet4, x_planet4, y_planet4 = position_2d(theta_planet4, self.file_planets["a"][p4],
                                                      self.file_planets["Epsilon"][p4])
        planet4_data_x.append(x_planet4[0] - x_centre_planet[0])
        planet4_data_y.append(y_planet4[0] - y_centre_planet[0])

        centre_planet.set_data(0, 0)
        sun.set_data(sun_data_x, sun_data_y)
        planet1.set_data(planet1_data_x, planet1_data_y)
        planet2.set_data(planet2_data_x, planet2_data_y)
        planet3.set_data(planet3_data_x, planet3_data_y)
        planet4.set_data(planet4_data_x, planet4_data_y)

        plt.legend(labels=[f"{self.file_planets['Object'][centre]}",
                           "Sun",
                           f"{self.file_planets['Object'][p1]}",
                           f"{self.file_planets['Object'][p2]}",
                           f"{self.file_planets['Object'][p3]}",
                           f"{self.file_planets['Object'][p4]}"],
                   fontsize=20, loc="upper left")

        self.event = Clock.schedule_interval(animate, 1 / 100)

        figure_canvas = FigureCanvas(self.fig)
        self.add_widget(figure_canvas)

        plt.close()

        button = Button(text='Go back', size_hint=(1, None), height=100, padding=(10, 10))
        button.bind(on_press=self.options_screen)
        self.add_widget(button)

        title_text = f"Task 7: Animating the Outer Orbits Relative to {self.file_planets['Object'][centre]} in 2D"
        title_widget = Label(text=title_text, font_size=50, padding=(10, 10), halign="center", valign='center')
        title_widget.pos = (0, 5 * self.height / 12)
        self.add_widget(title_widget)

    def sketch_3d_inner(self, centre):
        anim_speed = 2.125
        planet_nums = [1, 2, 3, 4]
        planet_nums.remove(centre)
        p1 = planet_nums[0]
        p2 = planet_nums[1]
        p3 = planet_nums[2]

        def animate(i):
            years = round(1000 * self.counter * anim_speed / 360) / 1000
            data = loop_3d(self.counter, anim_speed, self.file_planets)
            data_previous = loop_3d(self.counter - 1, anim_speed, self.file_planets)

            centre_planet.set_data([0], [0])
            centre_planet.set_3d_properties(0)
            centre_planet.set_color(data[centre]["colour"])

            sun.set_data(-np.array(data[centre]['x']), -np.array(data[centre]['y']))
            sun.set_3d_properties(-np.array(data[centre]['z']))
            sun.set_color("yellow")
            self.ax.plot([-np.array(data_previous[centre]['x']), -np.array(data[centre]['x'])],
                         [-np.array(data_previous[centre]['y']), -np.array(data[centre]['y'])],
                         [-np.array(data_previous[centre]['z']), -np.array(data[centre]['z'])],
                         color="yellow", linewidth=2)

            planet1_x = data[p1]['x'] - data[centre]['x']
            planet1_y = data[p1]['y'] - data[centre]['y']
            planet1_z = data[p1]['z'] - data[centre]['z']
            planet1_prev_x = data_previous[p1]['x'] - data_previous[centre]['x']
            planet1_prev_y = data_previous[p1]['y'] - data_previous[centre]['y']
            planet1_prev_z = data_previous[p1]['z'] - data_previous[centre]['z']
            planet1.set_data(planet1_x, planet1_y)
            planet1.set_3d_properties(planet1_z)
            planet1.set_color(data[p1]["colour"])
            self.ax.plot([planet1_prev_x, planet1_x],
                         [planet1_prev_y, planet1_y],
                         [planet1_prev_z, planet1_z],
                         color=data[p1]["colour"], linewidth=2)

            planet2_x = data[p2]['x'] - data[centre]['x']
            planet2_y = data[p2]['y'] - data[centre]['y']
            planet2_z = data[p2]['z'] - data[centre]['z']
            planet2_prev_x = data_previous[p2]['x'] - data_previous[centre]['x']
            planet2_prev_y = data_previous[p2]['y'] - data_previous[centre]['y']
            planet2_prev_z = data_previous[p2]['z'] - data_previous[centre]['z']
            planet2.set_data(planet2_x, planet2_y)
            planet2.set_3d_properties(planet2_z)
            planet2.set_color(data[p2]["colour"])
            self.ax.plot([planet2_prev_x, planet2_x],
                         [planet2_prev_y, planet2_y],
                         [planet2_prev_z, planet2_z],
                         color=data[p2]["colour"], linewidth=2)

            planet3_x = data[p3]['x'] - data[centre]['x']
            planet3_y = data[p3]['y'] - data[centre]['y']
            planet3_z = data[p3]['z'] - data[centre]['z']
            planet3_prev_x = data_previous[p3]['x'] - data_previous[centre]['x']
            planet3_prev_y = data_previous[p3]['y'] - data_previous[centre]['y']
            planet3_prev_z = data_previous[p3]['z'] - data_previous[centre]['z']
            planet3.set_data(planet3_x, planet3_y)
            planet3.set_3d_properties(planet3_z)
            planet3.set_color(data[p3]["colour"])
            self.ax.plot([planet3_prev_x, planet3_x],
                         [planet3_prev_y, planet3_y],
                         [planet3_prev_z, planet3_z],
                         color=data[p3]["colour"], linewidth=2)

            title.set_text(u"Years: {}".format(years))

            self.counter += 1
            self.fig.canvas.draw()

            return centre_planet, sun, planet1, planet2, planet3, title

        self.fig = plt.figure(figsize=(10, 10))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_xlabel("X/AU")
        self.ax.set_ylabel("Y/AU")
        self.ax.set_zlabel("Z/AU")
        self.ax.invert_xaxis()
        self.ax.invert_yaxis()
        self.ax.view_init(elev=20, azim=40)
        plt.grid(True)

        title = self.ax.text(10, 10, 0, "", bbox={'facecolor': 'w', 'alpha': 0.0, 'pad': 5},
                             transform=self.ax.transAxes, ha="center", fontsize=20)

        centre_planet_data_x = []
        centre_planet_data_y = []
        centre_planet_data_z = []

        sun_data_x = []
        sun_data_y = []
        sun_data_z = []

        planet1_data_x = []
        planet1_data_y = []
        planet1_data_z = []

        planet2_data_x = []
        planet2_data_y = []
        planet2_data_z = []

        planet3_data_x = []
        planet3_data_y = []
        planet3_data_z = []

        theta_centre_planet = np.linspace(0, 2 * math.pi, 1000)
        centre_planet, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][centre])
        r_centre_planet, x_centre_planet,\
            y_centre_planet, z_centre_planet = position_3d(theta_centre_planet,
                                                           self.file_planets["a"][centre],
                                                           self.file_planets["Epsilon"][centre],
                                                           self.file_planets["Inclination"][centre])
        centre_planet_data_x.append(x_centre_planet[0])
        centre_planet_data_y.append(y_centre_planet[0])
        centre_planet_data_z.append(z_centre_planet[0])

        theta_sun = np.linspace(0, 2 * math.pi, 1000)
        sun, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][0])
        r_sun, x_sun, y_sun, z_sun = position_3d(theta_sun, self.file_planets["a"][0],
                                                 self.file_planets["Epsilon"][0],
                                                 self.file_planets["Inclination"][0])
        sun_data_x.append(x_sun[0] - x_centre_planet[0])
        sun_data_y.append(y_sun[0] - y_centre_planet[0])
        sun_data_z.append(z_sun[0] - z_centre_planet[0])

        theta_planet1 = np.linspace(0, 2 * math.pi, 1000)
        planet1, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][p1])
        r_planet1, x_planet1, y_planet1, z_planet1 = position_3d(theta_planet1, self.file_planets["a"][p1],
                                                                 self.file_planets["Epsilon"][p1],
                                                                 self.file_planets["Inclination"][0])
        planet1_data_x.append(x_planet1[0] - x_centre_planet[0])
        planet1_data_y.append(y_planet1[0] - y_centre_planet[0])
        planet1_data_z.append(z_planet1[0] - z_centre_planet[0])

        theta_planet2 = np.linspace(0, 2 * math.pi, 1000)
        planet2, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][p2])
        r_planet2, x_planet2, y_planet2, z_planet2 = position_3d(theta_planet2, self.file_planets["a"][p2],
                                                                 self.file_planets["Epsilon"][p2],
                                                                 self.file_planets["Inclination"][p2])
        planet2_data_x.append(x_planet2[0] - x_centre_planet[0])
        planet2_data_y.append(y_planet2[0] - y_centre_planet[0])
        planet2_data_z.append(z_planet2[0] - z_centre_planet[0])

        theta_planet3 = np.linspace(0, 2 * math.pi, 1000)
        planet3, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][p3])
        r_planet3, x_planet3, y_planet3, z_planet3 = position_3d(theta_planet3, self.file_planets["a"][p3],
                                                                 self.file_planets["Epsilon"][p3],
                                                                 self.file_planets["Inclination"][p3])
        planet3_data_x.append(x_planet3[0] - x_centre_planet[0])
        planet3_data_y.append(y_planet3[0] - y_centre_planet[0])
        planet3_data_z.append(z_planet3[0] - z_centre_planet[0])

        centre_planet.set_data([0], [0])
        centre_planet.set_3d_properties(0)
        sun.set_data(sun_data_x, sun_data_y)
        sun.set_3d_properties(sun_data_z)
        planet1.set_data(planet1_data_x, planet1_data_y)
        planet1.set_3d_properties(planet1_data_z)
        planet2.set_data(planet2_data_x, planet2_data_y)
        planet2.set_3d_properties(planet2_data_z)
        planet3.set_data(planet3_data_x, planet3_data_y)
        planet3.set_3d_properties(planet3_data_z)

        plt.legend(labels=[f"{self.file_planets['Object'][centre]}",
                           "Sun",
                           f"{self.file_planets['Object'][p1]}",
                           f"{self.file_planets['Object'][p2]}",
                           f"{self.file_planets['Object'][p3]}"],
                   fontsize=20, loc="lower right")

        self.event = Clock.schedule_interval(animate, 1 / 100)

        figure_canvas = FigureCanvas(self.fig)
        self.add_widget(figure_canvas)

        plt.close()

        button = Button(text='Go back', size_hint=(1, None), height=100, padding=(10, 10))
        button.bind(on_press=self.options_screen)
        self.add_widget(button)

        title_text = f"Task 7: Animating the Inner Orbits Relative to {self.file_planets['Object'][centre]} in 3D"
        title_widget = Label(text=title_text, font_size=50, padding=(10, 10), halign="center", valign='center')
        title_widget.pos = (0, 5 * self.height / 12)
        self.add_widget(title_widget)

    def sketch_3d_outer(self, centre):
        anim_speed = 100
        planet_nums = [5, 6, 7, 8, 9]
        planet_nums.remove(centre)
        p1 = planet_nums[0]
        p2 = planet_nums[1]
        p3 = planet_nums[2]
        p4 = planet_nums[3]

        def animate(i):
            years = round(1000 * self.counter * anim_speed / 360) / 1000
            data = loop_3d(self.counter, anim_speed, self.file_planets)
            data_previous = loop_3d(self.counter - 1, anim_speed, self.file_planets)

            centre_planet.set_data(0, 0)
            centre_planet.set_3d_properties(0)
            centre_planet.set_color(data[centre]["colour"])

            sun.set_data(-data[centre]['x'], -data[centre]['y'])
            sun.set_3d_properties(-data[centre]['z'])
            sun.set_color("yellow")
            self.ax.plot([-data_previous[centre]['x'], -data[centre]['x']],
                         [-data_previous[centre]['y'], -data[centre]['y']],
                         [-data_previous[centre]['z'], -data[centre]['z']],
                         color="yellow", linewidth=2)

            planet1_x = data[p1]['x'] - data[centre]['x']
            planet1_y = data[p1]['y'] - data[centre]['y']
            planet1_z = data[p1]['z'] - data[centre]['z']
            planet1_prev_x = data_previous[p1]['x'] - data_previous[centre]['x']
            planet1_prev_y = data_previous[p1]['y'] - data_previous[centre]['y']
            planet1_prev_z = data_previous[p1]['z'] - data_previous[centre]['z']
            planet1.set_data(planet1_x, planet1_y)
            planet1.set_3d_properties(planet1_z)
            planet1.set_color(data[p1]["colour"])
            self.ax.plot([planet1_prev_x, planet1_x],
                         [planet1_prev_y, planet1_y],
                         [planet1_prev_z, planet1_z],
                         color=data[p1]["colour"], linewidth=2)

            planet2_x = data[p2]['x'] - data[centre]['x']
            planet2_y = data[p2]['y'] - data[centre]['y']
            planet2_z = data[p2]['z'] - data[centre]['z']
            planet2_prev_x = data_previous[p2]['x'] - data_previous[centre]['x']
            planet2_prev_y = data_previous[p2]['y'] - data_previous[centre]['y']
            planet2_prev_z = data_previous[p2]['z'] - data_previous[centre]['z']
            planet2.set_data(planet2_x, planet2_y)
            planet2.set_3d_properties(planet2_z)
            planet2.set_color(data[p2]["colour"])
            self.ax.plot([planet2_prev_x, planet2_x],
                         [planet2_prev_y, planet2_y],
                         [planet2_prev_z, planet2_z],
                         color=data[p2]["colour"], linewidth=2)

            planet3_x = data[p3]['x'] - data[centre]['x']
            planet3_y = data[p3]['y'] - data[centre]['y']
            planet3_z = data[p3]['z'] - data[centre]['z']
            planet3_prev_x = data_previous[p3]['x'] - data_previous[centre]['x']
            planet3_prev_y = data_previous[p3]['y'] - data_previous[centre]['y']
            planet3_prev_z = data_previous[p3]['z'] - data_previous[centre]['z']
            planet3.set_data(planet3_x, planet3_y)
            planet3.set_3d_properties(planet3_z)
            planet3.set_color(data[p3]["colour"])
            self.ax.plot([planet3_prev_x, planet3_x],
                         [planet3_prev_y, planet3_y],
                         [planet3_prev_z, planet3_z],
                         color=data[p3]["colour"], linewidth=2)

            planet4_x = data[p4]['x'] - data[centre]['x']
            planet4_y = data[p4]['y'] - data[centre]['y']
            planet4_z = data[p4]['z'] - data[centre]['z']
            planet4_prev_x = data_previous[p4]['x'] - data_previous[centre]['x']
            planet4_prev_y = data_previous[p4]['y'] - data_previous[centre]['y']
            planet4_prev_z = data_previous[p4]['z'] - data_previous[centre]['z']
            planet4.set_data(planet4_x, planet4_y)
            planet4.set_3d_properties(planet4_z)
            planet4.set_color(data[p4]["colour"])
            self.ax.plot([planet4_prev_x, planet4_x],
                         [planet4_prev_y, planet4_y],
                         [planet4_prev_z, planet4_z],
                         color=data[p4]["colour"], linewidth=2)

            title.set_text(u"Years: {}".format(years))

            self.counter += 1
            self.fig.canvas.draw()

            return centre_planet, sun, planet1, planet2, planet3, planet4, title

        self.fig = plt.figure(figsize=(10, 10))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_xlabel("X/AU")
        self.ax.set_ylabel("Y/AU")
        self.ax.set_zlabel("Z/AU")
        self.ax.invert_xaxis()
        self.ax.invert_yaxis()
        self.ax.view_init(elev=20, azim=40)
        plt.grid(True)

        title = self.ax.text(500, 500, 0, "", bbox={'facecolor': 'w', 'alpha': 0.0, 'pad': 5},
                             transform=self.ax.transAxes, ha="center", fontsize=20)

        centre_planet_data_x = []
        centre_planet_data_y = []
        centre_planet_data_z = []

        sun_data_x = []
        sun_data_y = []
        sun_data_z = []

        planet1_data_x = []
        planet1_data_y = []
        planet1_data_z = []

        planet2_data_x = []
        planet2_data_y = []
        planet2_data_z = []

        planet3_data_x = []
        planet3_data_y = []
        planet3_data_z = []

        planet4_data_x = []
        planet4_data_y = []
        planet4_data_z = []

        theta_centre_planet = np.linspace(0, 2 * math.pi, 1000)
        centre_planet, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][centre])
        r_centre_planet, x_centre_planet, \
            y_centre_planet, z_centre_planet = position_3d(theta_centre_planet,
                                                           self.file_planets["a"][centre],
                                                           self.file_planets["Epsilon"][centre],
                                                           self.file_planets["Inclination"][centre])
        centre_planet_data_x.append(x_centre_planet[0])
        centre_planet_data_y.append(y_centre_planet[0])
        centre_planet_data_z.append(z_centre_planet[0])

        theta_sun = np.linspace(0, 2 * math.pi, 1000)
        sun, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][0])
        r_sun, x_sun, y_sun, z_sun = position_3d(theta_sun, self.file_planets["a"][0],
                                                 self.file_planets["Epsilon"][0],
                                                 self.file_planets["Inclination"][0])
        sun_data_x.append(x_sun[0] - x_centre_planet[0])
        sun_data_y.append(y_sun[0] - y_centre_planet[0])
        sun_data_z.append(z_sun[0] - z_centre_planet[0])

        theta_planet1 = np.linspace(0, 2 * math.pi, 1000)
        planet1, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][p1])
        r_planet1, x_planet1, y_planet1, z_planet1 = position_3d(theta_planet1, self.file_planets["a"][p1],
                                                                 self.file_planets["Epsilon"][p1],
                                                                 self.file_planets["Inclination"][0])
        planet1_data_x.append(x_planet1[0] - x_centre_planet[0])
        planet1_data_y.append(y_planet1[0] - y_centre_planet[0])
        planet1_data_z.append(z_planet1[0] - z_centre_planet[0])

        theta_planet2 = np.linspace(0, 2 * math.pi, 1000)
        planet2, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][p2])
        r_planet2, x_planet2, y_planet2, z_planet2 = position_3d(theta_planet2, self.file_planets["a"][p2],
                                                                 self.file_planets["Epsilon"][p2],
                                                                 self.file_planets["Inclination"][p2])
        planet2_data_x.append(x_planet2[0] - x_centre_planet[0])
        planet2_data_y.append(y_planet2[0] - y_centre_planet[0])
        planet2_data_z.append(z_planet2[0] - z_centre_planet[0])

        theta_planet3 = np.linspace(0, 2 * math.pi, 1000)
        planet3, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][p3])
        r_planet3, x_planet3, y_planet3, z_planet3 = position_3d(theta_planet3, self.file_planets["a"][p3],
                                                                 self.file_planets["Epsilon"][p3],
                                                                 self.file_planets["Inclination"][p3])
        planet3_data_x.append(x_planet3[0] - x_centre_planet[0])
        planet3_data_y.append(y_planet3[0] - y_centre_planet[0])
        planet3_data_z.append(z_planet3[0] - z_centre_planet[0])

        theta_planet4 = np.linspace(0, 2 * math.pi, 1000)
        planet4, = self.ax.plot([], [], [], '.', markersize=20, color=self.file_planets["Colour"][p4])
        r_planet4, x_planet4, y_planet4, z_planet4 = position_3d(theta_planet4, self.file_planets["a"][p4],
                                                                 self.file_planets["Epsilon"][p4],
                                                                 self.file_planets["Inclination"][p4])
        planet4_data_x.append(x_planet4[0] - x_centre_planet[0])
        planet4_data_y.append(y_planet4[0] - y_centre_planet[0])
        planet4_data_z.append(z_planet4[0] - z_centre_planet[0])

        centre_planet.set_data(0, 0)
        centre_planet.set_3d_properties(0)
        sun.set_data(sun_data_x, sun_data_y)
        sun.set_3d_properties(sun_data_z)
        planet1.set_data(planet1_data_x, planet1_data_y)
        planet1.set_3d_properties(planet1_data_z)
        planet2.set_data(planet2_data_x, planet2_data_y)
        planet2.set_3d_properties(planet2_data_z)
        planet3.set_data(planet3_data_x, planet3_data_y)
        planet3.set_3d_properties(planet3_data_z)
        planet4.set_data(planet4_data_x, planet4_data_y)
        planet4.set_3d_properties(planet4_data_z)

        plt.legend(labels=[f"{self.file_planets['Object'][centre]}",
                           "Sun",
                           f"{self.file_planets['Object'][p1]}",
                           f"{self.file_planets['Object'][p2]}",
                           f"{self.file_planets['Object'][p3]}",
                           f"{self.file_planets['Object'][p4]}"],
                   fontsize=20, loc="lower right")

        self.event = Clock.schedule_interval(animate, 1 / 100)

        figure_canvas = FigureCanvas(self.fig)
        self.add_widget(figure_canvas)

        plt.close()

        button = Button(text='Go back', size_hint=(1, None), height=100, padding=(10, 10))
        button.bind(on_press=self.options_screen)
        self.add_widget(button)

        title_text = f"Task 7: Animating the Outer Orbits Relative to {self.file_planets['Object'][centre]} in 3D"
        title_widget = Label(text=title_text, font_size=50, padding=(10, 10), halign="center", valign='center')
        title_widget.pos = (0, 5 * self.height / 12)
        self.add_widget(title_widget)

    def options_screen(self, instance):
        self.clear_widgets()
        self.event.cancel()
        self.add_widget(TaskSevenScreen())

    def home_screen(self, instance):
        self.clear_widgets()
        self.add_widget(m.MainScreen())