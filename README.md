# bf2
Brainfuck 2.0
To run the interpreter you don't need anything excluding python3.6 or higher
# instructions:
```
  ( begins code and ) ends code
  + adds 1 to the pointer
  - subtracts 1 from the pointer
  / appends the pointer to the stack
  < prints the stack in number format
  ; prints the stack in text format (converts numbers to ascii characters)
  | prints the pointer
  : prints the pointer in text format
  ^ prints newline
  > gets 1 character input from user
  . resets Program memory
  [ adds 10 to the pointer and ] subtracts 10 from the pointer
  _ removes the last item from stack
  ! resets the Pointer
  & resets the stack
  and * prints sum of the stack (useful for calcution programs)
  use program like this: python3 interpreter.py <scriptname>.bf2
```
