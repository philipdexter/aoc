USING: sorting combinators sequences splitting sets prettyprint io math kernel ;
IN: 1

: valid-passphrase-1 ( arr -- ? ) all-unique? ;

: valid-passphrase-2 ( arr -- ? ) [ natural-sort ] map all-unique? ;

: bool>int ( ? -- x ) {
        { f [ 0 ] }
        { t [ 1 ] }
    } case ;

: solve ( -- )
    lines [ " " split ] map
    [ valid-passphrase-2 bool>int ] map sum . ;

MAIN: solve
