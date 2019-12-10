tape = [0]
cursor = 0 # right: +1, left: -1
states = {
    'a':[[1,+1,'b'],[0,-1,'f']],
    'b':[[0,+1,'c'],[0,+1,'d']],
    'c':[[1,-1,'d'],[1,+1,'e']],
    'd':[[0,-1,'e'],[0,-1,'d']],
    'e':[[0,+1,'a'],[1,+1,'c']],
    'f':[[1,-1,'a'],[1,+1,'a']]
}

step_limit = 12994925
i = 0
s = 'a'
while i<step_limit:
    nv,dc,ns = states[s][tape[cursor]]
    print nv, dc, ns
    tape[cursor]=nv
    cursor+=dc
    if cursor==-1:
        cursor=0
        tape.insert(0,0)
    elif cursor==len(tape):
        tape.append(0)
    s = ns
    i+=1

print sum(tape)
