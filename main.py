from tkinter import *

from student_info_window import StudentInfoWindow
from window1 import Window1
from window2 import Window2
from window3 import Window3


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.bold9 = ("Segoe UI", 9, 'bold')
        self.bold10 = ("Segoe UI", 10, 'bold')

        self.window_configuration()
        self.main_frame()

    def window_configuration(self):
        self.geometry('400x240')
        self.resizable(width=False, height=False)
        self.title('Лабораторна робота №2')
        self["bg"] = "grey"

    def main_frame(self):
        Frame(self, name="option_description").pack(fill=X, pady=(10, 0))

        self.about_student_button()
        self.describe_option()

        buttons_frame = Frame(self)
        buttons_frame.pack(fill=X, pady=(10, 0))

        param = {"master": buttons_frame, "width": 12, "height": 1, "fg": "#d9073d",
                 "relief": "raised", "activebackground": "grey", "font": self.bold9}
        Button(**param, text="1", command=self.open_window1).pack(padx=20, pady=10, side=LEFT)
        Button(**param, text="2", command=self.open_window2).pack(padx=20, pady=10, side=LEFT)
        Button(**param, text="3", command=self.open_window3).pack(padx=20, pady=10, side=LEFT)

    def describe_option(self):
        master = Frame(self.nametowidget(".option_description"))
        master.pack(pady=(0, 30))

        Label(master, text="Опис варіанту", font=self.bold10).grid(row=0, columnspan=2)

        Label(master, text="Відношення 1: ", font=self.bold10).grid(column=0, row=1)
        Label(master, text="aSb, якщо а мати b").grid(column=1, row=1)

        Label(master, text="Відношення 2: ", font=self.bold10).grid(column=0, row=2)
        Label(master, text="aRb, якщо а онука b").grid(column=1, row=2)

    def about_student_button(self):
        master = self.nametowidget(".option_description")
        Button(master, width=18, height=1, fg='#d9073d', relief="raised",
                  text='!  Інформація  !', activebackground='grey', font=self.bold10,
                  command=self.open_student_info_window).pack(pady=(10, 20))

    def open_student_info_window(self):
        student_info_window = StudentInfoWindow(self)
        student_info_window.grab_set()

    def open_window1(self):
        open_window_1 = Window1(self)
        open_window_1.grab_set()

    def open_window2(self):
        open_window_2 = Window2(self)
        self.s = open_window_2.return_sets()
        open_window_2.grab_set()

    def open_window3(self):
        open_window_3 = Window3(self, self.s)
        open_window_3.grab_set()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
