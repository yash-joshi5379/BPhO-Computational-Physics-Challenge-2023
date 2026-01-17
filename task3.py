from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import pandas as pd
from kivy.clock import Clock
import matplotlib.pyplot as plt
from kivy.uix.relativelayout import RelativeLayout
import math
from backend_kivyagg import FigureCanvasKivyAgg as FigureCanvas
import numpy as np
import main as m


def position(theta_func, a, eps):
    r_func = a * (1 - eps ** 2) / (1 - eps * np.cos(theta_func))
    x_func = r_func * np.cos(theta_func)
    y_func = r_func * np.sin(theta_func)

    return r_func, x_func, y_func


def loop(i, speed, file):
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
        r_func, x_func, y_func = position(theta_func, file["a"][j], e_temp)

        data[j] = {
            'x': [x_func],
            'y': [y_func],
            'colour': file["Colour"][j]
        }
    return data


class TaskThreeScreen(RelativeLayout):

    def __init__(self, **kwargs):
        super(TaskThreeScreen, self).__init__(**kwargs)
        self.ax = None
        self.fig = None
        self.event = None
        self.width, self.height = Window.system_size
        self.counter = 0
        self.file_planets = pd.read_excel("planets.xlsx")
        self.orientation = 'horizontal'
        self.create_screen()

    def create_screen(self):
        plt.style.use("dark_background")

        title_text = "Task 3: Animating 2D Elliptical Orbits"
        title = Label(text=title_text, font_size=60, padding=(10, 10), halign="center", valign='center')
        title.pos = (0, 4 * self.height / 5)
        self.add_widget(title)

        button_inner = Button(text='Plot Inner Planets', font_size=40, size_hint=(1/2, 15/24))
        button_inner.bind(on_release=self.create_screen_inner)
        button_inner.pos = (0, 2*self.height/5)
        self.add_widget(button_inner)

        button_outer = Button(text='Plot Outer Planets', font_size=40, size_hint=(1/2, 15/24))
        button_outer.bind(on_release=self.create_screen_outer)
        button_outer.pos = (self.width, 2*self.height/5)
        self.add_widget(button_outer)

        home_button = Button(text='Go back', font_size=40, size_hint=(1, 1/5))
        home_button.bind(on_release=self.home_screen)
        home_button.pos = (0, 0)
        self.add_widget(home_button)

    def create_screen_inner(self, instance):

        self.clear_widgets()

        anim_speed = 2.125

        def animate(i):
            years = round(1000 * self.counter * anim_speed / 360) / 1000

            data = loop(self.counter, anim_speed, self.file_planets)

            mercury.set_data(data[1]['x'], data[1]['y'])
            mercury.set_color(data[1]['colour'])

            venus.set_data(data[2]['x'], data[2]['y'])
            venus.set_color(data[2]['colour'])

            earth.set_data(data[3]['x'], data[3]['y'])
            earth.set_color(data[3]['colour'])

            mars.set_data(data[4]['x'], data[4]['y'])
            mars.set_color(data[4]['colour'])

            title.set_text(u"Years: {}".format(years))

            self.counter += 1
            self.fig.canvas.draw()

            return mercury, venus, earth, mars, title

        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        plt.grid(True)
        plt.xlim(-2.25, 2.25)
        plt.ylim(-1.75, 1.75)
        self.ax.set_xlabel("X/AU")
        self.ax.set_ylabel("Y/AU")

        self.ax.plot(0, 0, 'o', markersize=15, color="yellow")

        title = self.ax.text(0.5, 0.97, "", bbox={'facecolor': 'w', 'alpha': 0.0, 'pad': 5},
                             transform=self.ax.transAxes, ha="center", fontsize=20)

        mercury_data_x = []
        mercury_data_y = []

        venus_data_x = []
        venus_data_y = []

        earth_data_x = []
        earth_data_y = []

        mars_data_x = []
        mars_data_y = []

        theta_mercury = np.linspace(0, 2 * math.pi, 1000)
        mercury, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][1], label='_nolegend_')
        r_mercury, x_mercury, y_mercury = position(theta_mercury, self.file_planets["a"][1],
                                                   self.file_planets["Epsilon"][1])
        self.ax.plot(x_mercury, y_mercury, color=self.file_planets["Colour"][1], linewidth=2,
                     label=self.file_planets["Object"][1])
        mercury_data_x.append(x_mercury[0])
        mercury_data_y.append(y_mercury[0])

        theta_venus = np.linspace(0, 2 * math.pi, 1000)
        venus, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][2], label='_nolegend_')
        r_venus, x_venus, y_venus = position(theta_venus, self.file_planets["a"][2],
                                             self.file_planets["Epsilon"][2])
        self.ax.plot(x_venus, y_venus, color=self.file_planets["Colour"][2], linewidth=2,
                     label=self.file_planets["Object"][2])
        venus_data_x.append(x_venus[0])
        venus_data_y.append(y_venus[0])

        theta_earth = np.linspace(0, 2 * math.pi, 1000)
        earth, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][3], label='_nolegend_')
        r_earth, x_earth, y_earth = position(theta_earth, self.file_planets["a"][3],
                                             self.file_planets["Epsilon"][3])
        self.ax.plot(x_earth, y_earth, color=self.file_planets["Colour"][3], linewidth=2,
                     label=self.file_planets["Object"][3])
        earth_data_x.append(x_earth[0])
        earth_data_y.append(y_earth[0])

        theta_mars = np.linspace(0, 2 * math.pi, 1000)
        mars, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][4], label='_nolegend_')
        r_mars, x_mars, y_mars = position(theta_mars, self.file_planets["a"][4],
                                          self.file_planets["Epsilon"][4])
        self.ax.plot(x_mars, y_mars, color=self.file_planets["Colour"][4], linewidth=2,
                     label=self.file_planets["Object"][4])
        mars_data_x.append(x_mars[0])
        mars_data_y.append(y_mars[0])

        mercury.set_data(mercury_data_x, mercury_data_y)
        venus.set_data(venus_data_x, venus_data_y)
        earth.set_data(earth_data_x, earth_data_y)
        mars.set_data(mars_data_x, mars_data_y)

        plt.legend(labels=["Sun", "Mercury", "Venus", "Earth", "Mars"], fontsize=20)

        self.event = Clock.schedule_interval(animate, 1/100)

        figure_canvas = FigureCanvas(self.fig)
        self.add_widget(figure_canvas)

        plt.close()

        button = Button(text='Go back', size_hint=(1/3, None), height=85, padding=(10, 10))
        button.bind(on_release=self.options_screen)
        self.add_widget(button)

        title_text = "Task 3: Animating 2D Elliptical Orbits - Inner Planets"
        title_widget = Label(text=title_text, font_size=60, padding=(10, 10), halign="center", valign='center')
        title_widget.pos = (0, 5*self.height/12)
        self.add_widget(title_widget)

    def create_screen_outer(self, instance):

        self.clear_widgets()

        anim_speed = 200

        def animate(i):

            years = round(1000 * self.counter * anim_speed / 360) / 1000

            data = loop(self.counter, anim_speed, self.file_planets)

            jupiter.set_data(data[5]['x'], data[5]['y'])
            jupiter.set_color(data[5]['colour'])

            saturn.set_data(data[6]['x'], data[6]['y'])
            saturn.set_color(data[6]['colour'])

            uranus.set_data(data[7]['x'], data[7]['y'])
            uranus.set_color(data[7]['colour'])

            neptune.set_data(data[8]['x'], data[8]['y'])
            neptune.set_color(data[8]['colour'])

            pluto.set_data(data[9]['x'], data[9]['y'])
            pluto.set_color(data[9]['colour'])

            self.counter += 1
            self.fig.canvas.draw()

            title.set_text(u"Years: {}".format(years))
            return jupiter, saturn, uranus, neptune, pluto, title

        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        plt.grid(True)
        plt.xlim(-40, 55)
        plt.ylim(-40, 40)
        self.ax.set_xlabel("X/AU")
        self.ax.set_ylabel("Y/AU")

        self.ax.plot(0, 0, 'o', markersize=15, color="yellow")

        title = self.ax.text(0.5, 0.97, "", bbox={'facecolor': 'w', 'alpha': 0.0, 'pad': 5},
                             transform=self.ax.transAxes, ha="center", fontsize=20)

        jupiter_data_x = []
        jupiter_data_y = []

        saturn_data_x = []
        saturn_data_y = []

        uranus_data_x = []
        uranus_data_y = []

        neptune_data_x = []
        neptune_data_y = []

        pluto_data_x = []
        pluto_data_y = []

        theta_jupiter = np.linspace(0, 2 * math.pi, 1000)
        jupiter, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][5], label='_nolegend_')
        r_jupiter, x_jupiter, y_jupiter = position(theta_jupiter, self.file_planets["a"][5],
                                                   self.file_planets["Epsilon"][5])
        self.ax.plot(x_jupiter, y_jupiter, color=self.file_planets["Colour"][5], linewidth=2,
                     label=self.file_planets["Object"][5])
        jupiter_data_x.append(x_jupiter[0])
        jupiter_data_y.append(y_jupiter[0])

        theta_saturn = np.linspace(0, 2 * math.pi, 1000)
        saturn, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][6], label='_nolegend_')
        r_saturn, x_saturn, y_saturn = position(theta_saturn, self.file_planets["a"][6],
                                                self.file_planets["Epsilon"][6])
        self.ax.plot(x_saturn, y_saturn, color=self.file_planets["Colour"][6], linewidth=2,
                     label=self.file_planets["Object"][6])
        saturn_data_x.append(x_saturn[0])
        saturn_data_y.append(y_saturn[0])

        theta_uranus = np.linspace(0, 2 * math.pi, 1000)
        uranus, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][7], label='_nolegend_')
        r_uranus, x_uranus, y_uranus = position(theta_uranus, self.file_planets["a"][7],
                                                self.file_planets["Epsilon"][7])
        self.ax.plot(x_uranus, y_uranus, color=self.file_planets["Colour"][7], linewidth=2,
                     label=self.file_planets["Object"][7])
        uranus_data_x.append(x_uranus[0])
        uranus_data_y.append(y_uranus[0])

        theta_neptune = np.linspace(0, 2 * math.pi, 1000)
        neptune, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][8], label='_nolegend_')
        r_neptune, x_neptune, y_neptune = position(theta_neptune, self.file_planets["a"][8],
                                                   self.file_planets["Epsilon"][8])
        self.ax.plot(x_neptune, y_neptune, color=self.file_planets["Colour"][8], linewidth=2,
                     label=self.file_planets["Object"][8])
        neptune_data_x.append(x_neptune[0])
        neptune_data_y.append(y_neptune[0])

        theta_pluto = np.linspace(0, 2 * math.pi, 1000)
        pluto, = self.ax.plot([], [], '.', markersize=20, color=self.file_planets["Colour"][9], label='_nolegend_')
        r_pluto, x_pluto, y_pluto = position(theta_pluto, self.file_planets["a"][9],
                                             self.file_planets["Epsilon"][9])
        self.ax.plot(x_pluto, y_pluto, color=self.file_planets["Colour"][9], linewidth=2,
                     label=self.file_planets["Object"][9])
        pluto_data_x.append(x_pluto[0])
        pluto_data_y.append(y_pluto[0])

        jupiter.set_data(jupiter_data_x, jupiter_data_y)
        saturn.set_data(saturn_data_x, saturn_data_y)
        uranus.set_data(uranus_data_x, uranus_data_y)
        neptune.set_data(neptune_data_x, neptune_data_y)
        pluto.set_data(pluto_data_x, pluto_data_y)

        plt.legend(labels=["Sun", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"], fontsize=20)

        self.event = Clock.schedule_interval(animate, 1 / 100)

        figure_canvas = FigureCanvas(self.fig)
        self.add_widget(figure_canvas)

        plt.close()

        button = Button(text='Go back', size_hint=(1/3, None), height=85, padding=(10, 10))
        button.bind(on_release=self.options_screen)
        self.add_widget(button)

        title_text = "Task 3: Animating 2D Elliptical Orbits - Outer Planets"
        title_widget = Label(text=title_text, font_size=60, padding=(10, 10), halign="center", valign='center')
        title_widget.pos = (0, 5 * self.height / 12)
        self.add_widget(title_widget)

    def options_screen(self, instance):
        self.clear_widgets()
        self.event.cancel()
        self.add_widget(TaskThreeScreen())

    def home_screen(self, instance):
        self.clear_widgets()
        self.add_widget(m.MainScreen())