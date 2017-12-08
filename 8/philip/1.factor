USING: math locals sequences kernel io prettyprint hashtables
math.parser assocs splitting combinators math.order namespaces ;
IN: 1

:: ensure-var ( vars var -- )
    var vars at* [ drop ] [ drop 0 var vars set-at ] if ;

: != ( x y -- ? ) = not ;

: >word ( str -- word )
    { { "==" [ \ = ] }
      { "<" [ \ < ] }
      { ">" [ \ > ] }
      { "!=" [ \ != ] }
      { ">=" [ \ >= ] }
      { "<=" [ \ <= ] }
      { "inc" [ \ + ] }
      { "dec" [ \ - ] } } case ;

:: run ( seq vars quot -- )
    seq
    unclip               :> v1
    unclip >word         :> cmd
    unclip string>number :> amt
    unclip                  drop
    unclip               :> v2
    unclip >word         :> cmp
    unclip string>number :> i
    drop
    { v1 v2 } [ vars swap ensure-var ] each
    v2 vars at i cmp execute( x y -- ? )
    [ v1 vars at amt cmd execute( x y -- z ) v1 vars quot call( x y z -- ) ] when ;

: solve ( -- )
    H{ }
    lines [ " " split over [ set-at ] run ] each
    values 0 [ max ] reduce . ;

SYMBOL: o-max

: o-set-at ( value key assoc -- )
    pick
    o-max get max o-max set
    set-at ;

: solve2 ( -- )
    0 o-max set
    H{ }
    lines [ " " split over [ o-set-at ] run ] each drop
    o-max get . ;

MAIN: solve2
