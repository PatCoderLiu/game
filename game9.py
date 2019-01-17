# For moving exception put it in move_Door instead of move_Direction

keyIn = False
keyOn = False
roomnumber = 1
hroomnumber = 4
x = 2
y = 2
wallCounter = 0
def game():
    global direction
    direction = ''
    print("Hello Adventurer! You have spawned in the middle of 3x3 room\nType left, right, up, or down to move\nNavigate through different rooms to find the key to unlock the castle door to win!\nGood luck.")
    while keyIn != True and direction  != 'stop':
        direction = input("What direction do you want to go(left(l), right(r), up(u), down(d))?\n")
        shorten_Input()
        direction = direction.lower()
        move_Door()
        move_Direction()
        check_Door()
        enter_Room()
        reenter_Room()
        pick_Key()
        print_Coordinates()


def shorten_Input():
    global direction
    if direction == 'r':
        direction = 'right'
    if direction == 'l':
        direction = 'left'
    if direction == 'u':
        direction = 'up'
    if direction == 'd':
        direction = 'down'
def move_Direction():
    global x
    global y
    if (direction == 'left'):
        if x != 1 and y != -1 and y != -2 and y != -3 and y != 8 and y != 7:
          if x != 9:
            print("You have moved left 1 block")
            x = x - 1
          else:
            print("You can not run into a wall")
          if x == 9 and hroomnumber == 1:
            print("You have moved left 1 block")
            x = x - 1
        if roomnumber == 2 and hroomnumber == 1:
            if x == 4:
                x = x + 1
                print("You cannot run into a wall")
    if (direction == 'right'):
        if roomnumber == 1:
            if hroomnumber == 4:
                if x != 3 and y != -1 and y != -2 and y != -3:
                    print("You have moved right 1 block")
                    x = x + 1
                else:
                    if y != 2:
                        print("You can not run into a wall")
            if hroomnumber == 3:
                if x != 5 and y != 7 and y != 8 and y != 9:
                    print("You have moved right 1 block")
                    x = x + 1
                else:
                    print("You can not run into a wall")
            if hroomnumber == 2:
                if x != 5 and y != 7:
                    print("You have moved right 1 block")
                    x = x + 1
                else:
                    print("You can not run into a wall")
        if roomnumber == 2 and hroomnumber != 1:
            if x != 5 and y != -1:
                print("You have moved right 1 block")
                x = x + 1
            else:
                    print("You can not run into a wall")
        if roomnumber == 2 and hroomnumber == 1:
            if x != 3 and y != 4:
                print("You have moved right 1 block")
                x = x + 1
            else:
                    print("You can not run into a wall")
        if roomnumber == 3 and hroomnumber == 4:
            if x != 7:
                print("You have moved right 1 block")
                x = x + 1   
            else:
                print("You cannot run into a wall")
        if roomnumber == 3 and hroomnumber == 2:
            if x != 5:
                print("You have moved right 1 block")
                x = x + 1   
            else:
                print("You cannot run into a wall")
    if (direction == 'down'):
        if y != 1:
            if roomnumber == 1:
                if hroomnumber == 4:
                    if x != 5 and y != 1:
                        print("You have moved down 1 block")
                        y = y - 1
                    else:
                        print("You can not run into a wall")
                if hroomnumber == 3:
                    if x != 5 and y != 1:
                        print("You have moved down 1 block")
                        y = y - 1
                    else:
                        print("You can not run into a wall")
                if hroomnumber == 2:
                    if x != 5 and x != 7 and x != -1:
                        print("You have moved down 1 block")
                        y = y - 1
                    else:
                        print("You can not go down")
            if roomnumber == 2 and hroomnumber != 1:
                if x != 7 and x != -1:
                    print("You have moved down 1 block")
                    y = y - 1
                else:
                    print("You can not run into a wall")
            if roomnumber == 2 and hroomnumber == 1:
                if y != 1:
                    print("You have moved down 1 block")
                    y = y - 1
                else:
                    print("You can not run into a wall")
            if roomnumber == 3:
                if x != -1 and x != 7:
                    print("You have moved down 1 block")
                    y = y - 1
                else:
                    print("You can not run into a wall")
    if (direction == 'up'):
        if roomnumber == 1:
            if hroomnumber == 4:
                if y != 3 and x != 5 and x != -1:
                    print("You have moved up 1 block")
                    y = y + 1
                else:
                    print("You can not run into a wall")
            if hroomnumber == 3:
                if y != 5:
                    print("You have moved up 1 block")
                    y = y + 1
                else:
                    print("You can not run into a wall")
            if hroomnumber == 2:
                if y != 5 and x != 7:
                    print("You have moved up 1 block")
                    y = y + 1
                else:
                    print("You can not run into a wall")
        if roomnumber == 2 and hroomnumber != 1:
            if y != 5 and x != 7 and x != -1:
                print("You have moved up 1 block")
                y = y + 1
            else:
                print("You can not run into a wall")
        if roomnumber == 2 and hroomnumber == 1:
            if y != 3:
                print("You have moved up 1 block")
                y = y + 1
            else:
                print("You can not run into a wall")
        if roomnumber == 3 and hroomnumber != 2:
            if y != 7 and x != -1:
                print("You have moved up 1 block")
                y = y + 1   
            else:
                print("You cannot run into a wall")
        if roomnumber == 3 and hroomnumber == 2:
            if y != 5 and x != -1:
                print("You have moved up 1 block")
                y = y + 1
