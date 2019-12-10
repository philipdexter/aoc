USING: sorting combinators sequences splitting sets prettyprint io math kernel ;
IN: 1

: valid-passphrase-1 ( arr -- ? ) all-unique? ;

: valid-passphrase-2 ( arr -- ? ) [ natural-sort ] map all-unique? ;

: solve ( -- )
    lines [ " " split ] map
    0 swap [ valid-passphrase-1 1 0 ? + ] each . ;

MAIN: solve
