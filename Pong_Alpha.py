# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0,0]
paddle1_vel = [0,0]
paddle2_vel = [0,0]
vel = [0,0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_vel,ball_pos, WIDTH, HEIGHT
    ball_vel = [0,0]
    ball_pos = [WIDTH / 2, HEIGHT / 2]
# these are vectors stored as lists
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(120/30, 240/30)
        ball_vel[1] = -random.randrange(60/30, 180/30)
    elif direction =="LEFT":
        ball_vel[0] = -random.randrange(120/30, 240/30)
        ball_vel[1] = -random.randrange(60/30, 180/30)
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball("RIGHT")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,vel    

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    # collide and reflect off of right hand side of canvas
    elif ball_pos[0] >= WIDTH-BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    # collide and reflect off of top of canvas
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # collide and reflect off of bottom of canvas
    elif ball_pos[1] >= HEIGHT-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    global paddle1_vel, paddle2_vel
    paddle1_vel[0] += vel[0]
    paddle2_vel[1] += vel[1]
    
    # draw paddles
    canvas.draw_polygon([(0, 0),(0,PAD_HEIGHT),(PAD_WIDTH,PAD_HEIGHT),(PAD_WIDTH, 0)], 2, 'Blue')
    canvas.draw_polygon([(600, 0),(600,PAD_HEIGHT),(600-PAD_WIDTH,PAD_HEIGHT),(600-PAD_WIDTH, 0)], 2, 'Blue')
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 1
    if key==simplegui.KEY_MAP["left"]:
        vel[0] -= acc
    elif key==simplegui.KEY_MAP["right"]:
        vel[0] += acc
    elif key==simplegui.KEY_MAP["down"]:
        vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        vel[1] -= acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()