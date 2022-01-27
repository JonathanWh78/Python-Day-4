# Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
# Print out the edited file line by line.

openedfile = open("teams.txt")
readfile = openedfile.readlines()
openedfile.close()
readfile.insert(0,"This is a new line\n")
openedfile = open("teams.txt","w")
openedfile.writelines(readfile)
openedfile.close()

perline = ""
for line in readfile:
    print(line)