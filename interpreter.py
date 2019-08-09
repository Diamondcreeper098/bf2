#Brainfuck 2.0 by Diamondcreeper098
#Github: github.com/Diamondcreeper098

#instructions:
# ( begins code and ) ends code
# + means add 1 to the pointer
# - means subtract 1 from the pointer
# / means append the pointer to the stack
# < means print the stack in number format
# ; means print the stack in text format (converts numbers to ascii characters)
# | means print the pointer
# : means print the pointer in text format
# ^ means print newline
# > means get 1 character input from user (text having more than 1 characters will have their first character read)
# . means reset Program memory
# [ means add 10 to the pointer and ] means subtract 10 from the pointer
# _ means remove the last item from stack
# ! means reset the Pointer
# & means reset the stack
# and * means sum of the stack (useful for calcution programs)
#use program like this: python3 interpreter.py <scriptname>.bf2

import sys

def main(code):
    began = False
    ptr = 0
    stack = list()
    cmdln = code.splitlines()
    for cmdd in cmdln:
        for cmd in cmdd:
            if cmd == '(':
                began = True
            elif cmd == ')':
                began = False
            else:
                if began == True:
                    if cmd == '+':
                        ptr = ptr +1
                    elif cmd == '-':
                        ptr = ptr -1
                    elif cmd == '/':
                        stack.append(ptr)
                    elif cmd == '<':
                        for i in stack:
                            print(i,end=' ')
                        print('\n')
                    elif cmd == ';':
                        for i in stack:
                            print(chr(i),end=' ')
                        print('\n')
                    elif cmd == '|':
                        print(ptr)
                    elif cmd == ':':
                        print(chr(ptr))
                    elif cmd == '^':
                        print('\n')
                    elif cmd == '>':
                        ptr = int(list(input("Enter single character and press enter: "))[0])
                    elif cmd == '.':
                        stack = list()
                        ptr = 0
                    elif cmd == '[':
                        ptr = ptr + 10
                    elif cmd == ']':
                        ptr = ptr - 10
                    elif cmd == '_':
                        stack.pop(len(stack)-1)
                    elif cmd == '!':
                        ptr = 0
                    elif cmd == '&':
                        stack = list()
                    elif cmd == '*':
                        x = 0
                        for i in stack:
                            x = x + i
                        print("Sum of the numbers is: " + str(x))
                    else:
                        print("Incorrect command")

if __name__ == '__main__':
    try:
        scrpath = sys.argv[1]
    except IndexError:
        scrpath = input("Enter Script path: ")
    code = open(scrpath,'r')
    print("Executing " + scrpath)
    main(code.read())
