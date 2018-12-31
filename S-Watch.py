# "Stopwatch: The Game"
# http://www.codeskulptor.org/#user40_LNiNY4qBSj_5.py

# import libraries
import math
import simplegui

# define global variables
raw_time = 0
trials = 0
success = 0
zero = 1
trials_s = "0"
success_s = "0"
game = ""

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t): 
    global zero
    tens = t%10
    min = t/(60*10)
    if  t/10>=60:
        sec = t/10-min*60
    else:    
        sec = (t/10)        
    a = str (min)
    b = str (sec/10)
    c = str(sec%10)
    d = str(tens)
    zero = tens
    return a+":"+b+c+"."+d

# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()

def stop():
    global trials
    global success
    global zero
    global game
    timer.stop()
    trials = trials + 1
    if int(zero) == 0:
        success = success + 1
    trials_s = str(trials)
    success_s = str(success)
    game = success_s+"/"+trials_s
        
def reset():
    global raw_time
    global trials
    global success
    global zero 
    global trials_s
    global success_s 
    global game
    stop()
    raw_time = 0
    trials = 0
    success = 0
    zero = 1
    trials_s = "0"
    success_s = "0"
    game = success_s+"/"+trials_s

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global raw_time
    raw_time = raw_time +1    

# define draw handler
def draw(canvas):
    global i
    global game
    scrn_time = str(raw_time)
    canvas.draw_text(format(raw_time),[100, 150], 40, "White")
    canvas.draw_text(game,[200, 50], 30, "Blue")
    
# create frame
frame = simplegui.create_frame("Stopwatch Game",300, 300)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)
frame.add_button("Start",start,200)
frame.add_button("Stop",stop,200)
frame.add_button("Reset",reset,200)

# start frame
game = success_s+"/"+trials_s
timer.start()
frame.start()




