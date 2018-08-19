## BRAINFUCK-UNFUCKER: A BRAINF#CK EXECUTOR AND VISUALIZER IN PYTHON ##
by KHEDRON

This program can execute scripts written in Brainf#ck, and provide some simple console logging for visualization into how the code is running. 


**WHAT IS BRAINF#CK?**

Brainf#ck is a [Turing Complete](https://en.wikipedia.org/wiki/Turing_completeness) [Esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language); which means it was designed to *look* like a complete mess while still being completely functional. Designed in 1964, it's actually very old for a programming language.

**HOW DO BRAINF#CK PROGRAMS WORK?**

To understand how Brainf#ck works, we'll need to understand the hardware it was designed to work on. These early computers, known as [Turing machines](https://en.wikipedia.org/wiki/Turing_machine), have two core parts:

- A Work Tape, which is a list of spaces to hold values. (The predecessor to RAM, or Memory)
- A Read/Write Head, which can read the value held at a spot in the work tape, or change the value in that tape. 

Each character in a Brainf#ck program modifies the tape and pointer system, described above. 
Brainf#ck programs consist of only 8 characters. 

- The < and > characters, which move the pointer along the tape in either direction
- The + and - characters, which increase or decrease the value of the current cell by one
- The . and , characters, which will print the current cell OR ask the user to input a value that will become the current cell
- The [ and ] characters, which contain loops. When a loop has completed running, the current cell will be evaluated; if the cell holds a 0, the loop ends, and the program passes the ] and runs the next code. If the cell holds a value other than 0, the program will go back to the start of the loop, at the [, and re-run the looped code, until reaching the end again, where it will re-evaluate. 

**WHAT DOES THIS PROGRAM DO?**

This program can open a .bf file as an argument, execute it, and show the result. (The "result" of a BF file is whatever number is contained in the cell the pointer ends the program on.) At the top of the program is a `Logging = False` line, which, if set to `True`, will display the state of the tape and some other variables as the program is run. 

In this repository, the folder `sample_bf_files` has some simple bf files to try. There's one with no loops, a single loop, multiple loops, and a Fibonacci series generator. The one called `all_loop_interactions`, is the most complex, with loops both within each other and next to each other; this was the test file I used to check that my loop handling was perfect while writing this program. 

**CHALLENGES WITH WRITING THIS PROGRAM**

Brainf#ck is not a commonly used language, because of its obvious inefficiency and esoteric nature. Because of this, it's mostly used as a party trick of sorts in CTFs and similar showoff-y ways. This has led to some disagreements in how the language should work, for example:

- How long should the tape be? 256 cells, 10,000, 30,000, infinitely long?
- Where should the pointer start? On the leftmost side of the tape, or somewhere in the middle?
- What happens if the pointer is moved leftwards when it's in the leftmost cell? Does the pointer wrap around, or is a new cell added?
- What happens when a cell holding a zero is subtracted from? Does it go to 255, or negative numbers? Can cells only hold 8 bit numbers?

With so many different ways to interpret the language, I've made some of the most common assumptions and/or simplifications. The pointer cannot be moved leftwards at the leftmost cell. If moved right on the rightmost cell, a new cell is added. If a 0 cell is subtracted from, the cell becomes negative. Both the length of the tape and the value in a cell are big enough for the vast majority of programs. If you're writing a program and these limitations are in your way, you should consider either optimizing your code or choosing a more cooperative programming language.


**SOFTWARE LICENSE**

lol.