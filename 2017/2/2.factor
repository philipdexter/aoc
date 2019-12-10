USING: kernel math io sequences math.order splitting prettyprint
    math.parser monads locals ;
IN: 1

:: divides-evenly ( x y -- maybe )
    x y max
    x y min
    2dup
    mod
    0 =
    [ / maybe-monad return ]
    [ drop maybe-monad fail ] if
    ;

: process ( x seq -- seq )
    [ over divides-evenly ] map swap drop ;

: by2 ( seq -- seq )
    dup empty?
    [ drop { } ]
    [ dup
      first swap 0 swap remove-nth swap over
      process
      swap
      by2
      append ] if
    ;

: strings>numbers ( seq -- seq ) [ string>number ] map ;

: solve ( seq -- int )
    [ strings>numbers ] map
    [ by2 ] map
    [ 0 [ [ + ] [ ] if-maybe ] reduce ] map sum
    ;

: go ( -- ) lines [ "\t" split ] map solve . ;

MAIN: go