def check_Wall():
    global wallCounter
    if (x == 1 and hroomnumber == 4):
        if roomnumber == 1:
            print ("You are next to a wall")
        if roomnumber == 2 and y != 3:
            print ("You are next to a wall")
        if roomnumber == 3 and y != 5:
            print ("You are next to a wall")
    if x == 1 and hroomnumber == 3:
         print ("You are next to a wall")
    if (x == 3 and y != 2 and roomnumber == 1 and hroomnumber == 4):
        print ("You are next to a wall")
    if x == 5 and roomnumber == 1 and hroomnumber == 4:
        print ("There is a wall up and below you")
    if x == 5 and roomnumber == 1 and hroomnumber == 3:
        print("You are next to a wall")
    if (y == 1 and x != 2 and hroomnumber == 4):
        print ("You are next to a wall")
    if (y == 1 and x != 3 and hroomnumber == 3):
        print ("You are next to a wall")
    if (y == 3 and roomnumber == 1 and hroomnumber == 4):
        print ("You are next to a wall")
    if y == 5 and roomnumber == 2:
        print("You are next to a wall")
    if y == 5 and hroomnumber == 2 and x != 3:
        print("You are next to a wall")
    if x == 5 and hroomnumber == 2 and y != 3 and roomnumber == 1:
        print("You are next to a wall")
    if y == 5 and hroomnumber == 3 and x != 3:
        print("You are next to a wall")
    if x == 2:
        if roomnumber == 1:
            if y == -1:
                print("There is a wall on your left and right")
            if y == -2:
                print("There is a wall on your left and right")
            if y == -3:
                print("There is a wall on your left and right")
        
def check_Door():
    if roomnumber == 1 and hroomnumber == 4:
        if x == 3 and y == 2:
            if roomnumber != 3:
                print("You are next to a door")
        if x == 2 and y == 1:
            print("You are next to a door")
    if roomnumber == 2 and hroomnumber == 2:
        if x == 1 and y == 3:
            if roomnumber != 1:
                print("You are next to a door")
        if x == 5 and y == 3 and hroomnumber == 4:
            print("You are next to a door")
    if roomnumber == 3:
        if x == 1 and y == 5:
            print("You are next to a door")
    if hroomnumber == 3:
        if x == 3 and y == 5:
            print("You are next to a door")
        if x == 3 and y == 1:
            print("You are next to a door")
    if hroomnumber == 2 and roomnumber != 3:
        if x == 3 and y == 5:
            print("You are next to a door")
        if x == 5 and y == 3:
            print("You are next to a door")
        if roomnumber == 2 and hroomnumber == 2:
            if x == 3 and y == 1:
                print("You are next to a door")
        if roomnumber == 2 and hroomnumber == 1:
            if x == 2 and y == 3:
                print("You are next to a door")
    if hroomnumber == 2 and roomnumber == 3:
        if roomnumber == 3:
            if x == 1 and y == 3:
                print("You are next to a door")
    if hroomnumber == 4 and roomnumber == 2:
      if x == 5 and y == 3:
        print("You are next to a door")
      if x == 1 and y == 3:
        print("You are next to a door")
    if hroomnumber == 1 and roomnumber == 2:
      if x == 2 and y == 1:
        print("You are next to a door")
