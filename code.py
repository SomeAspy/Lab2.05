#   Aiden B.
#   Lab2.05
#   3/9/2021
#
#   info:
#   underline in unicode \u0332

#   BOARD
#   A1|A2|A3
#   B1|B2|B3
#   C1|C2|C3

# Import the RegEx library
import re

# Blank out variables and define them
a1=a2=a3=b1=b2=b3=c1=c2=c3=" "
Cclaimed=Pclaimed=[""]

# Build and display the board
def refresh(LastSet=True,BoardFormat=""):
    board="\n "+a1+"|"+a2+"|"+a3+"\n "+b1+"|"+b2+"|"+b3+"\ne "+c1+"|"+c2+"|"+c3
    # Add underline to all characters until we hit "e"
    for i in board:
        if i=="e":
            LastSet=False
        elif LastSet:
            BoardFormat+=i+"\u0332"
        elif LastSet==False:
            BoardFormat+=i
    print(BoardFormat)

# Change position given to X
def Place(pos):
    # Reference variables outside the function
    global a1,a2,a3,b1,b2,b3,c1,c2,c3
    if pos=="a1":
        a1="X"
    elif pos=="a2":
        a2="X"
    elif pos=="a3":
        a3="X"
    elif pos=="b1":
        b1="X"
    elif pos=="b2":
        b2="X"
    elif pos=="b3":
        b3="X"
    elif pos=="c1":
        c1="X"
    elif pos=="c2":
        c2="X"
    elif pos=="c3":
        c3="X"

# Check if the space given is claimed
def IsOpen(space):
    if space in Pclaimed or space in Cclaimed:
        return False
    else:
        return True

# Player's Turn
def PTurn():
    toCheck=input("Please choose an area to claim\f").lower()
    # check if input matches RegEx
    if bool(re.match(r"[a-c][1-3]", toCheck)):
        if IsOpen(toCheck):
            global SelectedSpace
            SelectedSpace=toCheck
            Place(SelectedSpace)
            # Add the given space to the list of claimed spaces
            Pclaimed.append(SelectedSpace)
            refresh()
        else:
            print("That space seems to be occupied! Please input an open space!")
            # Retry
            PTurn()
    else:
        print("That isn't a valid space, please double check your input!")
        PTurn()

# Check for player win conditions
def PWinCheck():
    if "a1"in Pclaimed and"b1"in Pclaimed and"c1"in Pclaimed:
        return True
    elif "a2"in Pclaimed and"b2"in Pclaimed and"c2"in Pclaimed:
        return True
    elif "a3"in Pclaimed and"b3"in Pclaimed and"c3"in Pclaimed:
        return True
    elif "a1"in Pclaimed and"a2"in Pclaimed and"a3"in Pclaimed:
        return True
    elif "b1"in Pclaimed and"b2"in Pclaimed and"b3"in Pclaimed:
        return True
    elif "c1"in Pclaimed and"c2"in Pclaimed and"c3"in Pclaimed:
        return True
    elif "a1"in Pclaimed and"b2"in Pclaimed and"c3"in Pclaimed:
        return True
    elif "a3"in Pclaimed and"b2"in Pclaimed and"c1"in Pclaimed:
        return True
    else:
        return False

# Check for Computer win conditions
def CWinCheck():
    if "a1"in Cclaimed and"b1"in Cclaimed and"c1"in Cclaimed:
        return True
    elif "a2"in Cclaimed and"b2"in Cclaimed and"c2"in Cclaimed:
        return True
    elif "a3"in Cclaimed and"b3"in Cclaimed and"c3"in Cclaimed:
        return True
    elif "a1"in Cclaimed and"a2"in Cclaimed and"a3"in Cclaimed:
        return True
    elif "b1"in Cclaimed and"b2"in Cclaimed and"b3"in Cclaimed:
        return True
    elif "c1"in Cclaimed and"c2"in Cclaimed and"c3"in Cclaimed:
        return True
    elif "a1"in Cclaimed and"b2"in Cclaimed and"c3"in Cclaimed:
        return True
    elif "a3"in Cclaimed and"b2"in Cclaimed and"c1"in Cclaimed:
        return True
    else:
        return False

# End the game and display winner
def WinCheck():
    if CWinCheck():
        print("Computer Wins!")
        # End the script
        quit()
    elif PWinCheck():
        print("You Win!")
        quit()
    else:
        pass

# Computer claiming system. probably will do this later.
# def CPlace(Z,CA1,CA2,CA3,CB1,CB2,CB3,CC1,CC2,CC3):
#    if Z=="a1":
#        return CA1
#    elif Z=="a2":
#        return CA2
#    elif Z=="a3":
#        return CA3
#    elif Z=="b1":
#        return CB1
#    elif Z=="b2":
#        return CB2
#    elif Z=="b3":
#        return CB3
#    elif Z=="c1":
#        return CC1

# Loop claiming and check for win.
def cycle():
    PTurn()
    # CTurn()
    WinCheck()
    cycle()

# Run the game
print("How To Play:\nSpots on the board are named A1-C3, with A being the top row and C being the bottom.")
refresh()
cycle()
