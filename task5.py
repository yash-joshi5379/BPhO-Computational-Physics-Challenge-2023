import numpy as np
import pandas as pd
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import main as m


def calculate_times(period):
    times = [0.1]
    upper = int(period*30) + 1
    for i in range(2, upper):
        times.append(i * 0.1)
    return times


def angle_vs_time(times, period, ecc):
    theta0 = 0
    d_theta = 1 / 1000
    num = np.ceil(times[-1] / period)
    theta = np.arange(theta0, 2*np.pi*num + theta0 + d_theta, d_theta)
    integrand = (1 - ecc * np.cos(theta))**(-2)
    length = len(theta)
    c = np.full(length, 2)
    c[1::2] = 4
    c[0] = c[-1] = 1
    dt = period * ((1 - ecc**2)**(3/2)) * (1 / (2 * np.pi)) * d_theta * 1/3
    tt = np.cumsum(c * integrand) * dt
    theta_interp = interp1d(tt, theta, kind='cubic')
    theta = theta_interp(times)
    return theta


class TaskFiveScreen(RelativeLayout):

    def __init__(self, **kwargs):
        super(TaskFiveScreen, self).__init__(**kwargs)
        self.file_planets = pd.read_excel("planets.xlsx")
        self.orientation = 'horizontal'
        self.create_screen()

    def create_screen(self):

        plt.style.use("default")

        width, height = Window.system_size
        period = self.file_planets["P"][9]
        eps = self.file_planets["Epsilon"][9]
        times = calculate_times(period)
        theta = angle_vs_time(times, period, eps)
        theta2 = angle_vs_time(times, period, 0)
        plt.figure(figsize=(11, 8))
        plt.plot(times, theta, color="green", label="Circular, ε=0")
        plt.plot(times, theta2, label="Pluto, ε=0.25")
        plt.grid(True)
        plt.xlabel('time /years', fontsize=12)
        plt.ylabel('orbital polar angle /rad', fontsize=12)
        plt.title("Orbital Angle vs Time for Pluto", fontsize=20)
        plt.legend(fontsize=20)
        plt.grid(True)
        plt.savefig('task5.png')
        plt.close()

        title_text = "Task 5: Plotting Orbital Angle against Time for Pluto"
        title = Label(text=title_text, font_size=60, padding=(10, 10), halign='center', valign='middle')
        title.pos = (0, 4*height/5)
        self.add_widget(title)

        image = Image(source='task5.png')
        image.pos = (-width/4, -height/6)
        self.add_widget(image)

        text = """Using Simpson's
Integration method,
you can plot a graph
of polar angle against
orbital time.

The straight line
represents a planet
with the same radius
as pluto, but with no
eccentricity, and the
other line represents
pluto."""

        label = Label(text=text, font_size=30, padding=(10, 10), halign='left', valign='middle')
        label.pos = (3 * width / 4, height / 10)
        self.add_widget(label)

        button = Button(text='Go back', padding=(10, 10), size_hint=(39/160, 1/4), halign="center", valign="middle")
        button.pos = (3 * width / 2, height / 45)
        button.bind(on_release=self.home_screen)
        self.add_widget(button)

    def home_screen(self, instance):
        self.clear_widgets()
        self.add_widget(m.MainScreen())