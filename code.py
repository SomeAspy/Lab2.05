#   Aiden B.
#   Lab2.05
#   3/9/2021
#
#   info:
#   underline in unicode \u0332
#   THIS USES EXEC AND IS THEREFORE BAD PRACTICE!!
#   convert to dictionary when I'm actually good maybe...
#   Apparently you can't use exec() inside a function, so like, wtf?
#
#   BOARD
#   A1|A2|A3
#   B1|B2|B3
#   C1|C2|C3
#
#   init
import re
a1=a2=a3=b1=b2=b3=c1=c2=c3=" "
claimed=[""]
def refresh(LastSet=True,BoardFormat=""):
    board="\n "+a1+"|"+a2+"|"+a3+"\n "+b1+"|"+b2+"|"+b3+"\ne "+c1+"|"+c2+"|"+c3
    for i in board:
        if i=="e":LastSet=False
        elif LastSet:BoardFormat+=i+"\u0332"
        elif LastSet==False:BoardFormat+=i
    print(BoardFormat)
print("How To Play:\nSpots on the board are named A1-C3, with A being the top row and C being the bottom.")

#SelectedSpace=input("Please choose an area to claim\f").lower()

#wtf=exec(SelectedSpace+'="X"') #legit can't even
#def fill():
#    if bool(re.match(r"[a-c][1-3]", SelectedSpace)):
#        if SelectedSpace in claimed:
#            print("That space is occupied!")
#        else:
#            wtf
#            claimed.append(SelectedSpace)
#    else:
#        print("That didn't work...")
#def refill():
#    refresh()
#    global SelectedSpace
#    SelectedSpace=input("Please choose an area to claim\f").lower()
#    fill()
#
#wtf=exec(SelectedSpace+'="X"')
#refresh()

def Place(pos):
    if pos=="a1":
        a1="X"
    elif pos=="a2":
        a2=="X"
    elif pos=="a3":
        a3=="X"
    elif pos=="b1":
        b1="X"
    elif pos=="b2":
        b2="X"

def IsOpen(space,PT=True):
    global claimed
    if space in claimed:
        if PT:
            print("That space is occupied!")
            return False
        elif not PT:
            return False
    else:
        return

def PTurn():
    global SelectedSpace
    SelectedSpace=input("Please choose an area to claim\f").lower()

def CPlace(Z,CA1,CA2,CA3,CB1,CB2,CB3,CC1,CC2,CC3):
    #I'm not making another wtf variable.
    if Z=="a1":
        return CA1
    elif Z=="a2":
        return CA2
    elif Z=="a3":
        return CA3
    elif Z=="b1":
        return CB1
    elif Z=="b2":
        return CB2
    elif Z=="b3":
        return CB3
    elif Z=="c1":
        return CC1

################ BOT?
# test code signing because it probably wont work
#Computer will try to claim these spaces on each turn. if the space is claimed, it will move to the next. 
#please send help https://xkcd.com/832_large/

#Bot Turn One
