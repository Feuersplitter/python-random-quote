f = open("quotes.txt", "a")
f.write("\n")
userinput = input('Add a new quote: ')
f.write(userinput)
f.close