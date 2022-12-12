import os


def find_points(grid, mark):
    points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == mark:
                points.append((x, y))
    return points


def is_point_in_grid(next_point, grid):
    return 0 <= next_point[0] < len(grid[0]) and 0 <= next_point[1] < len(grid)


def get_height(point_value):
    if point_value == "S":
        point_value = "a"
    if point_value == "E":
        point_value = "z"
    return ord(point_value)


def is_point_reachable(start, end):
    return get_height(end) - get_height(start) <= 1


def get_next_steps(point, grid):
    allowed_steps = []
    for step in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        next_point = point[0] + step[0], point[1] + step[1]
        if is_point_in_grid(next_point, grid) and \
           is_point_reachable(grid[point[1]][point[0]], grid[next_point[1]][next_point[0]]):
            allowed_steps.append(next_point)
    return allowed_steps


def find_path(grid, end, steps, visited):
    prospect_steps = set()
    for step in steps:
        next_steps = get_next_steps(step, grid)
        for next_step in next_steps:
            if next_step == end:
                return visited[step] + 1
            if next_step in visited:
                if visited[next_step] < (visited[step] + 1):
                    continue
            else:
                visited[next_step] = visited[step] + 1
            prospect_steps.add(next_step)
    if len(prospect_steps) == 0:
        return 0
    else:
        return find_path(grid, end, prospect_steps, visited)


def process_input(input_file_path):
    grid = []
    with open(input_file_path) as file:
        for line in file:
            grid.append(line[:-1])
    return grid


def main(input_file):
    grid = process_input(input_file)
    start = find_points(grid, "S")[0]
    end = find_points(grid, "E")[0]
    min_path_len = find_path(grid, end, [start], {start: 0})
    print(f"Shortest path requires {min_path_len} steps.")
    for start_point in find_points(grid, "a"):
        path_len = find_path(grid, end, [start_point], {start_point: 0})
        if 0 < path_len < min_path_len:
            min_path_len = path_len
    print(f"Shortest path any a/S point requires {min_path_len} steps.")


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_12_input.txt')
