from pybricks.hubs import EV3Brick
from pybricks.parameters import Button


class Screen:

    def __init__(self):
        self.screen = 0
        
    def basic_screen(self):
        screen.draw_text(0, 90, "↑")
        screen.draw_text(90, 0, "→")
        screen.draw_text(0, -90, "↓")
        screen.draw_text(-90, 0, "←")

    def first_screen(self):
        screen.draw_text(0, 110, "run 1")
        screen.draw_text(110, 0, "run 2")
        screen.draw_text(0, -110, "run 3")
        screen.draw_text(-110, 0, "run 4")
        
    def second_screen(self):
        screen.draw_text(0, 110, "run 1")
        screen.draw_text(110, 0, "run 2")
        screen.draw_text(0, -110, "run 3")
        screen.draw_text(-110, 0, "run 4")
        
    
    def change_screen(self):
        scren.clear
        choice = self.screen % 2
        if choice == 0:
            self.screen_0()
        else:
            self.screen_1()
