# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey): 
    radius = 5 # used in this class only; never changes
    
    
    def __init__(self,x,y,speed,angle):
        Prey.__init__(self, x,y,10,10,angle,5)
        self._x       = x
        self._y       = y
        self._speed   = 5 #speed
        self._angle   = angle
        self._width = Ball.radius
        self._height = Ball.radius
        self._color   = 'blue'

    
    def update(self,model):
##        super().move()
##        super().wall_bounce()
        self.move()
        self.wall_bounce()
		
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius,self._y-Ball.radius,self._x+Ball.radius,\
                           self._y+Ball.radius,fill=self._color)
   
