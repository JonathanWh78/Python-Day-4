# Lettercheck
# - write a class called 'Lettercheck'
# - create an attribute called vowels and fill it with vowels
# - create a method that takes a single letter and checks if it is a vowel
# - return true or false
# - rewrite the class so you can create different objects for finding if letters are members of different letter groups


#Class to check if its a vowel
class lettercheck:
    def checker(UInput):
        vowellst = ["A","E","I","O","U"]
        if UInput in vowellst:
             output = True
             return output
        else:
            output = False
            return output
#class to check for roman numerals
    def romanchecker(UInput):
        Roman = ["I","V","X","L","C","D","M"]
        if UInput in Roman:
             outputR = True
             return outputR
        else:
            outputR = False
            return outputR

#loop to make more fun
#added roman numeral checks
UInput = str
while UInput != "QUIT":
    print ("-----------------------------------------------------------")
    print ("")
    print ("Enter A Letter, Any Letter You Want!")
    print ("If You Want To Quit Type: Quit")
    print ("")
    UInput = str(input ("Enter A Letter You Want To Check If It's A Vowel Or Roman Numeral: ").upper())
    print ("-----------------------------------------------------------")
    if UInput == "QUIT":
        print ("")
        print ("---------------------------")
        print ("Quiting, Thanks For Playing")
        print ("---------------------------")        
        print ("")
        exit()
    elif lettercheck.checker(UInput) == True:
        print ("")
        print ("-------------------------------------------------------")
        print ("The Letter You Entered: " + UInput + "," + " Is A Vowel")
        print ("-------------------------------------------------------")
        print ("")
    elif lettercheck.checker(UInput) == False:
        print ("")
        print ("-----------------------------------------------------------")
        print ("The Letter You Entered: " + UInput + "," + " Is NOT A Vowel")
        print ("-----------------------------------------------------------")
        print ("")
    if lettercheck.romanchecker(UInput) == True:
        print ("")
        print ("---------------------------------------------------------------")
        print ("The Letter You Entered: " + UInput + "," + " Is A Roman Numeral")
        print ("---------------------------------------------------------------")
        print ("")
    elif lettercheck.romanchecker(UInput) == False:
        print ("")
        print ("-------------------------------------------------------------------")
        print ("The Letter You Entered: " + UInput + "," + " Is NOT A Roman Numeral")
        print ("-------------------------------------------------------------------")
        print ("")