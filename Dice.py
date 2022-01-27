# Dice Class
# - Write a class called Dice
# - When initialised the object will set how many faces the die has
# - Create objects for 6, 20, 2 and 4 sided die.
# - Roll a charactor sheet for a Swashbuckler Rogue called 'Earl Grey' DnD 5th ed.

from random import randint


class Dice:
    def __init__(self, NoofFaces = 6):
        self.NoofFaces = NoofFaces

    def Roll(Die):
        rdmroll = randint (1, Die)
        return rdmroll

D2 = Dice.Roll(2)
D4 = Dice.Roll(4)
D6 = Dice()
D8 = Dice.Roll(8)
D10 = Dice.Roll(10)
D20 = Dice.Roll(20)
print (D6.NoofFaces)

D2 = Dice(2)
D4 = Dice(4)
D6 = Dice()
D8 = Dice(8)
D10 = Dice(10)
D20 = Dice(20)
print (D2.NoofFaces)

Roll = Dice.Roll(D2.NoofFaces)
print(Roll)
DSelect = int
while DSelect != 0:
    print("")
    print("-----------------------")
    print("Press 1: To Flip A Coin")
    print("Press 2: To Roll A D4")
    print("Press 3: To Roll A D6")
    print("Press 4: To Roll A D8")
    print("Press 5: To Roll A D10")
    print("Press 6: To Roll A D20")
    print("Press 0: To Quit")
    print("-----------------------")
    print("")
    DSelect = int(input("Please Select An Option: "))
    print("")
    if DSelect == 1:
        Roll = Dice.Roll(D2.NoofFaces)
        if Roll == 1:
            print("-----------------------------------------")
            print ("Result: You Flipped A Coin And Got Heads")
            print("-----------------------------------------")
        elif Roll == 2:
            print("-----------------------------------------")
            print ("Result: You Flipped A Coin And Got Tails")
            print("-----------------------------------------")
    elif DSelect == 2:
        Roll = Dice.Roll(D4.NoofFaces)
        print("-----------------------------------------------")
        print ("Result: You Rolled a D4 And Got A: " +str(Roll))
        print("-----------------------------------------------")
    elif DSelect == 3:
        Roll = Dice.Roll(D6.NoofFaces)
        print("-----------------------------------------------")
        print ("Result: You Rolled a D6 And Got A: " +str(Roll))
        print("-----------------------------------------------")
    elif DSelect == 4:
        Roll = Dice.Roll(D8.NoofFaces)
        print("-----------------------------------------------")
        print ("Result: You Rolled a D8 And Got A: " +str(Roll))
        print("-----------------------------------------------")
    elif DSelect == 5:
        Roll = Dice.Roll(D10.NoofFaces)
        print("------------------------------------------------")
        print ("Result: You Rolled a D10 And Got A: " +str(Roll))
        print("------------------------------------------------")
    elif DSelect == 6:
        Roll = Dice.Roll(D20.NoofFaces)
        print("------------------------------------------------")
        print ("Result: You Rolled a D20 And Got A: " +str(Roll))
        print("------------------------------------------------")

    elif DSelect == 0:
        print("-------------------")
        print ("Thanks For Playing")
        print("-------------------")
        print("")
    else:
        print("------------------------------------------")
        print ("Please Enter One Of The Specified Options")
        print("------------------------------------------")