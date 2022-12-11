import os
import re


def calculate_tail_position(head, tail):
    dist_x, dist_y = head[0] - tail[0], head[1] - tail[1]
    abs_x = abs(dist_x)
    abs_y = abs(dist_y)
    if abs_x > 1 or abs_y > 1:
        return (
            tail[0] + (0 if dist_x == 0 else dist_x // abs_x),
            tail[1] + (0 if dist_y == 0 else dist_y // abs_y)
        )
    return tail


def move_head(rope, visited, x_step, y_step, steps):
    for x in range(0, abs(x_step * steps) + 1):
        for y in range(0, abs(y_step * steps) + 1):
            rope[0] = (rope[0][0] + 1*x_step, rope[0][1] + 1*y_step)
            for i in range(0, len(rope)-1):
                head = rope[i]
                tail = rope[i+1]
                new_tail = calculate_tail_position(head, tail)
                rope[i+1] = new_tail
            visited.add(rope[len(rope)-1])


def main(input_file):
    with open(input_file) as file:
        move_re = re.compile(r"(.) (\d+)")
        rope_part1 = [(0, 0) for _ in range(2)]
        rope_part2 = [(0, 0) for _ in range(10)]
        visited_part1 = set()
        visited_part2 = set()
        visited_part1.add(rope_part1[len(rope_part1)-1])
        visited_part2.add(rope_part2[len(rope_part2)-1])
        for line in file:
            move = move_re.search(line)
            direction = move.group(1)
            steps = int(move.group(2))
            if direction == "R":
                x_step = 1
                y_step = 0
            elif direction == "L":
                x_step = -1
                y_step = 0
            elif direction == "U":
                x_step = 0
                y_step = 1
            elif direction == "D":
                x_step = 0
                y_step = -1
            move_head(rope_part1, visited_part1, x_step, y_step, steps - 1)
            move_head(rope_part2, visited_part2, x_step, y_step, steps - 1)
        print(f"Part1: Tail visited {len(visited_part1)}")
        print(f"Part2: Tail visited {len(visited_part2)}")


def print_rope(rope, indent=""):
    for y in range(21, 0, -1):
        line = ".........................."
        for x in range(0, len(line)):
            for i in range(0, len(rope)):
                if (x, y) == rope[i]:
                    line = line[:x] + ("H" if i == 0 else str(i)) + line[x+1:]
                    break
        print(indent + line)
    print()


def test():
    rope = [(11, 6), (11, 6), (11, 6), (11, 6), (11, 6), (11, 6), (11, 6), (11, 6), (11, 6), (11, 6)]
    visited = set()
    visited.add(rope[len(rope)-1])
    print_rope(rope)
    print(" == R 5 == ")
    x_step = 1
    y_step = 0
    steps = 5
    move_head(rope, visited, x_step, y_step, steps - 1)
    print_rope(rope)
    print(" == U 8 ==")
    x_step = 0
    y_step = 1
    steps = 8
    move_head(rope, visited, x_step, y_step, steps - 1)
    print_rope(rope)
    print(" == L 8 ==")
    x_step = -1
    y_step = 0
    steps = 8
    move_head(rope, visited, x_step, y_step, steps - 1)
    print_rope(rope)
    print(" == D 3 ==")
    x_step = 0
    y_step = -1
    steps = 3
    move_head(rope, visited, x_step, y_step, steps - 1)
    print_rope(rope)
    print(" == R 17 ==")
    x_step = 1
    y_step = 0
    steps = 17
    move_head(rope, visited, x_step, y_step, steps - 1)
    print_rope(rope)
    print(" == D 10 ==")
    x_step = 0
    y_step = -1
    steps = 10
    move_head(rope, visited, x_step, y_step, steps - 1)
    print_rope(rope)
    print(" == L 25 ==")
    x_step = -1
    y_step = 0
    steps = 25
    move_head(rope, visited, x_step, y_step, steps - 1)
    print_rope(rope)
    print(" == U 20 ==")
    x_step = 0
    y_step = 1
    steps = 20
    move_head(rope, visited, x_step, y_step, steps - 1)
    print_rope(rope)


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_9_input.txt')
    #test()

