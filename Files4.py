#working code to remove all from readme and replace with the same but upper

openedfile = open("README.md")
readfile = openedfile.read()
print (readfile)
openedfile.close()

upper = readfile.upper() #can be interchanged with upper or lower
openedfile = open("README.md","w")
openedfile.write(upper)
openedfile.close()

#inserts text

# #inserting files
# openedfile = open("README.md")
# readfile = openedfile.readlines()
# print (readfile)
# openedfile.close()
# readfile.insert(8,"\ninserted line\n")
# openedfile = open("README.md","w")
# openedfile.writelines(readfile)
# openedfile.close()