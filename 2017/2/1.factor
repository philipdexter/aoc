USING: kernel math io sequences math.order splitting prettyprint math.parser ;
IN: 1

: maximum ( seq -- max ) dup first [ max ] reduce ;
: minimum ( seq -- min ) dup first [ min ] reduce ;
: remove-last ( seq -- seq ) dup length 1 - swap remove-nth ;
: strings>numbers ( seq -- seq ) [ string>number ] map ;

: solve ( seq -- int )
    [ strings>numbers ] map
    [ [ maximum ] map ]
    [ [ minimum ] map ] bi
    [ - ] 2map
    sum
    ;

: go ( -- ) lines [ "\t" split ] map solve . ;

MAIN: go
