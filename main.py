from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.utils import platform
import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4
import task5 as t5
import task6 as t6
import task7 as t7


class MainScreen(RelativeLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        if platform == 'android' or platform == 'ios':
            Window.maximize()
        else:
            Window.size = (1120, 540)
        self.create_initial_buttons()

    def create_initial_buttons(self):

        width, height = Window.system_size

        button1_text = """Task 1:
Proving
Kepler's
Third Law"""
        button1 = Button(text=button1_text, size_hint=(1/8, 2/3), halign="center", valign="middle")
        button1.bind(on_release=self.task_1)
        button1.pos = (0, 0)
        self.add_widget(button1)

        button2_text = """Task 2:
Plotting 2D
Elliptical
Orbits"""
        button2 = Button(text=button2_text, size_hint=(1/8, 2/3), halign="center", valign="middle")
        button2.bind(on_release=self.task_2)
        button2.pos = (2*width/8, 0)
        self.add_widget(button2)

        button3_text = """Task 3:
Animating 2D
Elliptical
Orbits"""
        button3 = Button(text=button3_text, size_hint=(1/8, 2/3), halign="center", valign="middle")
        button3.bind(on_release=self.task_3)
        button3.pos = (4*width/8, 0)
        self.add_widget(button3)

        button4_text = """Task 4:
Animating 3D
Elliptical
Orbits"""
        button4 = Button(text=button4_text, size_hint=(1/8, 2/3), halign="center", valign="middle")
        button4.bind(on_release=self.task_4)
        button4.pos = (6*width/8, 0)
        self.add_widget(button4)

        button5_text = """Task 5:
Plotting Polar
Angle Against
Orbital Time
for Pluto"""
        button5 = Button(text=button5_text, size_hint=(1/8, 2/3), halign="center", valign="middle")
        button5.bind(on_release=self.task_5)
        button5.pos = (8*width/8, 0)
        self.add_widget(button5)

        button6_text = """Task 6:
Creating
Spirographs"""
        button6 = Button(text=button6_text, size_hint=(1/8, 2/3), halign="center", valign="middle")
        button6.bind(on_release=self.task_6)
        button6.pos = (10*width/8, 0)
        self.add_widget(button6)

        button7_text = """Task 7:
Animating 2D
and 3D
Elliptical Orbits
Relative to
Planets"""
        button7 = Button(text=button7_text, size_hint=(1/8, 2/3), halign="center", valign="middle")
        button7.bind(on_release=self.task_7)
        button7.pos = (12*width/8, 0)
        self.add_widget(button7)

        title_text = """Anton Lewis and Yash Joshi Computational Physics
Submission 2023"""
        title = Label(text=title_text, font_size=60, padding=(10, 10), halign='center', valign='middle')
        title.pos = (0, 3*height/4)
        self.add_widget(title)

        label_text = "Welcome! Please choose a task number below:"
        label = Label(text=label_text, font_size=35, padding=(10, 10), halign='center', valign='middle')
        label.pos = (0, height/2)
        self.add_widget(label)

    def task_1(self, instance):
        self.clear_widgets()
        self.add_widget(t1.TaskOneScreen())

    def task_2(self, instance):
        self.clear_widgets()
        self.add_widget(t2.TaskTwoScreen())

    def task_3(self, instance):
        self.clear_widgets()
        self.add_widget(t3.TaskThreeScreen())

    def task_4(self, instance):
        self.clear_widgets()
        self.add_widget(t4.TaskFourScreen())

    def task_5(self, instance):
        self.clear_widgets()
        self.add_widget(t5.TaskFiveScreen())

    def task_6(self, instance):
        self.clear_widgets()
        self.add_widget(t6.TaskSixScreen())

    def task_7(self, instance):
        self.clear_widgets()
        self.add_widget(t7.TaskSevenScreen())


class MyApp(App):
    def build(self):
        self.title = "Anton and Yash Computational Physics Submission"
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()