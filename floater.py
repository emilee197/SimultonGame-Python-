# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5 # used in this class only; might changes
    #color = 'red'
    
    def __init__(self,x,y,speed,angle):
        Prey.__init__(self, x,y,10,10,angle,5)
        self._x       = x
        self._y       = y
        self._speed   = 5 #speed
        self._angle   = angle
        self._width = Floater.radius
        self._height = Floater.radius
        self._color   = 'red'

    
    def update(self,model): 
        if random()<=0.3: #30% chance for speed and angle change
            new_speed = self._speed + random() - 0.5
            if new_speed < 3: self._speed = 3
            elif new_speed > 7: self._speed = 7
            else: self._speed = new_speed             
            self._angle +=random() - 0.5

        self.move()
        self.wall_bounce()
		
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius,self._y-Floater.radius,self._x+Floater.radius,\
                           self._y+Floater.radius,fill=self._color)
