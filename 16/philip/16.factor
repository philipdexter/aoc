USING: io prettyprint sequences kernel math splitting combinators
math.parser locals sequences.extras ascii system arrays fry ;
IN: 16


CONSTANT: start
    {
        CHAR: a
        CHAR: b
        CHAR: c
        CHAR: d
        CHAR: e
        CHAR: f
        CHAR: g
        CHAR: h
        CHAR: i
        CHAR: j
        CHAR: k
        CHAR: l
        CHAR: m
        CHAR: n
        CHAR: o
        CHAR: p
    }

:: span ( seq quot: ( elt -- ? ) -- whiletrueslice rest )
    seq quot take-while
    seq quot drop-while ; inline

:: s-command ( seq n -- newseq )
    0 16 n - seq subseq
    16 n - 16 seq subseq
    swap append ;

:: x-command ( seq x y -- seq' )
    x seq nth :> x'
    y seq nth :> y'
    x' y seq set-nth
    y' x seq set-nth
    seq
    ;

:: y-command ( seq a b -- seq' )
    seq [ a = ] find drop :> x
    seq [ b = ] find drop :> y
    x seq nth :> x'
    y seq nth :> y'
    x' y seq set-nth
    y' x seq set-nth
    seq
    ;

: step ( seq cmd -- seq )
    unclip {
        { CHAR: s [ string>number s-command ] }
        { CHAR: x [ [ digit? ] span rest-slice [ string>number ] bi@ x-command ] }
        { CHAR: p [ unclip-slice [ unclip-last-slice ] dip [ drop ] 2dip swap y-command ] }
    }
    case ;

: solve1 ( cmds seq -- seq )
    [ step ] reduce ;

:: step2 ( seq seen __ i cmds -- seq' seen' i' )
    cmds seq solve1 :> a
    seen [ second a = ] find swap drop [
        1000000001 i 1 + rem '[ first _ = ] seen swap find second write nl
        flush
        0 exit
    ] [
        a
        seen i a clone 2array suffix
        0
    ] if* ;

:: solve2 ( cmds seq -- seq )
    seq { } 1000000000 <iota> 0 [ cmds step2 ] reduce drop drop ;

: solve ( -- )
    lines first "," split dup start clone solve1 write nl start solve2 write ;

MAIN: solve
