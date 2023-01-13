# The Hunter class is derived from Pulsator (1st) and the Mobile_Simulton (2nd).
#   It updates/displays like its Pulsator base, but also moves (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton): 
    update_counter = 0
    radius = 10
    def __init__(self,x,y,w,h,speed,angle):
        Pulsator.__init__(self, x,y,Hunter.radius*2,Hunter.radius*2)
        self._x       = x
        self._y       = y
        self._speed   = 5 #speed
        self._angle   = angle
        self._width = Hunter.radius
        self._height = Hunter.radius
        self._radius = Hunter.radius
        self._update_counter = 0
        #self._color   = color
    
    def update(self,model):
        ans = model.find(lambda x:isinstance(x,Prey))
        sub = ans.copy()
        tar_list = [] 
        for p in sub:
            p_dist = self.distance(p.get_location())
            if p_dist < 200:
                tar_list.append([p, p_dist])
            if not self.contains(p.get_location()): ans.remove(p)
        if len(tar_list) > 0:    
            tar=sorted(tar_list, key=lambda x:x[1])[0]
            tar_loc=tar[0].get_location()
            #print('find target:', tar, tar_loc)
            #print('my position:', self._x, self._y)
            new_angle = atan2(tar_loc[1] - self._y, tar_loc[0]-self._x)                
            self._angle = new_angle
        self.move()

        self._update_counter +=1                                        
        if len(ans) > 0: #eat something
            #print('update counter:', self._update_counter)
            self._width += 1
            self._height +=1
            self._radius = self._width
            self._update_counter = 0
        else:
            if self._update_counter % 30 == 0:                    
                self._width -=1
                self._height -=1
                self._radius = self._width
            
            if self._width == 0 : ans=set({self})
            
        return ans

		
    def display(self,canvas):
        canvas.create_oval(self._x-self._width,self._y-self._height,\
                           self._x+self._width,self._y+self._height,fill='brown')