def move_Door():
    global x
    global y
    if direction == "right":
        if roomnumber == 1 and hroomnumber == 4:
            if x == 3 and y == 2:
                if roomnumber != 3:
                    x = x + 1
                    print("You have opened a door and entered a hallway")
        if roomnumber == 2:
            if x == 5 and y == 3:
                x = x + 1
                print("You have opened a door and entered a hallway")
        if hroomnumber == 2 and roomnumber != 3:
            if x == 5 and y == 3:
                x = x + 1
                print("You have opened a door and entered a hallway")
    if direction == "left":
        if roomnumber == 2 and hroomnumber == 2:
            if x == 1 and y == 3:
                x = x - 1
                print("You have opened a door and entered a hallway")
        if roomnumber == 2 and hroomnumber == 4:
            if x == 1 and y == 3:
                x = x - 1
                print("You have opened a door and entered a hallway")
        if roomnumber == 3 and hroomnumber == 4:
            if x == 1 and y == 5:
                x = x - 1
                print("You have opened a door and entered a hallway")
        if roomnumber == 3 and hroomnumber == 2:
            if x == 1 and y == 3:
                x = x - 1
                print("You have opened a door and entered a hallway")
    if direction == "down":
        if roomnumber == 1:
            if x == 2 and y == 1:
                y = y - 1
                print("You have opened a door and entered a hallway")
        if hroomnumber == 3:
            if x == 3 and y == 1:
                y = y - 1
                print("You have opened a door and entered a hallway")
        if hroomnumber == 2 and roomnumber == 2:
            if x == 3 and y == 1:
                y = y - 1
                print("You have opened a door and entered a hallway")
        if hroomnumber == 1 and roomnumber == 2:
          if x == 2 and y == 1 and keyOn == True:
            print("You have opened the castle door and won!")
            keyIn = True
          else:
            if x == 2 and y == 1 and keyOn == False
            print("The door is locked")
          
    if direction == "up":
        if hroomnumber == 3:
            if x == 3 and y == 5:
                y = y + 1
                print("You have opened a door and entered a hallway")
        if hroomnumber == 2:
            if x == 3 and y == 5:
                y = y + 1
                print("You have opened a door and entered a hallway")
        if hroomnumber == 1:
            if x == 2 and y == 3:
                y = y + 1
                print("You have opened a door and entered a hallway")
def enter_Room():
    global roomnumber
    global hroomnumber
    global x 
    global y
    if direction == 'right':
        if x == 6:
            if roomnumber == 1:
                print("You have entered a room")
                x = 1
                y = 3
                roomnumber = roomnumber + 1
        if x == 8:
            if roomnumber == 2 and hroomnumber == 4:
                print("You have entered a room")
                x = 1
                y = 5
                roomnumber = roomnumber + 1
            if roomnumber != 3 and hroomnumber == 2:
                print("You have entered a room")
                x = 1
                y = 3
                roomnumber = roomnumber + 1
    if direction == 'left':
        if x == -2:
            print("You have entered a room")
            if roomnumber == 2:
                if hroomnumber == 4:
                    x = 3
                    y = 2
                if hroomnumber == 2:
                    x = 5
                    y = 3
            if roomnumber == 3:
                x = 5
                y = 3
            roomnumber = roomnumber - 1
    if direction == 'down':
        if y == -4:
            print("You have entered a room")
            if roomnumber == 1:
                x = 3
                y = 5
                hroomnumber = hroomnumber - 1
        if y == -2 and hroomnumber == 3:
            print("You have entered a room")
            if hroomnumber == 3:
                x = 3
                y = 5
                hroomnumber = hroomnumber - 1
        if y == -2 and hroomnumber == 2:
            print("You have entered a room")
            if hroomnumber == 2:
                x = 2
                y = 9
                hroomnumber = hroomnumber - 1
        
            
    if direction == 'up':
        if y == 10 and hroomnumber == 3:
            print("You have entered a room")
            if hroomnumber == 3:
                x = 2
                y = 1
                hroomnumber = hroomnumber + 1
        if y == 8:
            print("You have entered a room")
            if hroomnumber == 2:
                x = 3
                y = 1
                hroomnumber = hroomnumber + 1
        if y == 6:
            if hroomnumber == 1:
                print("You have entered a room")
                x = 3
                y = 1
                hroomnumber = hroomnumber + 1
def print_Coordinates():
    print('x = ', x, ',', 'y = ', y , ',', 'Room:', roomnumber, 'Horizontal:', hroomnumber, keyOn)
def reenter_Room():
    global x
    global y
    if direction == 'left':
        if roomnumber == 1 and hroomnumber == 4:
            if x == 4:
                x = x - 1
                print("You have entered a room")
        if roomnumber == 2:
            if x == 6:
                x = x - 1
                print("You have entered a room")
        if hroomnumber == 2:
            if x == 6:
                x = x - 1
                print("You have entered a room")
    if direction == 'right':
        if roomnumber == 2:
            if x == 0:
                x = x + 1
                print("You have entered a room")
        if roomnumber == 3:
            if x == 0:
                x = x + 1
                print("You have entered a room")
    if direction == 'up':
        if hroomnumber == 4:
            if y == 0:
                y = y + 1
                print("You have entered a room")
        if hroomnumber == 3:
            if y == 0:
                y = y + 1
                print("You have entered a room")
        if hroomnumber == 2:
            if y == 0:
                y = y + 1
                print("You have entered a room")
    if direction == 'down':
        if hroomnumber == 2:
            if y == 6:
                y = y - 1
                print("You have entered a room")
        if hroomnumber == 1:
            if y == 4:
                y = y - 1
                print("You have entered a room")
def pick_Key():
    global keyOn
    if x == 7 and y == 1 and keyOn == False:
        print("You have picked up a key!")
        keyOn = True
def obstacles():
    print()
def check_Key():

game()
