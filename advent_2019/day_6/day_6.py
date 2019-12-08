
with open(r'day_6\input.txt', 'r') as f:
    objects = {}
    object = [o.split(')') for o in f.read().splitlines()]

for parent, child in object:
    objects[child] = parent

def count_orbits(obj: str):
    if obj in objects:
        return 1 + count_orbits(objects.get(obj))
    else:
        return 0

print(sum(count_orbits(c) for c in objects))

def calc_orbits(obj, jumps):
    if obj in objects:
        jumps[obj] = len(jumps)
        calc_orbits(objects.get(obj), jumps)

def least_jumps(start, finish):
    jumps = []
    for j in start.keys() & finish.keys():
        jumps.append (start[j] + finish[j])

    return min(jumps) - 2

YOU_jumps = {}
SAN_jumps = {}
calc_orbits("YOU", YOU_jumps)
calc_orbits("SAN", SAN_jumps)

print(least_jumps(YOU_jumps, SAN_jumps))