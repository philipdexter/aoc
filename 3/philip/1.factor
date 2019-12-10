
USING: kernel math prettyprint combinators locals ;
IN: 1

SYMBOLS: R U D L ;

: next-direction ( dir -- dir )
    {
        { R [ U ] }
        { U [ L ] }
        { L [ D ] }
        { D [ R ] }
    }
    case ;


: dist-magnitude-change ( dist dir -- dist )
    {
        { R [ 0 ] }
        { U [ 1 ] }
        { L [ 0 ] }
        { D [ 1 ] }
    }
    case + ;

: move-step ( dir -- xquot yquot )
    {
        { R [ [ + ] [ drop ] ] }
        { U [ [ drop ] [ + ] ] }
        { L [ [ - ] [ drop ] ] }
        { D [ [ drop ] [ - ] ] }
    }
    case ;

:: one-step ( x y dir -- x y )
    dir move-step
    y swap 1 swap call( x x -- x )
    swap x swap 1 swap call( x x -- x ) ;

:: find-target ( x y dist dir -- x y )
    dir move-step
    y swap dist swap call( x x -- x )
    swap x swap dist swap call( x x -- x ) ;

:: at-target? ( x y a b -- ? )
    x a =
    y b =
    and ;

: move-until ( x y target -- x y )
    4dup at-target?
    at-target?
    [ move-

:: move ( x y dist dir -- x y )
    x y dist dir find-target
    x y move-until ;
