IN: part1
USING: kernel sequences io assocs math prettyprint ;

: solve ( str -- str )
    ! create a version of the input with the first char appended to
    ! the end
    dup 0 over nth suffix
    ! and then remove the first char
    0 swap remove-nth
    ! zip the original and the modified together
    zip
    ! for each pair of chars, if they're equal then output a single
    ! copy of the value, if not then output a 0
    [
        [ 0 swap nth dup ]
        [ 1 swap nth ] bi
        =
        ! subtract the char '0' to get the int value
        [ CHAR: 0 - ]
        [ drop 0 ] if
    ] map
    sum
    ;

: go ( -- ) [ solve . ] each-line ;

MAIN: go
