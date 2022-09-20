# ManiC22
My own CPU (It's Just a Assembly Like Programming Language Interpreter)

### Table of Contents  
[Instructions](#Instructions)  
[Labels and Variables](#Labels_and_Variables)
<a name="Instructions"/>

## Instructions 
</a>

```R:``` Register or Variables  
```V:``` Value  
```N:``` name  
```I:``` Integer  
```L:``` Label

### mov
Change Data of a Variables or Register
```assembly
mov R, V
```
### int
Make a Syscall
```assembly
mov I
```
### pop
Deletes a Variables
```assembly
pop R
```
### math:
You can Do Math Like:
```assembly
add R, I  ; Add a number to a Variable or Register
sub V, I  ; Subtract a number to a Variable or Register
mul V, I  ; Multiplie a number to a Variable or Register
div V, I  ; Divide a number to a Variable or Register
```
### jump:
Jump to a Label when Some event Happens
```assembly
jmp L   ; Always Jump
je L    ; Jump when Equal
jne L   ; Jump when not Equal
jg L    ; Jump when Greater
jle L   ; Jump Not when Less(Jump when Greater or Equal)
jg L    ; Jump when Less
jle L   ; Jump Not when Greater(Jump when Less or Equal)
```
<a name="Labels_and_Variables"/>

## Labels and Variables
</a>

### Making a Label
Syntax For Making a Label is:
```assembly
_LableName:
    Instructions
```
