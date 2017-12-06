USING: kernel math sequences io prettyprint locals sets
       sequences.extras math.functions splitting math.parser ;
IN: blah2

:: distribute ( seq amount idx -- )
    seq length :> l
    amount l / floor :> rounds
    amount l mod :> leftover
    seq [ rounds + ] map! drop
    idx 1 +
    dup leftover +
    dup <iota> <slice>
    [ l mod ] map
    [| i | i seq nth 1 + i seq set-nth ] each ;

:: step-it ( seen seq steps -- seen seq steps )
    seq arg-max :> idx
    idx seq nth :> to-give
    0 idx seq set-nth
    seq to-give idx distribute
    seen seq steps 1 + ;

:: done? ( seen seq steps -- ? )
    seq seen [ first ] map in? ;

:: record-step ( seen seq steps -- seen seq steps )
    seen { } seq clone suffix steps suffix suffix seq steps ;

:: finish ( seen seq steps -- answer )
    seen [ first seq = ] find swap drop second
    steps swap - ;

: solve ( seen seq steps -- steps )
    step-it
    3dup done?
    [ finish ] [ record-step solve ] if ;

: go ( -- )
    { }
    lines first "\t" split [ string>number ] map
    0
    solve . ;

MAIN: go
