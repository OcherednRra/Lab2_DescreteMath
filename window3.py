from tkinter import *
from itertools import permutations

class Window3(Toplevel):
    def __init__(self, parent, s):
        super().__init__(parent)
        set_S = set(s[0])
        set_R = set(s[1])

        names = ["Camila", "Sophia", "Amelia", "Isabel", "Evelyn", "Gianna", "Aurora", "Emilia",
                 "Daniel", "Joseph", "Samuel", "Carter", "Julian", "Jayden", "Hudson", "Thomas"]

        self.unionRandS = set_R | set_S
        self.andRandS = set_R & set_S
        self.RminusS = set_R - set_S
        self.UminusR = {r for r in set(permutations(names, 2)) if r not in set_R}

        s1, s2 = set(zip(*set_S))
        self.SminusOne = set(zip(s2, s1))

        with open("txt/set_A.txt", "r", encoding="utf-8") as file:
            self.set_A = file.readline()[4:].split(" ")

        with open("txt/set_B.txt", "r", encoding="utf-8") as file:
            self.set_B = file.readline()[4:].split(" ")

        self.window_configuration()
        self.window3_frame()

    def window_configuration(self):
        self.geometry("400x335")
        self.resizable(width=False, height=False)
        self.title("window3")
        self['bg'] = 'grey'

    def empty_matrix(self):
        frame = self.nametowidget(".!window3.result_frame")
        Frame(frame, name="matrix_frame").grid(padx=(10, 10), pady=(0, 10))

        frame = self.nametowidget(".!window3.result_frame.matrix_frame")
        for i, name in enumerate(self.set_A):
            Label(frame, text=name, wraplength=1).grid(row=0, column=i + 1, sticky="s")
        for i, name in enumerate(self.set_B):
            Label(frame, text=name).grid(row=i + 1, column=0, sticky="e")

        entries_frame = Frame(frame, name="entries_frame", width=10, height=10)
        entries_frame.grid(column=1, columnspan=5, row=1, rowspan=5)

        x, y = 0, 0
        for i in self.set_B:
            for j in self.set_A:
                entry = Entry(entries_frame, width=3)
                entry.insert(END, "  0")
                entry.place(x=10+x, y=10+y)
                x += 30
            y += 30
            entries_frame["width"] += 30
            entries_frame["height"] += 30
            x = 0

    def matrix(self, text, K):
        self.nametowidget(".!window3.result_frame.matrix_frame.entries_frame").grid_remove()
        self.nametowidget('.!window3.result_frame.action_title')["text"] = text

        frame = self.nametowidget(".!window3.result_frame.matrix_frame")
        for i, name in enumerate(self.set_A):
            Label(frame, text=name, wraplength=1).grid(row=0, column=i + 1, sticky="s")
        for i, name in enumerate(self.set_B):
            Label(frame, text=name).grid(row=i + 1, column=0, sticky="e")

        entries_frame = Frame(frame, name="entries_frame", width=10, height=10)
        entries_frame.grid(column=1, columnspan=5, row=1, rowspan=5)

        x, y = 0, 0
        for i in self.set_B:
            for j in self.set_A:
                e = Entry(entries_frame, width=3)
                if text == "U\R":
                    if (j, i) in K:
                        flag = "  1"
                        e.config({"background": "#dedede"})
                elif ((i, j) in K) or ((j, i) in K):
                        flag = "  1"
                        e.config({"background": "#dedede"})
                else:
                    flag = "  0"

                e.insert(END, flag)
                e.place(x=10 + x, y=10 + y)
                x += 30
            y += 30
            entries_frame["width"] += 30
            entries_frame["height"] += 30
            x = 0

    def buttons(self):
        frame = self.nametowidget(".!window3.buttons_frame")

        Button(frame, width=10, text="R∪S", command=lambda: self.matrix("R∪S", self.unionRandS)).pack(pady=19)
        Button(frame, width=10, text="R⋂S", command=lambda: self.matrix("R⋂S", self.andRandS)).pack(pady=19)
        Button(frame, width=10, text="R\S", command=lambda: self.matrix("R\S", self.RminusS)).pack(pady=19)
        Button(frame, width=10, text="U\R", command=lambda: self.matrix("U\R", self.UminusR)).pack(pady=19)
        Button(frame, width=10, text="S^-1", command=lambda: self.matrix("S^-1", self.SminusOne)).pack(pady=19)

    def window3_frame(self):
        Frame(self, name="buttons_frame").grid(column=0, row=0, ipadx=20, padx=(5, 5), pady=(5, 5), sticky="sn")
        Frame(self, name="result_frame").grid(column=1, row=0)

        self.buttons()

        frame = self.nametowidget(".!window3.result_frame")
        Label(frame, text="Операція над співвідношеннями", font=("Segoe UI", 11, 'bold')).grid(padx=(10, 10))
        Label(frame, name="action_title", font=("Segoe UI", 11), fg="red").grid(pady=(10, 10))

        self.empty_matrix()
