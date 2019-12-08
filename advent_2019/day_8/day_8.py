from collections import Counter
#0 is black
#1 is white
#2 is transparent

def split_layers(digits: str, area: int):
    layers = []
    for i in range(0, len(digits), area):
        layers.append(digits[i:i+area])

    return layers

def count_pixels(layers, area):
    lowest = [area, 0, 0]
    for l in layers:
        c = Counter(l)
        if c['0'] < lowest[0]:
            lowest = [c['0'], c['1'], c['2']]

    return lowest[1] * lowest[2]

def stack_layers(layers, area):
    picture = ['2'] * area
    for l in layers:
        for i in range(0, len(l)):
            if picture[i] == '2':
                picture[i] = l[i]
    picture = ''.join(str(i) for i in picture)
    return picture

def print_picture(picture, width, height):
    picture = picture.replace('1', ' ')
    picture = picture.replace('2', '0')
    for i in range(0, len(picture), width):
        print(picture[i:i + width])

with open("day_8/input.txt", "r") as f:
    pixels = f.read().strip()

width = 25
height = 6
area = width * height
layers = split_layers(pixels, area)

assert(count_pixels(layers, area) == 2125)

picture = stack_layers(layers, area)
print_picture(picture, width, height)


