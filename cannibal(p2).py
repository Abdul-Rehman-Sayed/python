lM = lC = 3 # M is Monk (Missionary) and C is Cannibal
rM = rC = 0
print("\nM M M C C C | --- | \n")


def get_input():
    uM = int(input("Enter number of Missionaries traveling: "))
    uC = int(input("Enter number of Cannibals traveling: "))

    if 0 < (uM + uC) <= 2: # Boat should carry 1 or 2 people
        return uM, uC
    else:
        print("Invalid input! The boat must carry 1 or 2 people.")


def display():
    print("\n" + "M " * lM + "C " * lC + "| --- | " + "M " * rM + "C " * rC + "\n")

def move(uM, uC, direction):
    global lM, lC, rM, rC
    if direction == "LtoR":
        lM -= uM
        lC -= uC
        rM += uM
        rC += uC
    else:
        lM += uM
        lC += uC
        rM -= uM
        rC -= uC
# Check for invalid moves
    if lM < 0 or lC < 0 or rM < 0 or rC < 0:
        print("Invalid move: Not enough people on the side to move!")
        exit()
# Check if cannibals outnumber missionaries
    if (lM > 0 and lM < lC) or (rM > 0 and rM < rC):
        print("Cannibals eat missionaries: You lost the game!")
        exit()
# Winning condition
    if rM + rC == 6:
        print("You won the game!")
# Game loop
while (rM + rC) < 6:
    print("Left side -> Right side river travel")

    uM, uC = get_input()
    move(uM, uC, "LtoR")
    display()
    if rM + rC == 6: # If game is won, stop asking for return move
        break
    print("Right side -> Left side river travel")
    uM, uC = get_input()
    move(uM, uC, "RtoL")
    display()