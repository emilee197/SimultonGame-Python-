# The Black_Hole class is derived from Simulton. It updates by finding/removing
#   any class derived from Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton): #Prey
    radius = 10 # used in this class only; never changes
    color = 'black'
    
    def __init__(self,x,y,w,h):
        Simulton.__init__(self, x,y,Black_Hole.radius*2,Black_Hole.radius*2)
        self._x       = x
        self._y       = y
        #self._speed   = speed
        #self._angle   = angle
        self._width = Black_Hole.radius
        self._height = Black_Hole.radius
        self._radius = Black_Hole.radius
        #self._color   = color

    
    def update(self,model):
        ans = model.find(lambda x:isinstance(x,Prey))
        sub = ans.copy()
        for p in sub:
            if not self.contains(p.get_location()): ans.remove(p)
        return ans
        
##        ans = model.find(self.contains)
##        new_set = set()
##        for s in ans:
##            if isinstance(s, Prey): new_set.update({s})
##        return new_set

                

		
    def display(self,canvas):
        canvas.create_oval(self._x-Black_Hole.radius,self._y-Black_Hole.radius,\
                           self._x+Black_Hole.radius,self._y+Black_Hole.radius,fill=Black_Hole.color)

    def __contains__(self,xy):
        return self.distance(xy) <= self._radius
