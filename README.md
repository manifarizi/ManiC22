# ManiC22
My own CPU (It's Just a Assembly Like Programming Language Interpreter)

### Table of Contents  
0 - [Instructions](#Instructions)  
* [Math](#Math)
* [Jumps](#Jump)

1 - [Labels and Variables](#Labels_and_Variables)  
2 - [IF](#IF)  
3 - [SysCalls](#Sys_Calls)
<a name="Instructions"/>

## Instructions 
</a>

```R:``` Register or Variables  
```V:``` Value  
```N:``` Name  
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
<a name="Math"/>

### math:
</a>

You can Do Math Like:

```assembly
add R, I  ; Add a number to a Variable or Register
sub V, I  ; Subtract a number to a Variable or Register
mul V, I  ; Multiplie a number to a Variable or Register
div V, I  ; Divide a number to a Variable or Register
```
<a name="Jump"/>

### jump:
</a>

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
You Can Jump To a Location With 

<a name="IF"/>

## IF(CMP)
</a>

You Can Use if with CMP

Syntax:

```
cmp V, V
```

and then You can Use [Jump Commands](#Jump)

Example:

```

cmp 1, 1   ; if
je _1equ1  ; 1 == 1: jump _1equ1
```

<a name="Sys_Calls"/>

## SysCalls
</a>

### 10: Add a Pixel

Add a Pixel at X: ```aox``` Y: ```aoy``` with color: ```aoc```

Example:
```assembly
mov aox, 10    ; Set X = 10
mov aoy, 40    ; Set Y = 40
mov aoc, #fff  ; Set Color = White
int 10         ; Draw The Pixels
```

### 21: Add a Group of Pixels

Add a Group of Pixel from Rom with Name: ```rrm``` at X: ```aox``` Y: ```aoy``` with Color: ```aoc```

Example:
```assembly
mov aox, 10    ; Set X = 10
mov aoy, 40    ; Set Y = 40
mov aoc, #fff  ; Set Color = White
mov rrm, $A    ; Set Pixels = A
int 21         ; Draw The Pixels
```

### 32: Sleep
Sleep Time: ```ah``` Miliseconds

Example:
```assembly
mov ti, 2000   ; Set ti = 2000
int 32         ; Sleep ti Miliseconds
```

### 4: MainLoop
When MainLoop is Happening You Cant Change Anything and User Needs to Close The Window To Exit From MainLoop

Example:
```assembly
int 4  ; MainLoop
```
### 128: Exit
Exits The Programm

Example:
```assembly
int 128  ; Exit
```
### 8: CMP Last Key Press
Returns Last Pressed Key and You Can ```cmp``` the Key Code

Example:
```assembly
mov ti, 2000  ; Set ti = 2000
int 32        ; Sleep ti Miliseconds
mov ah, 0     ; Set ah to 0
int 8         ; Set CMP to [Last Key Press, ah]
jne _Pressed  ; If not Key == 0(a Key Was Pressed): Jump To Label 'Pressed'
```

### 16: Keyboard Getch
Get Last Key Press in ```ad``` Register

Example:
```assembly
mov ti, 2000   ; Set ti = 2000
int 32         ; Sleep ti Miliseconds
int 16         ; Set ab to Last Key Press
mov aox, ad    ; Set X = ab
mov aoy, 1     ; Set Y = 1
mov aoc, #fff  ; Set Color = White
mov rrm, $FB   ; Set Shape = Full Block
int 21         ; Add The Shape To Screen
int 4          ; MainLoop
```
### 2: Clear
Clear The Screen

Example:
```assembly
int 2  ; Clear The Screen
```