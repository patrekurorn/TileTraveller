# Gera starting position og geta hreyft sig í þær áttir sem hægt er

def starting_posistion():
    x = 1
    y = 1
    lx = 1
    ly = 1
    return x , y , lx, ly

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

def is_user_user_in_range(x, y, lx, ly):
    # Here below is the whole frame
    if x > 3:
        x = 3
        print("Not a valid direction!")
    if x < 1:
        x = 1
        print("Not a valid direction!")
    if y > 3:
        y = 3
        print("Not a valid direction!")
    if y < 1:
        y = 1
        print("Not a valid direction!")
    # Here below is the allowed movements for the user
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
    
    #####
    #(1, 1)
    if lx == 1 and ly == 1:
        if x > 1:
            x = 1
            print("Not a valid direction!")
            print("You can travel: (N)orth.")
    #(2,1)
    if lx == 2 and ly == 1:
        if x > 2:
            x = 2
            print("Not a valid direction!")
            print("You can travel: (N)orth.")

    if lx == 2 and ly == 1:
        if x < 2:
            x = 2
            print("Not a valid direction!")
            print("You can travel: (N)orth.")
    #(3,1)
    if lx == 3 and ly == 1:
        if x < 3:
            x = 3
            print("Not a valid direction!")
            print("You can travel: (N)orth.")
    #(2,2)
    if lx == 2 and ly == 2:
        if x > 2:
            x = 2
            print("Not a valid direction!")
            print("You can travel: (S)outh or (W)est.")

    if lx == 2 and ly == 2:
        if y > 2:
            y = 2
            print("Not a valid direction!")
            print("You can travel: (S)outh or (W)est.")

    #(3,2)
    if lx == 3 and ly == 2:
        if x < 3:
            x = 3
            print("Not a valid direction!")
            print("You can travel: (N)orth or (S)outh.")

    #(2,3)
    if lx == 2 and ly == 3:
        if y < 3:
            y = 3
            print("Not a valid direction!")
            print("You can travel: (E)ast or (W)est.")



    
    return x, y



current_x, current_y, last_posistion_of_x, last_posistion_of_y = starting_posistion()

#for the moment, to exit the while loop use "q"
while True:
    current_x, current_y = is_user_user_in_range(current_x, current_y, last_posistion_of_x, last_posistion_of_y)
    print("x", current_x)
    print("y", current_y)
    print("last x", last_posistion_of_x)
    print("last y", last_posistion_of_y)

    last_posistion_of_x = current_x
    last_posistion_of_y = current_y

    user_input = get_user_input()
    current_x, current_y = what_direction_to_move(user_input, current_x, current_y)








