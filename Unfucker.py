readme = """
UNFUCKER: A BRAINFUCK EXECUTOR IN PYTHON
by KHEDRON
"""

#I think this is a fibonacci series or something, I forget now
BFFILE = """
++++++++++[>+++++++>++++++++++>+++>+<<<<-]
>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.
"""

simplerBFFILE = """

+>++>+++>>>+++++--->++++-
"""
#1 2 3 0 0 0 2 3

def convertFile(file):

    cells = [0]
    pointer = 0
    legals = ["+", "-", "[", "]", ">", "<"]

    for n in file:

        if n == "+":
            cells[pointer] +=1
        elif n == "-":
            cells[pointer] -=1
        elif n == ">":
            if (pointer >= len(cells)-1):
                cells.append(0)
            pointer +=1
        elif n == "<":
            pointer -=1
        if n in legals:
            print n, "tick", cells #console for debugging

        else:
            fish = "glub glub" #my favorite do-nothing statement
            #this will have to be changed to properly handle comments

convertFile(simplerBFFILE)
