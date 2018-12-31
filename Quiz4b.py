a = [49, 27, 101, -10]
b = a
c = list(a)
d = c
a[3] = 68
c[2] = a[1]
b = a[1 : 3]
b[1] = c[2]
print b

point = [0, 0]

def function1():
    point[0] += 1
    point[1] += 2

def function2():
    point = [50, 50]
    
print point

a = ["green", "blue", "white", "black"]
b = a
c = list(a)
d = c
a[3] = "red"
c[2] = a[1]
b = a[1 : 3]
b[1] = c[2]

print a
print b
print c
print d
import simplegui

def draw(canvas):
    canvas.draw_polygon([(50, 50),(180, 50),(180, 140),(50, 140)], 2, 'Red')
    

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 300)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()


import simplegui

# initialize state
width = 300
height = 300
position = [10,20]


# event handlers
def keydown(key):
    if key == simplegui.KEY_MAP['down']:
        position[1] = position[1] + 0.7
        position[0] = position[0] + 3

def draw(canvas):
    canvas.draw_circle(position, 2, 2, "blue", "blue")
    canvas.draw_polygon([(50, 50),(180, 50),(180, 140),(50, 140)], 2, 'Red')
    

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 300)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

# Keyboard echo

import simplegui

# initialize state
current_key = ' '
globo = 5

# event handlers
def keydown(key):
    global globo
    global current_key
    current_key = chr(key)
    globo = globo * 2
    print globo

def keyup(key):
    global globo
    global current_key
    current_key = ' '
    globo = globo - 3
    print globo
    
def draw(canvas):
    canvas.draw_text(current_key, [10, 25], 20, "Red")
    
# create frame
frame = simplegui.create_frame("Echo", 35, 35)

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# start frame
frame.start()