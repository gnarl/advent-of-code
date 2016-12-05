import csv

DIR_FACE = {'R': lambda x: (x+1) % 4,
            'L': lambda x: (x-1) % 4
            }


def get_directions():
    with open('input.csv', 'rb') as f:
        input = csv.reader(f, delimiter=',', skipinitialspace=True)
        directions = []
        for row in input:
            for item in row:
                directions.append(item)
    return directions


def locations(distances):
    loc1 = distances[0] - distances[2]
    loc2 = distances[1] - distances[3]
    return (loc1, loc2)

distances = [0, 0, 0, 0]
directions = get_directions()
current_direction = 0

for direction in directions:
    current_direction = DIR_FACE[direction[0]](current_direction)
    distances[current_direction] += int(direction[1:])
    loc = locations(distances)

result = abs(distances[0] - distances[2]) + abs(distances[1] - distances[3])
print result
