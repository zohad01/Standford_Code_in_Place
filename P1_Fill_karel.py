from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    put_all()
    # OverAll Function to complete execution
def put_all():
    while left_is_clear():
        move_put()
        move_tight()
        check_above_line()
    move_put()

# To change the face of karel in right direction
def move_right():
    for i in range(3):
        turn_left()

# kerel put beeper and move on
def move_put():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    # move_right()
# To move karel back
def move_tight():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()
# Check weather is there any need to move above
def check_above_line():
    if left_is_clear():
        turn_left()
        move()
        move_right()
    
        
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()