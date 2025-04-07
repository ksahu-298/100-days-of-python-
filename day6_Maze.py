def turn_right():
    for right in range (0,3):
        turn_left()
        
while not at_goal():
    if right_is_clear() :
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
     
        
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
