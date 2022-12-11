"""
[P]     [L]         [T]
[L]     [M] [G]     [G]     [S]
[M]     [Q] [W]     [H] [R] [G]
[N]     [F] [M]     [D] [V] [R] [N]
[W]     [G] [Q] [P] [J] [F] [M] [C]
[V] [H] [B] [F] [H] [M] [B] [H] [B]
[B] [Q] [D] [T] [T] [B] [N] [L] [D]
[H] [M] [N] [Z] [M] [C] [M] [P] [P]
 1   2   3   4   5   6   7   8   9
"""
import re
from copy import copy

ship_part1 = {
    "1": ["H", "B", "V", "W", "N", "M", "L", "P"],
    "2": ["M", "Q", "H"],
    "3": ["N", "D", "B", "G", "F", "Q", "M", "L"],
    "4": ["Z", "T", "F", "Q", "M", "W", "G"],
    "5": ["M", "T", "H", "P"],
    "6": ["C", "B", "M", "J", "D", "H", "G", "T"],
    "7": ["M", "N", "B", "F", "V", "R"],
    "8": ["P", "L", "H", "M", "R", "G", "S"],
    "9": ["P", "D", "B", "C", "N"],
}


ship_part2 = {
    "1": ["H", "B", "V", "W", "N", "M", "L", "P"],
    "2": ["M", "Q", "H"],
    "3": ["N", "D", "B", "G", "F", "Q", "M", "L"],
    "4": ["Z", "T", "F", "Q", "M", "W", "G"],
    "5": ["M", "T", "H", "P"],
    "6": ["C", "B", "M", "J", "D", "H", "G", "T"],
    "7": ["M", "N", "B", "F", "V", "R"],
    "8": ["P", "L", "H", "M", "R", "G", "S"],
    "9": ["P", "D", "B", "C", "N"],
}


def print_top_crates(ship, ship_name):
    top_crates = ""
    for stack in ship:
        top_crates += ship[stack][len(ship[stack]) - 1]
    print(f"On top of {ship_name} are: {top_crates}")


def main(input_file):
    instruction_re = re.compile(r"move (\d+) from (\d+) to (\d+)")
    with open(input_file) as file:
        for line in file:
            instruction = instruction_re.search(line)
            moves = int(instruction.group(1))
            from_stack = instruction.group(2)
            to_stack = instruction.group(3)
            # part 1
            for i in range(0, moves):
                ship_part1[to_stack].append(ship_part1[from_stack].pop())
            # part 2
            ship_part2[to_stack].extend(ship_part2[from_stack][-moves:])
            ship_part2[from_stack] = ship_part2[from_stack][:-moves]

    print_top_crates(ship_part1, "ship_part1")
    print_top_crates(ship_part2, "ship_part2")


if __name__ == '__main__':
    main('../../inputs/dec_5_input.txt')
