# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from prey  import Prey


class Pulsator(Black_Hole):    
    #starve_limit = 600
    #starve_counter = 0
    update_counter = 0
    def __init__(self,x,y,w,h):
        Black_Hole.__init__(self, x,y,Black_Hole.radius*2,Black_Hole.radius*2)
        self._x       = x
        self._y       = y
##        self._speed   = speed
##        self._angle   = angle
        self._width = 20
        self._height = 20
        self._update_counter = 0
        self._radius = 10
        #self._color   = color

    
    def update(self,model):
        ans = model.find(lambda x:isinstance(x,Prey))
        sub = ans.copy()
        for p in sub:
            if not self.contains(p.get_location()): ans.remove(p)

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
        
##        ans = model.find(self.contains)
##        new_set = set()
##        for s in ans:
##            if isinstance(s, Prey): new_set.update({s})            
##        
##        self._update_counter +=1
##        if type(new_set) is set:                                
##            if len(new_set) > 0: #eat something
##                #print('update counter:', self._update_counter)
##                self._width += 1
##                self._height +=1
##                self._radius = self._width
##                self._update_counter = 0
##            else:
##                if self._update_counter % 30 == 0:                    
##                    self._width -=1
##                    self._height -=1
##                    self._radius = self._width
##                
##                if self._width == 0 : new_set=set({self})
##        return new_set            

		
    def display(self,canvas):
        canvas.create_oval(self._x-self._width,self._y-self._height,\
                           self._x+self._width,self._y+self._height,fill='grey')

