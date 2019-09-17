# Gera starting position og geta hreyft sig í þær áttir sem hægt er

def starting_posistion():
    x = 1
    y = 1
    return x , y

def get_user_input():
    return input("Where do you want to move? ").lower()

def what_direction_to_move(current_user_input,x,y):
    #north
    if current_user_input == "n":
        y +=1
    #east
    if current_user_input == "e":
        x +=1
    #south
    if current_user_input == "s":
        y -=1
    #west
    if current_user_input == "w":
        x -=1
    return x, y

def is_user_user_in_range(x, y):
    # Here below is the whole frame
    """if x > 3:
        x = 3
    if x < 1:
        x = 1
    if y > 3:
        y = 3
    if y < 1:
        y = 1"""
    # Here below is the allowed movements for the user
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
        if x > 1:
            x = 1
            print("Not a valid direction!")
        elif x < 1:
            x = 1
            print("Not a valid direction!")
        elif y < 1:
            y = 1
            print("Not a valid direction!")
        elif y > 1:
            y += 1

    
    return x, y

current_x, current_y = starting_posistion()
user_input = get_user_input()

#for the moment, to exit the while loop use "q"
while user_input != "q":

    current_x, current_y = what_direction_to_move(user_input, current_x, current_y)
    current_x, current_y = is_user_user_in_range(current_x, current_y)

    print("x", current_x)
    print("y", current_y)




    user_input = get_user_input()
