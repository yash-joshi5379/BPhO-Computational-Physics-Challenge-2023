from kivy.uix.button import Button
from kivy.uix.image import Image
import pandas as pd
import matplotlib.pyplot as plt
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.utils import platform
import main as m
import numpy as np


class TaskOneScreen(RelativeLayout):

    def __init__(self, **kwargs):
        super(TaskOneScreen, self).__init__(**kwargs)
        self.file_planets = pd.read_excel("planets.xlsx")
        self.orientation = 'horizontal'
        if platform == 'android' or platform == 'ios':
            Window.maximize()
        else:
            Window.size = (1500, 540)
        self.create_screen()

    def create_screen(self):
        width, height = Window.system_size
        plt.style.use("default")
        x_axis = self.file_planets["a"] ** 1.5
        y_axis = self.file_planets["P"]
        plt.figure(figsize=(11, 8))
        gradient, intercept = np.polyfit(x_axis, y_axis, 1)
        plt.plot(x_axis, y_axis, marker='o', linestyle='-')
        equation_text = f"y = {gradient:.2f}x + {intercept*-1:.2f}"
        plt.text(102, 90, equation_text, fontsize=12, color='black')
        plt.xlabel('Distance from sun in AU')
        plt.ylabel('Orbital period in years')
        plt.title("Kepler's Third Law")
        plt.grid(True)
        plt.savefig('task1.png')
        plt.close()

        title_text = "Task 1: Proving Kepler's Third Law"
        title = Label(text=title_text, font_size=60, padding=(10, 10), halign="center", valign='center')
        title.pos = (0, 4*height/5)
        self.add_widget(title)

        image = Image(source='task1.png')
        image.pos = (-width/4, -height/6)
        self.add_widget(image)

        text = """As you can see, the
line of best fit to 2
decimal places has
a gradient of 1.00
and no y-intercept.

This means that the
distance from the sun
in AU to the power of
1.5 is equal to the
orbital period in years,
which proves Kepler's
Third Law."""
        label = Label(text=text, font_size=30, padding=(10, 10), halign='left', valign='middle')
        label.pos = (500, 0)
        self.add_widget(label)

        button = Button(text='Go back', padding=(10, 10), size_hint=(39/160, 1/40), halign="center", valign="middle")
        button.pos = (0, 0)
        button.bind(on_release=self.home_screen)
        self.add_widget(button)

    def home_screen(self, instance):
        self.clear_widgets()
        self.add_widget(m.MainScreen())