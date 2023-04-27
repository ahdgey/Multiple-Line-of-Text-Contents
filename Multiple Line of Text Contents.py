#Alexza Jean R. Catanoy
#BSCPE 1-4
#Multiple Line of Text Contents

#Title
print("\033[0;36m*" * 90)
print("\033[1;97mA Method in Python to Write Multiple Line of Text into a Text File".center(97))
print("\033[0;36m*" * 90)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4")
print("-" * 90)

def text ():

#Open My Life.txt (read) and then write text_input as the mode
    with open("My Life.txt", "w") as text_input:

        #To constantly run the program block, apply the while loop
        while True:
            line = input("Enter line: ")

        #In My Life.txt, write the input
            text_input.write(line + "\n")
            add_line = input("Are there more line y/n? ")
            if add_line.lower() != "y":
                break

#Output, print the texts
    print("Inputted lines: ")
    with open("My Life.txt") as text_input:

        #Read every line
        for line in text_input:
            print(line.strip())

text()