i: db 10
mov aox, 15
mov aoy, 15
mov rrm, $BDU
_t:
    add aox, 5
    int 21
    cmp aox, 40
    jl _t
mov rrm, $BDR
int 21
mov aoy, 30
jmp _t
mov aox, 20
mov rrm, $BDL
int 21
mov aox, 40
mov aoy, 25
mov rrm, $BDD
int 21
mov rrm, $BDR
int 21
int 4