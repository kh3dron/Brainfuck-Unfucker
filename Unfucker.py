readme = """
UNFUCKER: A BRAINFUCK EXECUTOR IN PYTHON
by KHEDRON

Use for any and all purposes!
"""
#I'm going to assume this is better left on by default.
logging = False

#HAD TO BE FED the string the the [ at the BEGINNING.
def jumpUp(text):
#    print "Jumping up on", text,
    skips = 0
    clock = 0
    for n in text:
        #print clock, n
        clock += 1
        if n == "[":
            skips += 1
        elif n == "]":
            skips -= 1
            if skips == 0:
                break
        #print "skips at", skips
    #print "found clock of ", clock
    return clock -1
#HAS TO BE FED the string with the ] at the END.
def jumpBack(text):
    #print "Jumping back on", text,
    skips = 0
    clock = 0
    for n in reversed(text):
        clock += 1
        #print clock, n
        if n == "[":
            skips -= 1
            if skips == 0:
                break
        elif n == "]":
            skips += 1
        #print "skips at", skips
    clock -= 2
    #print "found clock of", clock
    return clock +1

def Compile(file):
    legals = ["+", "-", "[", "]", ">", "<"]
    cells = [0]
    pointer = 0
    t = 0

    while t < len(file):
        n = file[t]
        t+= 1


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
            print "Instruction", t, "is", n, ", pointer index:", pointer, cells

    return cells

#untested...
def clean(text):
    scrubbed = ""
    legals = ["+", "-", "[", "]", ">", "<"]
    for n in text:
        if n in legals:
            scrubbed += n
    return n

#This bit of logic borrowed from a similar project
def main():
  if len(sys.argv) == 2:
      Compile(sys.argv[1])
  else:
      print("Usage:", sys.argv[0], "filename")
      #ya dingus

file = '''+>+<[[>>>+<<<-]>[>+>+<<-]>.]'''

print Compile(file)

#fact: once you use one of these in a python program you've made it
#if __name__ == "__main__": main()
