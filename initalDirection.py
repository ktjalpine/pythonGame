# Imports
import sys
import north
import west
import east
import south

# Initial definition of the player-defined direction as a CLI
direction = sys.argv[0]


def startDirection(direction):
    if direction == "N":
        print("You have chosen to start in the north."
              " It is a very harsh and cold land..\n")
        north.start()
    else:
        direction == "S"
    print("You have chosen to start in the south."
          " It is a very tropical land, with multiple cities to explore"
          " and treasure to be found.")
    south.start()
'''
    else:
    if direction == "E":
        print("You have chosen to start in the east."
              " It is a land dominated by rolling hills, vast open spaces,"
              " and the backdrop of the mountains to the north makes this the"
              " most beautiful country in all lands.")

# east.start()
else:
if direction == "W":
    print("You have chosen to start in the west."
          " The west is a vast desert, with nothing in sight but continous"
          " dunes of sand that reach hundreds of feet high, and temperatures"
          " soar to above 120 degrees.")
    #   west.start()
'''
