#-------------------------------------------------------------------------------
# Name:        AlgeCheck_reload
# Purpose:     App used for a user to check mathematic calculations like 
#              quadratic equations, deffirentiation etc. A level project re-done 
#              in kivy.
#
# Author:      Dzidula Keteku
#
# Created:     
#-------------------------------------------------------------------------------

from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from math import *
import numpy as np
from numpy import *


class Home(Screen):
    pass

class Quad_Eq(Screen):
    a_quad = ObjectProperty(None)
    b_quad = ObjectProperty(None)
    c_quad = ObjectProperty(None)
    quad_result = ObjectProperty(None)

    def quadratic(self):
        a = float(self.a_quad.text)
        b = float(self.b_quad.text)
        c = float(self.c_quad.text)
        discriminant = (b**2)-(4*a*c)

        if discriminant < 0:
            self.quad_result.text = f'There are no solutions'
        elif discriminant == 0:
            first_solution = ((-1*(b))+math.sqrt(discriminant))/2*a
            self.quad_result.text = f' x = {first_solution}'
        else:
            first_solution = ((-1*(b))+math.sqrt(discriminant))/2*a
            sec_solution = ((-1*(b))-math.sqrt(discriminant))/2*a

            self.quad_result.text = f'x = {first_solution} or x = {sec_solution}'

        self.a_quad.text = ""
        self.b_quad.text = ""
        self.c_quad.text = ""

    def page_reset(self):
        self.a_quad.text = ""
        self.b_quad.text = ""
        self.c_quad.text = ""
        self.quad_result.text = ""

class Long_Div(Screen):
    coe_a1 = ObjectProperty(None)
    coe_b1 = ObjectProperty(None)
    coe_c1 = ObjectProperty(None)
    coe_d1 = ObjectProperty(None)
    coe_a2 = ObjectProperty(None)
    coe_b2 = ObjectProperty(None)
    coe_c2 = ObjectProperty(None)
    long_result = ObjectProperty(None)
    long_remainder = ObjectProperty(None)

    def poly_div(self):
        a1 = float(self.coe_a1.text)
        b1 = float(self.coe_b1.text)
        c1 = float(self.coe_c1.text)
        d1 = float(self.coe_d1.text)
        a2 = float(self.coe_a2.text)
        b2 = float(self.coe_b2.text)
        c2 = float(self.coe_c2.text)

        x = np.array([a1, b1, c1, d1])
        y = np.array([a2, b2, c2])
        div_calc = np.polydiv(x, y)
        long_result = div_calc[0]
        long_remainder = div_calc[1]

        if long_result[1] == 0:
            real_res = "Ans: {}x".format(long_result[0])
        elif long_result[1] < 0:
            real_res = "Ans: {}x {}".format(long_result[0], long_result[1])
        else:
            real_res = "Ans: {}x+{}".format(long_result[0], long_result[1])

        if len(long_remainder) < 2:
            rem = "Remainder: {}x".format(long_remainder[0])
        elif long_remainder[1] < 0:
            rem = "Remainder: {}x {}".format(long_remainder[0], long_remainder[1])
        else:
            rem = "Remainder: {}x+{}".format(long_remainder[0], long_remainder[1])

        self.long_result.text = f'{real_res}'
        self.long_remainder.text = f'{rem}'

        self.coe_a1.text = ""
        self.coe_b1.text = ""
        self.coe_c1.text = ""
        self.coe_d1.text = ""
        self.coe_a2.text = ""
        self.coe_b2.text = ""
        self.coe_c2.text = ""

    def page_reset(self):
        self.coe_a1.text = ""
        self.coe_b1.text = ""
        self.coe_c1.text = ""
        self.coe_d1.text = ""
        self.coe_a2.text = ""
        self.coe_b2.text = ""
        self.coe_c2.text = ""
        self.long_result.text = ""
        self.long_remainder.text = ""

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('AlgeWindows.kv')

class AlgeCheckApp(App):
    def build(self):
        Window.clearcolor = (64/255, 255, 174/255, 1)
        Window.size = (700, 600)
        return kv

if __name__ == "__main__":
    AlgeCheckApp().run()

