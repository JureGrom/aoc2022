import os
import re


def get_points_within_manhattan_distance_at_line(sensor, beacon, y):
    manhattan_distance = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
    row_distance = abs(sensor[1] - y)
    points = []
    for i in range(manhattan_distance - row_distance + 1):
        points.append((sensor[0] - i, y))
        points.append((sensor[0] + i, y))
    return points


def main(file_name, y):
    pairs = []

    input_re = re.compile(r"Sensor .* x=(-?\d+), y=(-?\d+):.*x=(-?\d+), y=(-?\d+)")
    with open(file_name) as file:
        for line in file:
            input_points = input_re.search(line)
            sensor = (int(input_points.group(1)), int(input_points.group(2)))
            beacon = (int(input_points.group(3)), int(input_points.group(4)))
            pairs.append((sensor, beacon))
    not_covered = set()
    beacons = set()
    for sensor, beacon in pairs:
        points = get_points_within_manhattan_distance_at_line(sensor, beacon, y)
        not_covered = not_covered.union(set(points))
        beacons.add(beacon)
    print(f"There are {len(not_covered.difference(beacons))} positions that cannot contain beacon at {y}.")


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_15_test_input.txt', 10)
    main(os.path.dirname(__file__) + '/../../inputs/dec_15_input.txt', 2000000)
