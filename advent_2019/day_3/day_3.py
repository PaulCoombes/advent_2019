from collections import namedtuple

Coord = namedtuple('Coord', 'x y steps')

def map_wire(path):
    x = 0
    y = 0
    steps = 0
    wire = set()
    for p in path:
        direction = p[0]
        distance = int(p[1:])
        if direction == "R":
            end = x + distance
            while x < end:
                x += 1
                steps += 1
                wire.add(Coord(x, y, steps))
        if direction == "L":
            end = x - distance
            while x > end:
                x -= 1
                steps += 1
                wire.add(Coord(x, y, steps))
        if direction == "U":
            end = y + distance
            while y < end:
                y += 1
                steps += 1
                wire.add(Coord(x, y, steps))
        if direction == "D":
            end = y - distance
            while y > end:
                y -= 1
                steps += 1
                wire.add(Coord(x, y, steps))
    print(steps)
    return wire

def find_closest_crossed_wire(wire_1, wire_2):
    steps = []
    for w1 in wire_1:
        for w2 in wire_2:
            if w1.x == w2.x and w1.y == w2.y and not (w1.x == 0 and w1.y == 0):
                steps.append(w1.steps + w2.steps)

    return min(steps)


#Test Case 1
test_1 = map_wire('R8,U5,L5,D3'.split(','))
test_2 = map_wire('U7,R6,D4,L4'.split(','))
assert find_closest_crossed_wire(test_1, test_2) == 30

#Test Case 2
test_1 = map_wire('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','))
test_2 = map_wire('U62,R66,U55,R34,D71,R55,D58,R83'.split(','))
assert find_closest_crossed_wire(test_1, test_2) == 610

#Test Case 3
test_1 = map_wire('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','))
test_2 = map_wire('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','))
assert find_closest_crossed_wire(test_1, test_2) == 410

#Production
with open(r'day_3\input.txt', 'r') as f:
    wires = f.read().splitlines()

wire_1 = map_wire(wires[0].split(','))
wire_2 = map_wire(wires[1].split(','))
print(find_closest_crossed_wire(wire_1, wire_2))


