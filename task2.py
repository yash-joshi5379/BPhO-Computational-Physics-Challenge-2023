from kivy.uix.button import Button
from kivy.uix.image import Image
import pandas as pd
import matplotlib.pyplot as plt
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
import main as m
import numpy as np


class TaskTwoScreen(RelativeLayout):

    def __init__(self, **kwargs):
        super(TaskTwoScreen, self).__init__(**kwargs)
        self.file_planets = pd.read_excel("planets.xlsx")
        self.orientation = 'horizontal'
        self.create_screen()

    def create_screen(self):
        plt.style.use("dark_background")
        width, height = Window.system_size
        cos = np.cos
        sin = np.sin
        pi = np.pi
        theta = np.linspace(0, 2*pi, 360)

        temp_filtered_data = self.file_planets[self.file_planets["PlanetNum"] > 0]
        filtered_data_a = temp_filtered_data[temp_filtered_data["PlanetNum"] < 5]
        plt.figure(figsize=(8, 8))
        plt.plot(0, 0, marker='o', markersize='15', color="yellow")
        for index, row in filtered_data_a.iterrows():
            a = row["a"]
            e = row["Epsilon"]
            r = (a*(1-e**2)) / (1 - e*cos(theta))
            x_axis = r * cos(theta)
            y_axis = r * sin(theta)
            plt.plot(x_axis, y_axis, color=row["Colour"])
        plt.legend(labels=["Sun", "Mercury", "Venus", "Earth", "Mars"])
        plt.xlabel("x/AU")
        plt.ylabel("y/AU")
        plt.grid(True)
        plt.gca().set_aspect('equal')
        plt.savefig("task2a.png")
        plt.close()

        filtered_data_b = self.file_planets[self.file_planets["PlanetNum"] > 4]
        plt.figure(figsize=(8, 8))
        plt.plot(0, 0, marker='o', markersize='15', color="yellow")
        for index, row in filtered_data_b.iterrows():
            a = row["a"]
            e = row["Epsilon"]
            r = (a * (1 - e ** 2)) / (1 - e * cos(theta))
            x_axis = r * cos(theta)
            y_axis = r * sin(theta)
            plt.plot(x_axis, y_axis, color=row["Colour"])
        plt.legend(labels=["Sun", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"])
        plt.xlabel("x/AU")
        plt.ylabel("y/AU")
        plt.grid(True)
        plt.gca().set_aspect('equal')
        plt.savefig("task2b.png")
        plt.close()

        title_text = "Task 2: Plotting 2D Elliptical Orbits"
        title = Label(text=title_text, font_size=50, padding=(10, 10), halign="center", valign="center")
        title.pos = (-47*width/100, 4*height/5)
        self.add_widget(title)

        image1 = Image(source='task2a.png')
        image1.pos = (-width/2, -height/6)
        self.add_widget(image1)

        image2 = Image(source='task2b.png')
        image2.pos = (width/2, -height/6)
        self.add_widget(image2)

        label_text = """The left image shows the orbits of the inner 4 planets, and the
right image shows the orbits of the outer 5 planets."""
        label = Label(text=label_text, font_size=25, padding=(10, 10), halign="left", valign="center")
        label.pos = (-width/2, 3*height/5)
        self.add_widget(label)

        button = Button(text='Go back', size_hint=(5/12, 1/6), padding=(10, 10))
        button.bind(on_release=self.home_screen)
        button.pos = (11*width/10, 37*height/24)
        self.add_widget(button)

    def home_screen(self, instance):
        self.clear_widgets()
        self.add_widget(m.MainScreen())