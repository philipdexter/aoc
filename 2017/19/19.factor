USING: io kernel prettyprint sequences accessors math combinators
locals arrays system tools.annotations namespaces ;
IN: 19

TUPLE: point x y ;
SYMBOLS: up down left right ;

: find-start-index ( arr -- point )
    first [ drop CHAR: | = ] find-index drop 0 point boa ;

: pat ( arr point -- char )
    [ x>> ] [ y>> ] bi rot nth nth ;

: next ( point dir -- point )
    swap clone swap
    { { up [ dup y>> 1 - >>y ] }
      { down [ dup y>> 1 + >>y ] }
      { left [ dup x>> 1 - >>x ] }
      { right [ dup x>> 1 + >>x ] }
    } case ;

:: find-next ( arr point dir -- point dir )
    dir
    { { up [ point left next dup arr swap pat 32 = [ drop point right next right ] [ left ] if ] }
      { down [ point left next dup arr swap pat 32 = [ drop point right next right ] [ left ] if ] }
      { left [ point up next dup arr swap pat 32 = [ drop point down next down ] [ up ] if ] }
      { right [ point up next dup arr swap pat 32 = [ drop point down next down ] [ up ] if ] }
    } case ;

SYMBOL: steps

:: step ( arr point dir -- point dir )
    arr point pat
    {
        { CHAR: | [ point dir next dir ] }
        { CHAR: - [ point dir next dir ] }
        { CHAR: + [ arr point dir find-next  ] }
        [ 1array write nl point dir next dir ]
    } case ;

:: ensure-in ( arr point -- )
    point y>> 0 >=
    point y>> arr length <
    point x>> 0 >=
    point x>> 1 arr nth length <
    and and and
    [ ] [ steps get . flush 0 exit ] if ;


:: go ( arr point dir -- )
    arr point ensure-in
    arr point pat 32 = [ ] [ steps get 1 + steps set ] if
    arr dup point dir step go ;

: solve ( -- )
    0 steps set
    lines dup find-start-index down go ;

MAIN: solve
