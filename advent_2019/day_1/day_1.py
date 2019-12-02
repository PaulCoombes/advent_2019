with open(r'day_1\input.txt', 'r') as f:
    modules = map(int, f.read().splitlines())

fuel = []
for m in modules:
    module_fuel = ((m // 3) - 2)
    fuel.append(module_fuel)
 
    while module_fuel != 0:
        fuel_req = module_fuel // 3 - 2

        if fuel_req >= 0:
            module_fuel = fuel_req
        else:
            module_fuel = 0

        fuel.append(module_fuel)

print(sum(fuel))


