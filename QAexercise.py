#Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
#Reads and displays the names of the 1st and 4th team in the file.


openedfile = open("teams.txt")
readfile = openedfile.readlines()
openedfile.close()
#readfile.insert(1,"Manchester United\n""\nManchester City\n""\nLeeds\n""\nLiverpool\n""\nChelsea\n") # commented out as testing the correct output
print(readfile[1])
print(readfile[7])
openedfile = open("teams.txt","w")
openedfile.writelines(readfile)
openedfile.close()