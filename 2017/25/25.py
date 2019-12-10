print 'hello'

steps = 12994925 # 12317297

a, b, c, d, e, f = range(6)
left, right = 0, 1

tm = {
    (a, 0): (1, right, b),
    (a, 1): (0, left, f),

    (b, 0): (0, right, c),
    (b, 1): (0, right, d),

    (c, 0): (1, left, d),
    (c, 1): (1, right, e),

    (d, 0): (0, left, e),
    (d, 1): (0, left, d),

    (e, 0): (0, right, a),
    (e, 1): (1, right, c),

    (f, 0): (0, left, a),
    (f, 1): (1, right, a),
}

tape = {}
head, state = 0, a

for i in xrange(steps):
    val = tape.get(head, 0)
    wval, move, nextstate = tm.get((state, val))
    def f(a):
        return -1 if a == left else 1
    def g(a):
        return "abcdef"[a]
    print wval, f(move), g(nextstate)

    tape[head] = wval
    head = head+1 if move == right else head-1
    state = nextstate

print sum(tape.values())
