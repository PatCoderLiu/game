keyIn = False
roomnumber = 1
x = 2
y = 2
wallCounter = 0
def game():
    direction = ''
    print("Hello Adventurer! You have spawned in the middle of 3x3 room\nType left, right, forward, or back to move\nNavigate through different rooms to find the key to unlock the castle door to win!\nGood luck.")
#    print(" __ __ __\n|__|__|__|\n|__|O_|__|\n|__|__|__|")
    while keyIn != True and direction  != 'stop':
        global direction
        direction = input("What direction do you want to go(left, right, up, down)?\n")
        direction = direction.lower()
#        print_Room()
        move_Door()
        move_Direction()
        check_Wall()
        check_Door()
        enter_Room()
        print_Coordinates()



def move_Direction():
    global x
    global y
    if (direction == 'left'):
        if x != 1:
            print("You have moved left 1 block")
            x = x - 1
        else:
            print("You can not run into a wall")
    if (direction == 'right'):
        if x != 3:
            print("You have moved right 1 block")
            x = x + 1
        else:
            if y != 2:
                print("You can not run into a wall")
    if (direction == 'down'):
        if y != 1:
            print("You have moved down 1 block")
            y = y - 1
        else:
            print("You can not run into a wall")
    if (direction == 'up'):
        if x != 5:
            if y != 3:
                print("You have moved up 1 block")
                y = y + 1
        else:
            print("You can not run into a wall")
    
def check_Wall():
    global wallCounter
    if (x == 1):
        print ("You are next to a wall")
    if (x == 3 and y != 2):
        print ("You are next to a wall")
    if x == 5:
        print ("There is a wall up and below you")       
    if (y == 1 and x != 2):
        print ("You are next to a wall")
    if (y == 3):
        print ("You are next to a wall")
        
def check_Door():
    if x == 3 and y == 2:
        print("You are next to a door")
def move_Door():
    global x
    global y
    if direction == "right":
        if x == 3 and y == 2:
            x = x + 1
            print("You have opened a door and entered a hallway")
def enter_Room():
    global roomnumber
    global x 
    global y
    if direction == 'right':
        if x == 6:
            print("You have entered a new room")
            x = 1
            y = 2
            roomnumber = roomnumber + 1                                                                                                                                                                                                                                             
def print_Coordinates():
    print('x = ', x, ',', 'y = ', y , ',', 'Room:', roomnumber)
            
game()


# def print_Room():
#    if x == 1 and y == 1:
#        print(" __ __ __\n|__|__|__|\n|__|__|__|\n|O_|__|__|")
#    if x == 2 and y == 1:
#        print(" __ __ __\n|__|__|__|\n|__|__|__|\n|__|O_|__|")
#    if x == 3 and y == 1:
#        print(" __ __ __\n|__|__|__|\n|__|__|__|\n|__|__|O_|")
#    if x == 1 and y == 2:
#        print(" __ __ __\n|__|__|__|\n|O_|__|__|\n|__|__|__|")
#    if x == 2 and y == 2:
#        print(" __ __ __\n|__|__|__|\n|__|O_|__|\n|__|__|__|")
#    if x == 3 and y == 2:
#        print(" __ __ __\n|__|__|__|\n|__|__|O_|\n|__|__|__|")
#    if x == 1 and y == 3:
#       print(" __ __ __\n|O_|__|__|\n|__|__|__|\n|__|__|__|")
#    if x == 2 and y == 3:
#        print(" __ __ __\n|__|O_|__|\n|__|__|__|\n|__|__|__|")
#    if x == 3 and y == 3:
#        print(" __ __ __\n|__|__|O_|\n|__|__|__|\n|__|__|__|")
