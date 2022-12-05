Objective
One of the things an assembler has to do is take assembly language instructions (like ADD, AND, and JMP) and convert those into binary opcodes. Each assembly instruction has a corresponding 4-bit binary opcode. For example, the binary opcode for ADD is 0001, for AND it's 0101, and for JMP it's 1100.

Write an LC-3 assembly language program that does the following:

Output a message to the screen that prompts the user to type in an LC-3 assembly language instruction (like ADD). The user ends their input by pressing Enter/Return.
If the instruction typed by the user is a legal LC-3 assembly language instruction, your program displays the corresponding 4-bit opcode. For example, if the user types "ADD", the program would print out "0001".
If the instruction typed by the user is not a legal LC-3 assembly language instruction (for example,  "ADDD"), your program displays an appropriate error message.
After displaying the output, your program loops back to the top, reinitializes anything that needs to be reinitialized, and goes again.
Your program will exit when the user types the string "QUIT" and presses Enter/Return.