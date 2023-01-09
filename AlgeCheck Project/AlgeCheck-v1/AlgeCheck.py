import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math
from math import *
import numpy as np
from numpy import *


class AlgebraCheckerApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        tk.Tk.wm_title(self, "AlgeCheck")
        tk.Tk.configure(self, background='red')
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for Page in (StartPage, quadE_page, longDiv):
            frame = Page(container, self)

            self.frames[Page] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Tk.configure(self, background='light blue')

        page_title = tk.Label(self, text="x²  AlgeCheck  x²", font='Elephant 34 ', bg = 'blue')
        page_title.pack()

        choose_label = tk.Label(self, text="Choose the topic you are working on:",
                                font='none 12  bold underline', bg = 'light blue')
        choose_label.pack()

        quadE_button = tk.Button(self, text="Quadratic Equations", bg = 'dark cyan', height = 2,
                                 command= lambda:controller.show_frame(quadE_page))
        quadE_button.pack()

        longDiv_button = tk.Button(self, text="Long Division", bg = 'dark cyan', height = 2,
                                 command= lambda:controller.show_frame(longDiv))
        longDiv_button.pack()


class quadE_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Tk.configure(self, background='light blue')
        self.coe_a=DoubleVar()
        self.coe_b=DoubleVar()
        self.coe_c=DoubleVar()

        def InputCheck(input):
            if input.isdigit():
                return True
            else:
                lambda: tk.messagebox.showinfo("Error", "Please input numbers")


        Title =  tk.Label(self, text="x²  AlgeCheck  x²", font='Elephant 34 ', bg = 'blue').grid(row=0, columnspan=7)
        homeButton = tk.Button(self, text="Back to Main Menu", bg= 'red', height = 3,
                                 command= lambda:controller.show_frame(StartPage))
        homeButton.grid(row=0, column=7)

        Label(self, text="Quadratic Equations", font='none 18 bold underline', bg= 'light blue').grid(row=1, column = 3, sticky = N)
        Label(self, text="Input each coeffiecient:", font='none 12 bold underline', bg= 'light blue').grid(row=2,)
        A = Entry(self, textvariable=self.coe_a)
        A.grid(row=3, column=0 )
        Label(Label(self, text="x²",font='none 15 bold',bg= 'light blue').grid(row=3, column=1))
        B = Entry(self, textvariable=self.coe_b)
        B.grid(row=3, column=3)
        Label(Label(self, text="x",font='none 15 bold', bg= 'light blue').grid(row=3, column=4,))
        C = Entry(self, textvariable=self.coe_c)
        C.grid(row=3, column=6 )

        reg = self.register(InputCheck)
        A.config(validate="key", validatecommand=(reg, '%P'))
        B.config(validate="key", validatecommand=(reg, '%P'))
        C.config(validate="key", validatecommand=(reg, '%P'))
        solveButton = tk.Button(self, text="Solve", bg= 'green',  height = 2, width = 5, command=lambda: self.Quadratic()).grid(row=5, column=3, sticky = S)



    def Quadratic(self):
        a = self.coe_a.get()
        b = self.coe_b.get()
        c = self.coe_c.get()

        discriminant = (b**2)-(4*a*c)

        if discriminant < 0:
            print("There are no solutions")
            self.result = Label(self, text = "There are no solutons", font = "none 13 bold italic").grid(row=7, columnspan = 4)
        elif discriminant == 0:
            first_solution = ((-1*(b))+math.sqrt(discriminant))/2*a
            print(first_solution)
            self.result = Label(self, text = " x = {0}".format(first_solution), font = "none 13 bold italic").grid(row= 7, columnspan = 4)
        else:
            first_solution = ((-1*(b))+math.sqrt(discriminant))/2*a
            sec_solution = ((-1*(b))-math.sqrt(discriminant))/2*a
            print(first_solution)
            print(sec_solution)
            self.result = Label(self, text = "x = {0} or x = {1}" .format(first_solution, sec_solution),
                                font = "none 13 bold italic").grid(row=7, columnspan = 4)

class longDiv(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Tk.configure(self, background='light blue')
        Title =  Title =  tk.Label(self, text="x²  AlgeCheck  x²", font='Elephant 34 ', bg = 'blue').grid(row=0, columnspan=5)
        homeButton = tk.Button(self, text="Back to Main Menu", bg= 'red', height = 3,
                                 command= lambda:controller.show_frame(StartPage))
        homeButton.grid(row=0, column=6)

        self.coe_a1=DoubleVar()
        self.coe_b1=DoubleVar()
        self.coe_c1=DoubleVar()
        self.coe_d1=DoubleVar()
        self.coe_a2=DoubleVar()
        self.coe_b2=DoubleVar()
        self.coe_c2=DoubleVar()


        Label(self, text="Input each coeffiecient:", font='none 12 bold underline', bg= 'light blue').grid(row=1, )
        A1 = Entry(self, textvariable=self.coe_a1)
        A1.grid(row=2, column=0 )
        Label(Label(self, text="x³",font='none 15 bold', bg= 'light blue').grid(row=2, column=1 ))
        B1 = Entry(self, textvariable=self.coe_b1)
        B1.grid(row=2, column=2)
        Label(Label(self, text="x²",font='none 15 bold', bg= 'light blue').grid(row=2, column=3 ))
        C1 = Entry(self, textvariable=self.coe_c1)
        C1.grid(row=2, column=4 )
        Label(Label(self, text="x",font='none 15 bold', bg= 'light blue').grid(row=2, column=5 ))
        D1 = Entry(self, textvariable=self.coe_d1)
        D1.grid(row=2, column=6 )

        Label(self, text = "____________________________________________________", font='none 15 bold', bg= 'light blue').grid(row=3, columnspan=7)

        A2 = Entry(self, textvariable=self.coe_a2)
        A2.grid(row=4, column=0)
        Label(Label(self, text="x²",font='none 15 bold', bg= 'light blue').grid(row=4, column=1 ))
        B2 = Entry(self, textvariable=self.coe_b2)
        B2.grid(row=4, column=2)
        Label(Label(self, text="x",font='none 15 bold', bg= 'light blue').grid(row=4, column=3 ))
        C2 = Entry(self, textvariable=self.coe_c2)
        C2.grid(row=4, column=4 )

        solveButton = tk.Button(self, text="Solve", bg= 'green', height = 2, command=lambda: self.poly_Div()).grid(row=5, column = 3)


    def poly_Div(self):
        a1 = float(self.coe_a1.get())
        b1 = float(self.coe_b1.get())
        c1 = float(self.coe_c1.get())
        d1 = float(self.coe_d1.get())
        a2 = float(self.coe_a2.get())
        b2 = float(self.coe_b2.get())
        c2 = float(self.coe_c2.get())

        x = np.array([a1, b1, c1, d1])
        y = np.array([a2, b2, c2])
        div_calc = np.polydiv(x, y)
        print(div_calc)
        self.result = Label(self, text = "{}".format(div_calc),
                    font = "none 13 bold italic").grid(row=6, columnspan = 7)
        self.key = Label(self, text = "KEY: array[a,b]), array([c,d]) = ax+b, remainder cx+d",
                    font = "none 12 italic").grid(row = 7, columnspan = 7, sticky = S)






app = AlgebraCheckerApp()
app.mainloop()

