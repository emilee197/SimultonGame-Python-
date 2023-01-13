import controller
import model   # Use in update_all to pass update a reference to this module

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from runner    import Runner
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
import math,random

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
mySimultons = set()
selected_object = ''    #'Ball'


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

def random_speed():
    # Magnitude is 5-10
    return random.randint(5,10)

def random_angle():
    # between 0 and 2pi
    return random.random()*math.pi*2
	
##def random_color():
##    # hex(52) -> "0x34", so [2:] is the two hex digits, without the 0x prefix
##    return "#"+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]

	
#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,mySimultons
    running     = False
    cycle_count = 0
    mySimultons       = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False 


#tep just one update in the simulation
def step ():
    global running
    running = False 
    global cycle_count    
    cycle_count += 1
    for s in mySimultons:
        s.update(model)


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    #print('select_object:', kind)
    global selected_object
    selected_object = kind
    


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global selected_object
    if selected_object == 'Ball':
        s=Ball(x,y,random_speed(),random_angle())
        add(s)
    elif selected_object == 'Floater':
        s=Floater(x,y,random_speed(),random_angle())
        add(s)
    elif selected_object == 'Special':
        s=Runner(x,y,random_speed(),random_angle())
        add(s)
    elif selected_object == 'Black_Hole':
        s=Black_Hole(x,y,0,0)
        add(s)
    elif selected_object == 'Pulsator':
        s=Pulsator(x,y,0,0)
        add(s)
    elif selected_object == 'Hunter':
        s=Hunter(x,y,0,0,5,random_angle())
        add(s)
    elif selected_object == 'Remove':
        print('remove:',x,y)
        for r in find(lambda z:z.distance((x,y))<10): remove(r)

    #if selected_object != '': add(s)
    


#add simulton s to the simulation
def add(s):
    mySimultons.add(s)
    #print('ball:', s, isinstance(s, Ball))
    
    

# remove simulton s from the simulation    
def remove(s):
    mySimultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    temp_set = set()
    for sim in mySimultons:
        if p(sim):
            temp_set.add(sim)
    return temp_set
    
##    myset=set()
##    for s in mySimultons:
##        if selected_object == 'Remove' and type(p) == tuple:
##            if s.distance(p) < 10: myset.update({s}) #10 is estimated
##        
##        #elif isinstance(s, Ball) or isinstance(s, Floater) or isinstance(s, Runner):
##        else:
##        #if isinstance(s, Prey): ## Prey is not defined here
##            res = p(s.get_location())
##            if type(res) == bool :
##                if res:
##                    #print('be eaten!', s)
##                    myset.update({s})
##            elif type(res) is float:
##                if res<200:
##                    #print('distance:', res, ' type:', s)
##                    myset.update({s})
##    return myset
        


#call update for every simulton in this simulation (passing model to each) 
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        delSet = set()
        for s in mySimultons:
            ans= s.update(model)            
            if type(ans) is set:                                
                if len(ans) > 0:
##                    if ans[0] == 'dead' : delSet.update(s) #remove 
##                    else:
                    print('find simultons to be removed!', ans)
                    delSet.update(ans)
        
        for d in delSet:
            #print('update all:', d)
            remove(d)

#For animation: (1) delete every simulton on the canvas; (2) call display on
#  each simulton being simulated, adding it back to the canvas, possibly in a
#  new location; (3) update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
# Easier to delete all and display all; could use move with more thought
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for s in mySimultons:
        s.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(mySimultons))+" balls/"+str(cycle_count)+" cycles")

