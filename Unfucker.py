readme = """
BRAINFUCK-UNFUCKER: A BRAINF#CK EXECUTOR AND VISUALIZER IN PYTHON
by KHEDRON
"""
#I'm going to assume this is better left on by default.
logging = True

#HAD TO BE FED the string the the [ at the BEGINNING.
def jumpUp(text):
    skips = 0
    clock = 0
    for n in text:
        clock += 1
        if n == "[":
            skips += 1
        elif n == "]":
            skips -= 1
            if skips == 0:
                break
    return clock -1

def jumpBack(text):
    skips = 0
    clock = 0
    for n in reversed(text):
        clock += 1
        if n == "[":
            skips -= 1
            if skips == 0:
                break
        elif n == "]":
            skips += 1
    clock -= 2
    return clock +1

def Compile(file):
    legals = ["+", "-", "[", "]", ">", "<"]
    cells = [0]
    pointer = 0
    t = 0

    while t < len(file):
        n = file[t]
        t+= 1

        #non-loop character handling is straightforward
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
            print "Input value for cell", pointer, ":",
            cells[pointer] = int(raw_input())

        elif n == "[":
            if cells[pointer] == 0:
                t += jumpUp(file[t:])
        elif n == "]":
            if cells[pointer] != 0:
                t -= jumpBack(file[:t])

        if (n in legals) & (logging):
            print "Instruction", t, "is", n, ", pointer index:", pointer, "cells:", cells

    return cells[pointer]

def clean(text):
    scrubbed = ""
    legals = ["+", "-", "[", "]", ">", "<", ".", ","]
    for n in text:
        if n in legals:
            scrubbed += n
    return n

def main():
  if len(sys.argv) == 2:
      Compile(clean(sys.argv[1]))
  else:
      print("Usage:", sys.argv[0], "filename")

#fact: once you use one of these in a python program you've made it
if __name__ == "__main__": main()
