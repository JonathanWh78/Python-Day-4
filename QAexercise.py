#Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
#Reads and displays the names of the 1st and 4th team in the file.


openedfile = open("teams.txt")
readfile = openedfile.readlines()
#print (readfile)
openedfile.close()
readfile.insert("\nManchester United\n""\nManchester City\n""\nLeeds\n""\nLiverpool\n""\nChelsea\n")
openedfile = open("teams.txt","w")
openedfile.writelines(readfile)
openedfile.close()