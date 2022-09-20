mov ti, 2000   ; Set ti = 2000
int 32         ; Sleep ti Miliseconds
int 16         ; Set ab to Last Key Press
mov aox, ad    ; Set X = ab
mov aoy, 1     ; Set Y = 1
mov aoc, #fff  ; Set Color = White
mov rrm, $FB   ; Set Shape = Full Block
int 21         ; Add The Shape To Screen
int 4          ; MainLoop