from PIL import Image


def create_matrix_by_image(name='lab.jpg'):
    im = Image.open(name)
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения
    matrix = []
    for i in range(y):
        row = []
        for j in range(x):
            r, g, b = pixels[i, j]
            if r > 122 and g > 122 and b > 122:
                el = '.'
            elif r < 122 and g < 122 and b < 122:
                el = '#'
            elif r < 122 and g > 122 and b < 122:
                el = 'a'
            elif r > 122 and g < 122 and b < 122:
                el = 'b'
            row.append(el)
        matrix.append(row)
    return matrix


def create_image_by_matrix(matrix, name='lab.jpg'):
    im = Image.open(name)
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения
    for i in range(y):
        for j in range(x):
            if matrix[i][j] == '$':
                pixels[i, j] = 0, 255, 0
    im.save('route.jpg')




def create_matrix_by_file(file_name='labirint.txt'):
    file = open(file_name)
    place_map = []
    for line in file:
        place_map.append(line.split())
    return place_map





def find_start_points(place_map, step):
    points = set()
    for y in range(len(place_map)):
        for x in range(len(place_map[y])):
            if place_map[y][x] == step:
                points.add((y, x))
    return points


def traceback(row, col, step):
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


def print_map(matrix):
    for row in matrix:
        print(*row, sep='\t')
    print('-' * 80)


place_map = create_matrix_by_image()
step = 0
points = find_start_points(place_map, 'a')
while points:
    new_points = set()
    step += 1
    for point in points:
        row, col = point
        if row - 1 >= 0 and place_map[row - 1][col] in ['.', 'b']:
            if place_map[row - 1][col] == 'b':
                traceback(row - 1, col, step)
            else:
                place_map[row - 1][col] = step
                new_points.add((row - 1, col))
        if row + 1 < len(place_map) and place_map[row + 1][col] in ['.', 'b']:
            if place_map[row + 1][col] == 'b':
                traceback(row + 1, col, step)
            else:
                place_map[row + 1][col] = step
                new_points.add((row + 1, col))
        if col - 1 >= 0 and place_map[row][col - 1] in ['.', 'b']:
            if place_map[row][col - 1] == 'b':
                traceback(row, col - 1, step)
            else:
                place_map[row][col - 1] = step
                new_points.add((row, col - 1))
        if col + 1 < len(place_map[0]) and place_map[row][col + 1] in ['.', 'b']:
            if place_map[row][col + 1] == 'b':
                traceback(row, col + 1, step)
            else:
                place_map[row][col + 1] = step
                new_points.add((row, col + 1))
    points = new_points
create_image_by_matrix(place_map)