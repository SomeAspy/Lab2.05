#Aiden B.
#Lab2.05
#3/9/2021
#
#   info:
#   underline in unicode \u0332
#   THIS USES EXEC AND IS THEREFORE BAD PRACTICE!!
#   convert to dictionary when I'm actually good maybe...
#
#   BOARD
#
#   A1|A2|A3
#   B1|B2|B3
#   C1|C2|C3
#
#   init
boardFormat=""
a1=a2=a3=b1=b2=b3=c1=c2=c3=" "
LastSet=True

def refresh():
    board="\n "+a1+"|"+a2+"|"+a3+"\n "+b1+"|"+b2+"|"+b3+"\ne "+c1+"|"+c2+"|"+c3
    global LastSet,boardFormat
    for i in board:
        if i=="e":LastSet=False
        elif LastSet:boardFormat+=i+"\u0332"
        elif LastSet==False:boardFormat+=i
    print(boardFormat)

print("How To Play:\nSpots on the board are named A1-C3, with A being the top row and C being the bottom.")

SelectedSpace=input("Please choose an area to claim\f").lower()

exec(SelectedSpace+'="X"')

refresh()