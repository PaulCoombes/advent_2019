#param_mode 0 = position mode
#param_mode 1 = immediate mode
def parse_program(prog: int, input: int):
    i = 0
    while i <= len(prog):
        op_code = int(str(prog[i])[-2:])
        modes = get_modes(prog[i])

        #determine the parameters
        params =[0,0,0]
        if op_code in (1, 2, 3, 4, 5, 6, 7, 8):
            if modes[0] == 0:
                params[0] = prog[prog[i+1]]
            else:
                params[0] = prog[i+1]

        if op_code in (1, 2, 5, 6, 7, 8):
            if modes[1] == 0:
                params[1] = prog[prog[i+2]]
            else:
                params[1] = prog[i+2]

        if op_code in (7, 8):
            params[2] = prog[i+3]

        #print(str(i)+": "+ str(prog[i]) +" " + str(modes) + str(params))

        if op_code == 1:
            #addition
            prog[prog[i+3]] = params[0] + params[1]
            increment = 4
        elif op_code == 2:
            #multiplication
            prog[prog[i+3]] = params[0] * params[1]
            increment = 4
        elif op_code == 3:
            #save to position
            prog[prog[i+1]] = input
            increment = 2
        elif op_code == 4:
            #output from position
            output = params[0]
            increment = 2
        elif op_code == 5:
            #jump-if-true
            if params[0] != 0:
                increment = params[1] - i 
            else:
                increment = 3
        elif op_code == 6:
            #jump-if-false
            if params[0] == 0:
                increment = params[1] - i 
            else:
                increment = 3
        elif op_code == 7:
            #less than
            if params[0] < params[1]:
                prog[params[2]] = 1
            else:
                prog[params[2]] = 0

            increment = 4
        elif op_code == 8:
            #equals
            if params[0] == params[1]:
                prog[params[2]] = 1
            else:
                prog[params[2]] = 0

            increment = 4
        elif op_code == 99:
            #exit
            return(output)
        else:
            exit

        i += increment

    return 0

def get_modes(instr: int):
    instr = str(instr).zfill(5)
    modes = list(instr[0:3])
    modes = list(map(int, modes))
    modes.reverse()
    
    return modes

#test cases
assert(parse_program([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0) == 0)
assert(parse_program([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 1) == 1)
assert(parse_program([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0) == 0)
assert(parse_program([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 1) == 1)

test = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

assert(parse_program(list(test), 7) == 999)
assert(parse_program(list(test), 8) == 1000)
assert(parse_program(list(test), 9) == 1001)

#production ready
with open(r'day_5\input.txt', 'r') as f:
    start_mem = list(map(int, f.read().split(",")))
    print(parse_program(start_mem,5))
