from tkinter import *


class Window1(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.flag = 0
        self.bold_font = ("Segoe UI", 9, 'bold')
        self.window_configuration()
        self.window1_frame()

    def window_configuration(self):
        self.geometry("400x350")
        self.resizable(width=False, height=False)
        self.title("window1")

    def flag0(self):
        self.flag = 0

    def flag1(self):
        self.flag = 1

    def save_A(self):
        with open('txt/set_A.txt', 'w', encoding='utf-8') as file:
            file.write(self.lbl_a['text'])

    def save_B(self):
        with open('txt/set_B.txt', 'w', encoding='utf-8') as file:
            file.write(self.lbl_b['text'])

    def women_frame(self):
        label_frame = self.nametowidget(".!window1.label_frame")

        women_frame = LabelFrame(label_frame, text="women")
        women_frame.grid(row=0, column=0, padx=(0, 60))
        scrollbar = Scrollbar(women_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        women = Listbox(women_frame, yscrollcommand=scrollbar.set, width = 20)
        names = ["Camila", "Sophia", "Amelia", "Isabel", "Evelyn", "Gianna", "Aurora", "Emilia"]
        for i, name in enumerate(names):
            women.insert(i, name)
        women.pack()
        return women

    def men_frame(self):
        label_frame = self.nametowidget(".!window1.label_frame")

        men_frame = LabelFrame(label_frame, text="men")
        men_frame.grid(row=0, column=1)
        scrollbar = Scrollbar(men_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        men = Listbox(men_frame, yscrollcommand=scrollbar.set, width = 20)
        names = ["Daniel", "Joseph", "Samuel", "Carter", "Julian", "Jayden", "Hudson", "Thomas"]
        for i, name in enumerate(names):
            men.insert(i, name)
        men.pack()
        return men

    def get_selected(self, women, men):
        name = men if women.curselection() == () else women
        if self.flag == 0:
            self.lbl_a['text'] += " " + name.get(ACTIVE)
        else:
            self.lbl_b['text'] += " " + name.get(ACTIVE)

    def window1_frame(self):
        label_frame = Frame(self, name = "label_frame")
        label_frame.pack(pady=(10, 0))

        men = self.men_frame()
        women = self.women_frame()

        Radiobutton(label_frame, text="A", value=1, font=self.bold_font, command=self.flag0).grid(column=0, row=2, sticky="w")
        Radiobutton(label_frame, text="B", value=0, font=self.bold_font, command=self.flag1).grid(column=0, row=3, sticky="w")

        self.lbl_a = Label(label_frame, text="A =")
        self.lbl_a.grid(column=0, columnspan=2, row=2, sticky="w", padx=(60, 0))
        self.lbl_b = Label(label_frame, text="B =")
        self.lbl_b.grid(column=0, columnspan=2, row=3, sticky="w", padx=(60, 0))

        param = {"master": label_frame, "width": 10, "height": 1, "text": ">>>>",
                 "command": lambda: self.get_selected(women, men)}
        Button(**param).grid(column=0, row=1, pady=(5, 20), padx=(0, 60))
        Button(**param).grid(column=1, row=1, pady=(5, 20))

        Button(label_frame, width=10, height=1, text="Save A", command=self.save_A)\
                                .grid(column=0, row=6, padx=(0, 60), pady=(15, 0))
        Button(label_frame, width=10, height=1, text="Save B", command=self.save_B)\
                                .grid(column=1, row=6, pady=(15, 0))
