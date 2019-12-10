USING: accessors kernel locals math sequences prettyprint io ;
IN: 17

CONSTANT: input 17
TUPLE: state list length pos ;

: <state> ( list length pos -- state )
    state boa ;

:: go ( state x i -- newstate )
    state pos>> i + state length>> mod 1 + :> p'
    x 1 + p' state list>> insert-nth
    state length>> 1 +
    p'
    <state> ;

: finish ( state -- i )
    list>>
    [ [ drop 2017 = ] find-index drop ] keep
    [ 1 + ] dip nth ;

:: solve ( i -- y )
    2017 <iota> { 0 } 1 0 state boa [ i go ] reduce finish ;

:: go2 ( state x i -- newstate )
    state pos>> i + state length>> mod 1 + :> p'
    p' 2 < [ x 1 + p' state list>> insert-nth ] [ state list>> ] if
    state length>> 1 +
    p'
    <state> ;

: finish2 ( state -- i )
    list>> second ;

:: solve2 ( i -- y )
    50000000 <iota> { 0 } 1 0 state boa [ i go2 ] reduce finish2 ;
