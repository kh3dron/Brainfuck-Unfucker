readme = """
UNFUCKER: A BRAINFUCK EXECUTOR IN PYTHON
by KHEDRON
"""
logging = True
#Upon becoming more familiar with the language, I see now that this
#probably spells out a message of sorts
numberList = """
+>++>+++>>>+++++--->++
"""

#A single loop
fourTimesFivePlusTwo = """
++++[>+++++<-]>++
"""

#Another single loop program
HelloWorld = """
++++++++++[>+++++++>++++++++++>+++>+<<<<-]
>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.
"""

#multiple levels of loops, current challenge
fib = """
+++++[->----[---->+<]>++.-[++++>---<]>.++.---------.+++.[++>---<]>--.++[->+++<]>.+++++++++..---.+++++++.+[-->+++++<]>-.<]
"""


def locateEndLoop(text):
    n = len(text)-1
    while n > 0:
        if text[n] == "]":
            found = n
            break
        n -= 1
    return text[:found]

def recursableCompiling(file, cells, pointer):
    print "Currently compiling\n", file

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
            isolatedLoop = locateEndLoop(file[t+1:])
            while cells[pointer] > 1:
                cells = recursableCompiling(isolatedLoop, cells, pointer)

        if n in legals:
            if logging:
                print n, "tick", cells #console for debugging
            else:
                fish = "glub glub"
        t+= 1
    return cells

print recursableCompiling(fib, [0], 0)
