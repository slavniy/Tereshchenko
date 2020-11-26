def find_start_points(place_map, step):
    points = set()
    for y in range(len(place_map)):
        for x in range(len(place_map[y])):
            if place_map[y][x] == step:
                points.add((y, x))
    return points

def traceback(row,col, step):
    place_map[row][col] = '$'
    step -= 1
    if row - 1 >= 0 and place_map[row - 1][col] == step:
        traceback(row - 1, col, step)
    elif row + 1 < len(place_map) and place_map[row + 1][col] == step:
        traceback(row + 1, col, step)
    elif col - 1 >= 0 and place_map[row][col - 1] == step:
        traceback(row, col - 1, step)

    elif col + 1 < len(place_map[0]) and place_map[row][col + 1] == step:
        traceback(row, col + 1, step)


def print_map():
    for row in place_map:
        print(*row, sep='\t')
    print('-' * 80)


file = open('labirint.txt')
place_map = []
for line in file:
    place_map.append(line.split())

step = 0
points = find_start_points(place_map, 'a')
while points:
    step += 1
    for point in points:
        row, col = point
        if row - 1 >= 0 and place_map[row - 1][col] in ['.', 'b']:
            if place_map[row - 1][col] == 'b':
                traceback(row - 1, col, step)
            else:
                place_map[row - 1][col] = step
        if row + 1 < len(place_map) and place_map[row + 1][col] in ['.', 'b']:
            if place_map[row + 1][col] == 'b':
                traceback(row + 1, col, step)
            else:
                place_map[row + 1][col] = step
        if col - 1 >= 0 and place_map[row][col - 1] in ['.', 'b']:
            if place_map[row][col - 1] == 'b':
                traceback(row, col - 1, step)
            else:
                place_map[row][col - 1] = step
        if col + 1 < len(place_map[0]) and place_map[row][col + 1] in ['.', 'b']:
            if place_map[row][col + 1] == 'b':
                traceback(row, col + 1, step)
            else:
                place_map[row][col + 1] = step
    points = find_start_points(place_map, step)
print_map()
