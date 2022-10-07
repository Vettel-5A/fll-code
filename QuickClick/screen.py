from pybricks.hubs import EV3Brick
from pybricks.parameters import Button


class Screen:

    def __init__(self):
        self.screen = 0
        self.ev3 = EV3Brick()
        
        
    def basic_screen(self):
        ev3.screen.draw_text(0, 90, "↑")
        ev3.screen.draw_text(90, 0, "→")
        ev3.screen.draw_text(0, -90, "↓")
        ev3.screen.draw_text(-90, 0, "←")

    def first_screen(self):
        ev3.screen.draw_text(0, 110, "run 1")
        ev3.screen.draw_text(110, 0, "run 2")
        ev3.screen.draw_text(0, -110, "run 3")
        ev3.screen.draw_text(-110, 0, "run 4")
        
    def second_screen(self):
        ev3.screen.draw_text(0, 110, "run 1")
        ev3.screen.draw_text(110, 0, "run 2")
        ev3.screen.draw_text(0, -110, "run 3")
        ev3.screen.draw_text(-110, 0, "run 4")
        
    
    def change_screen(self):
        ev3.screen.clear()
        self.basic_screen()
        self.screen += 1
        if self.screen % 2 == 0:
            self.first_screen()

        else:
            self.second_screen()
