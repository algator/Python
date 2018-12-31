# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user40_3eyQThAYsX_30.py
        ball_vel[0] = random.randrange(120/40, 240/40)
        ball_vel[1] = -random.randrange(60/40, 180/40)
    elif direction =="LEFT":
        ball_vel[0] = -random.randrange(120/40, 240/40)
        ball_vel[1] = -random.randrange(60/40, 180/40)
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2,scorestring1,scorestring2  # these are ints
    score1 = 0
    score2 = 0
    scorestring1 = "0"
    scorestring2 = "0"
    paddle1_pos = [0,HEIGHT/2]
    paddle2_pos = [0,HEIGHT/2]
    spawn_ball("LEFT")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,vel,scorestring1,scorestring2     

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide with left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        spawn_ball("RIGHT")
        score2 = score2+1
        scorestring2 = str(score2)        
    canvas.draw_polygon([(600,paddle1_pos[1]-PAD_HEIGHT/2),(600,paddle1_pos[1]+PAD_HEIGHT/2),(600-PAD_WIDTH,paddle1_pos[1]+PAD_HEIGHT/2),(600-PAD_WIDTH,paddle1_pos[1]-PAD_HEIGHT/2)], 2, 'White','White')
    canvas.draw_polygon([(0,paddle2_pos[1]-PAD_HEIGHT/2),(0,paddle2_pos[1]+PAD_HEIGHT/2),(PAD_WIDTH,paddle2_pos[1]+PAD_HEIGHT/2),(PAD_WIDTH,paddle2_pos[1]-PAD_HEIGHT/2)], 2, 'White','White')
    
    # collide and reflect off of left hand paddle
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH and ball_pos[1] <= paddle1_pos[1]+PAD_HEIGHT/2 and ball_pos[1] >= paddle1_pos[1]-PAD_HEIGHT/2:
               ball_vel[0] = - ball_vel[0]*1.1 
            
    # collide and reflect off of right hand paddle
    if ball_pos[0] >= WIDTH-(BALL_RADIUS+PAD_WIDTH) and ball_pos[1] <= paddle2_pos[1]+PAD_HEIGHT/2 and ball_pos[1] >= paddle2_pos[1]-PAD_HEIGHT/2:
               ball_vel[0] = - ball_vel[0]*1.1 
            
    # draw scores
    canvas.draw_text("SCORE", (265, 25), 20, "White","sans-serif")    
    canvas.draw_text(scorestring1, (150, 60), 30, "White","sans-serif")  
    canvas.draw_text(scorestring2, (450, 60), 30, "White","sans-serif")  
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 7
    if key==simplegui.KEY_MAP["up"]:
        paddle1_vel[1] -= acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle1_vel[1] += acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle2_vel[1] -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle2_vel[1] += acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = -7

    if key==simplegui.KEY_MAP["up"]:
        paddle1_vel[1] -= acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle1_vel[1] += acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle2_vel[1] -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle2_vel[1] += acc


# create frame
frame = simplegui.create_frame("PONG", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESTART",new_game,200)

# start frame
new_game()
frame.start()





