import sys

inital_direction = str(sys.argv[0])

#Inital check to make sure player entered a good direction
if sys.argv[0] == "N" or sys.argv[0] == "S" or sys.argv[0] == "E"\
     or sys.argv[0] == "W" :
    if len(sys.argv) > 0 :
        print("Hello, welcome to the game.")

#Startup error output to player
else:
    print("Some sort of error has occured."
          "Make sure you input an inital N,S,E,W direction in the command line."
          "Only one, please")

#Explaination of direction to the player
print("You are about to embark on a journey."
      " Based on the inital direction you chose at the command line"
      " you will be placed in a specific region of the game.")
