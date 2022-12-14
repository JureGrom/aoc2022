import os


def get_coordinates(point):
    coordinates = point.split(",")
    return int(coordinates[0]), int(coordinates[1])


def get_points_between(start, end):
    points = set()
    if start[0] == end[0]:
        for i in range(start[1], end[1], 1 if start[1] < end[1] else -1):
            point = (start[0], i)
            points.add(point)
    if start[1] == end[1]:
        for i in range(start[0], end[0], 1 if start[0] < end[0] else -1):
            point = (i, start[1])
            points.add(point)
    return points


def move_sand_point(sand_point, blocked_points, max_y, max_depth_return=False):
    """
    A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or
    sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked,
    the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as
    it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible
    destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of
    sand is created back at the source.
    """
    if sand_point[1] > max_y:
        return sand_point if max_depth_return else None
    down_point = (sand_point[0], sand_point[1] + 1)
    left_below = (sand_point[0]-1, sand_point[1] + 1)
    right_below = (sand_point[0]+1, sand_point[1] + 1)
    for point in [down_point, left_below, right_below]:
        if point not in blocked_points:
            return move_sand_point(point, blocked_points, max_y, max_depth_return)
    return sand_point


def print_cave(rocks, sand_points, max_y, last_line):
    min_x = 500
    max_x = 500
    for point in rocks.union(sand_points):
        if point[0] < min_x:
            min_x = point[0]
        if point[0] > max_x:
            max_x = point[0]
    for y in range(max_y + 1):
        for x in range(min_x, max_x + 1):
            point = (x, y)
            if y == max_y:
                print(last_line, end="")
            elif point in rocks:
                print("#", end="")
            elif point in sand_points:
                print("o", end="")
            else:
                print(".", end="")
        print()


def main(file_name):
    rocks = set()
    sand_source = (500, 0)
    max_y = 0
    with open(file_name) as file:
        for line in file:
            points = line[:-1].split(" -> ")
            for i in range(len(points)-1):
                start = get_coordinates(points[i])
                end = get_coordinates(points[i+1])
                if start[1] > max_y:
                    max_y = start[1]
                if end[1] > max_y:
                    max_y = end[1]
                rocks.add(start)
                if i+2 == len(points):
                    rocks.add(end)
                rocks = rocks.union(get_points_between(start, end))
    print(f"There are {len(rocks)} rocks with max depth of {max_y}.")

    # Part 1
    abyss_not_reached = True
    sand_points = set()
    blocked = set(rocks)
    while abyss_not_reached:
        sand_point = move_sand_point(sand_source, blocked, max_y)
        if sand_point:
            sand_points.add(sand_point)
            blocked.add(sand_point)
        else:
            abyss_not_reached = False
    print(f"{len(sand_points)} units of sand come to rest before sand starts flowing into the abyss below.")
    print_cave(rocks, sand_points, max_y+1, last_line=".")

    print()
    # Part 2
    sand_points = set()
    blocked = set(rocks)
    while True:
        sand_point = move_sand_point(sand_source, blocked, max_y, True)
        sand_points.add(sand_point)
        blocked.add(sand_point)
        if sand_point == (500, 0):
            break
    print(f"{len(sand_points)} units of sand come to rest.")
    print_cave(rocks, sand_points, max_y+2, last_line="#")


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_14_input.txt')
