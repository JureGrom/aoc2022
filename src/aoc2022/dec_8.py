import os


def main(input_file):
    tree_map = []
    tree_visibility_map = []
    scenic_score_map = []
    with open(input_file) as file:
        for line in file:
            line = line[:-1]
            tree_map.append([int(h) for h in line])
            tree_visibility_map.append([0 for i in range(0, len(line))])
            scenic_score_map.append([0 for i in range(0, len(line))])

    map_width = len(tree_map[0])
    map_height = len(tree_map)

    count_visible_trees(map_height, map_width, tree_map, tree_visibility_map)

    calculate_scenic_score(map_height, map_width, scenic_score_map, tree_map)


def calculate_scenic_score(map_height, map_width, scenic_score_map, tree_map):
    max_scenic_score = 0
    for y in range(1, map_height - 1):
        for x in range(1, map_width - 1):
            visible_north = 0
            visible_south = 0
            visible_east = 0
            visible_west = 0
            max_height = tree_map[y][x]
            for i in range(y - 1, -1, -1):
                visible_north += 1
                if tree_map[i][x] >= max_height:
                    break
            for i in range(y + 1, map_height):
                visible_south += 1
                if tree_map[i][x] >= max_height:
                    break
            for i in range(x - 1, -1, -1):
                visible_west += 1
                if tree_map[y][i] >= max_height:
                    break
            for i in range(x + 1, map_width):
                visible_east += 1
                if tree_map[y][i] >= max_height:
                    break
            scenic_score_map[y][x] = visible_north * visible_south * visible_east * visible_west
            if scenic_score_map[y][x] > max_scenic_score:
                max_scenic_score = scenic_score_map[y][x]
    print(f"Max scenic score is {max_scenic_score}")


def count_visible_trees(map_height, map_width, tree_map, tree_visibility_map):
    highest_north = [-1 for i in range(0, map_width)]
    highest_south = [-1 for i in range(0, map_width)]
    highest_east = [-1 for i in range(0, map_height)]
    highest_west = [-1 for i in range(0, map_height)]
    for y in range(0, map_height):
        lb_y = map_height - y - 1
        for x in range(0, map_width):
            if tree_map[y][x] > highest_north[x]:
                tree_visibility_map[y][x] = 1
                highest_north[x] = tree_map[y][x]
            if tree_map[y][x] > highest_west[y]:
                tree_visibility_map[y][x] = 1
                highest_west[y] = tree_map[y][x]
            lb_x = map_width - x - 1
            if tree_map[lb_y][lb_x] > highest_south[lb_x]:
                tree_visibility_map[lb_y][lb_x] = 1
                highest_south[lb_x] = tree_map[lb_y][lb_x]
            if tree_map[lb_y][lb_x] > highest_east[lb_y]:
                tree_visibility_map[lb_y][lb_x] = 1
                highest_east[lb_y] = tree_map[lb_y][lb_x]
    visible_trees = 0
    for r in tree_visibility_map:
        visible_trees += sum(r)
    print(f"There are {visible_trees} visible trees.")


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_8_input.txt')
