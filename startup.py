import sys
import initalDirection
import optionsAndInventory

inital_direction = str(sys.argv[1])


# Inital check to make sure player entered a good direction
# Then starts player in that direction
if inital_direction == "N" or inital_direction == "S" or inital_direction == "E"\
     or inital_direction == "W" :
    if len(sys.argv) > 0 :
        print("Hello, welcome to the game.\n")
        # Explaination of direction to the player
        print("You are about to embark on a journey."
              " Based on the inital direction you chose at the command line"
              " you will be placed in a specific region of the game.\n")
        initalDirection.startDirection(sys.argv[0])

#Startup error output to player
else:
    print("Some sort of error has occured."
          "Make sure you input an inital N,S,E,W direction in the command line."
          "Only one, please\n")