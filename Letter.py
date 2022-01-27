# Lettercheck
# - write a class called 'Lettercheck'
# - create an attribute called vowels and fill it with vowels
# - create a method that takes a single letter and checks if it is a vowel
# - return true or false
# - rewrite the class so you can create different objects for finding if letters are members of different letter groups



class lettercheck:
    def checker(UInput):
        if UInput == "A" or UInput == "E" or UInput == "I" or UInput == "O" or UInput == "U":
             output = True
             return output
        else:
            output = False
            return output

UInput = str
while UInput != "QUIT":
    print ("-----------------------------------------------------------")
    print ("")
    print ("Enter A Letter, Any Letter You Want!")
    print ("If You Want To Quit Type: Quit")
    print ("")
    UInput = str(input ("Enter A Letter You Want To Check If It's A Vowel: ").upper())
    print ("-----------------------------------------------------------")
    if UInput == "QUIT":
        print ("")
        print ("---------------------------")
        print ("Quiting, Thanks For Playing")
        print ("---------------------------")
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