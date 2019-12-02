def parse_program(prog: int):
    for i in range(0,len(prog),4):
        operator = prog[i + 0]

        if operator == 1:
            prog[prog[i+3]] = prog[prog[i + 1]] + prog[prog[i + 2]]
        elif operator == 2:
            prog[prog[i+3]] = prog[prog[i + 1]] * prog[prog[i + 2]]
        elif operator == 99:
            exit
        else:
            exit

    return prog

assert(parse_program([1,9,10,3,2,3,11,0,99,30,40,50])) \
    == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
assert(parse_program([1,0,0,0,99])) == [2,0,0,0,99]
assert(parse_program([2,3,0,3,99])) == [2,3,0,6,99]
assert(parse_program([2,4,4,5,99,0])) == [2,4,4,5,99,9801]
assert(parse_program([1,1,1,4,99,5,6,0,99])) == [30,1,1,4,2,5,6,0,99]

with open(r'day_2\input.txt', 'r') as f:
    start_mem = list(map(int, f.read().split(",")))

    for noun in range(0,100):
        for verb in range(0,100):
            test_mem = list(start_mem)
            test_mem[1] = noun
            test_mem[2] = verb
            if parse_program(test_mem)[0] == 19690720:
                print(noun, verb)
