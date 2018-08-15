readme = """
UNFUCKER: A BRAINFUCK EXECUTOR IN PYTHON
by KHEDRON
"""
logging = True
#Upon becoming more familiar with the language, I see now that this
#probably spells out a message of sorts
BFFILE = """
++++++++++[>+++++++>++++++++++>+++>+<<<<-]
>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.
"""
simplerBFFILE = """
+>++>+++>>>+++++--->++
"""
#1 2 3 0 0 0 2 3

fourTimesFive = """
++++[>+++++<-]++
"""
explain = """
Set [1] to 4
add 5 to [2], minus 1 from [1] (20)
add 2 more to 20, make it 22
return
"""

def locateEndLoop(text):
    n = len(text)-1
    while n > 0:
        if text[n] == "]":
            found = n
        n -= 1
    return text[:found]


def compileWithSimeplCharacters(file):
    cells = [0]
    pointer = 0
    legals = ["+", "-", "[", "]", ">", "<"]

    t = 0
    while t < len(file):
        n = file[t]

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
        elif n == ".":
            print cells[pointer]
        elif n == ",":
            print "INPUT VALUE FOR CELL", pointer, ":",
            cells[pointer] = int(raw_input())

        elif n == "[":
            return cells[pointer]


        if n in legals:
            if logging:
                print n, "tick", cells #console for debugging
        else:

        t+= 1
    return cells


def handleLoops():
    flagpoint = cells[pointer]
    isolatedLoopRoutine = locateEndLoop(file[t+1:])
    while flagpoint > 0:
        cells += compileFucked(isolatedLoopRoutine)


print compileWithSimeplCharacters(simplerBFFILE)
