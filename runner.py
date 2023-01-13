# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage



from prey import Prey
from blackhole import Black_Hole
from random import random
import math


class Runner(Prey): 
    radius = 5 # used in this class only; might changes
    #color = 'red'
    
    def __init__(self,x,y,speed,angle):
        Prey.__init__(self, x,y,10,10,angle,5)
        self._x       = x
        self._y       = y
        self._speed   = 5 #speed
        self._angle   = angle
        self._width = Runner.radius
        self._height = Runner.radius
        self._color   = 'green'

    
    def update(self,model):
        ans = model.find(lambda x:isinstance(x,Black_Hole))
        sub = ans.copy()
        tar_list = []
        beTraped = False
        for p in sub:                      
            p_dist = self.distance(p.get_location())
            if p_dist < 100:
                tar_list.append([p, p_dist])
            
        if len(tar_list) > 0:   #something within 100 
            tar=sorted(tar_list, key=lambda x:x[1])[0]
            tar_loc=tar[0].get_location()
            if self.distance(tar_loc) < 20: self._speed = 10
            new_angle = math.atan2(tar_loc[1] - self._y, tar_loc[0]-self._x)
            if abs(new_angle - self._angle) <= math.pi*1/6: #keep some margin
                beTraped = True
            else:
                beTraped = False
            self._angle = new_angle + math.pi
        else: #coast is clear
            self._speed = 5
            beTraped = False
            if random()<=0.3: #30% chance for speed and angle change
                self._angle +=random() - 0.5

        if beTraped: self._angle += (random() - 0.5) * math.pi            
        self.move()        

        
		
    def display(self,canvas):
        canvas.create_oval(self._x-Runner.radius,self._y-Runner.radius,self._x+Runner.radius,\
                           self._y+Runner.radius,fill=self._color)
