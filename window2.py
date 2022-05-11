from tkinter import *


class Window2(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.bold_font = ("Segoe UI", 9, 'bold')

        self.window_configuration()
        self.window2_frame()

    def window_configuration(self):
        self.geometry("475x520")
        self.resizable(width=False, height=False)
        self.title("window1")
        self["bg"] = "grey"

    def window2_frame(self):
        Frame(self, name="master_left").grid(column=0, row=0, pady=(10, 0), padx=(10, 10))
        master_left = self.nametowidget(".!window2.master_left")

        Frame(self, name="master_right").grid(column=1, row=0, pady=(10, 0))
        master_right = self.nametowidget(".!window2.master_right")

        setA_frame = LabelFrame(master_left, text="Set A")
        setA_frame.grid(column=0, row=0, pady=(10, 0))
        listbox_A = Listbox(setA_frame)
        listbox_A.pack()

        setB_frame = LabelFrame(master_right, text="Set B")
        setB_frame.grid(column=0, row=0, pady=(10, 0))
        listbox_B = Listbox(setB_frame)
        listbox_B.pack()

        with open("txt/set_A.txt", "r", encoding="utf-8") as file:
            self.set_A = file.readline()[4:].split(" ")
            listbox_A.insert(END, *self.set_A)

        with open("txt/set_B.txt", "r", encoding="utf-8") as file:
            self.set_B = file.readline()[4:].split(" ")
            listbox_B.insert(END, *self.set_B)

        S = [("Sophia", "Hudson"), ("Amelia", "Jayden"), ("Evelyn", "Daniel"), ("Aurora", "Thomas"),
             ("Amelia", "Sophia"), ("Evelyn", "Sophia"), ("Amelia", "Aurora"), ("Gianna", "Samuel")]
        self.women = self.matrixS(S)

        R = [("Hudson", "Julian"), ("Thomas", "Samuel"), ("Carter", "Joseph"), ("Evelyn", "Carter"),
             ("Carter", "Amelia")]
        self.men = self.matrixR(R)

    def matrix(self, frame, S):
        x, y = 0, 0
        set_ = []
        for m in self.set_B:
            for w in self.set_A:
                e = Entry(frame, width=3)
                if ((w, m) in S) or ((m, w) in S) :
                    flag = "  1"
                    set_.append((w, m))
                    e.config({"background": "#dedede"})
                else:
                    flag = "  0"
                e.insert(END, flag)
                e.place(x=10+x, y=10+y)
                x += 30
            y += 30
            frame["width"] += 30
            frame["height"] += 30
            x = 0
        return set_

    def matrixS(self, S):
        master = self.nametowidget(".!window2.master_left")
        Label(master, text="Матричне відношення S\n(a мати b)", font=self.bold_font).grid(pady=(5, 5))

        name_frame = Frame(master)
        name_frame.grid(padx=(10, 10), pady=(0, 10))

        for i, name in enumerate(self.set_A):
            Label(name_frame, text=name, wraplength=1).grid(row=0, column=i+1, sticky="s")
        for i, name in enumerate(self.set_B):
            Label(name_frame, text=name).grid(row=i+1, column=0, sticky="e")

        frame = Frame(name_frame, width=10, height=10)
        frame.grid(column=1, columnspan=5, row=1, rowspan=5)
        set_ = self.matrix(frame, S)

        return set_

    def matrixR(self, R):
        master = self.nametowidget(".!window2.master_right")
        Label(master, text="Матричне відношешння R\n(a онука b)", font=self.bold_font).grid(pady=(5, 5))

        name_frame = Frame(master)
        name_frame.grid(padx=(10, 10), pady=(0, 10))

        for i, name in enumerate(self.set_A):
            Label(name_frame, text=name, wraplength=1).grid(row=0, column=i+1, sticky="s")
        for i, name in enumerate(self.set_B):
            Label(name_frame, text=name).grid(row=i+1, column=len(self.set_B)+1, sticky="w")

        frame = Frame(name_frame, width=10, height=10)
        frame.grid(column=1, columnspan=5, row=1, rowspan=5)
        set_ = self.matrix(frame, R)

        return set_

    def return_sets(self):
        return (self.women, self.men)
