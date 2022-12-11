def render(x_register_by_cycles):
    line = ["" for _ in range(40)]
    for i in range(len(x_register_by_cycles)):
        line[i % 40] = "#" if (x_register_by_cycles[i]-1 <= i % 40 <= x_register_by_cycles[i]+1) else "."
        if (i+1) % 40 == 0:
            print("".join(line))
            line = ["" for _ in range(40)]


def main(input_file):
    with open(input_file) as file:
        instructions = [row.split() for row in file.readlines()]
    x_register_by_cycles = part_1(instructions)
    render(x_register_by_cycles)


def part_1(instructions):
    cycle = 0
    register_x = 1
    signal_strength_sum = 0
    important_cycles = [20, 60, 100, 140, 180, 220]
    signal_cycle = 0
    x_register_by_cycles = []
    for i in range(len(instructions)):
        if instructions[i][0] == "noop":
            cycle_increase = 1
            register_x_increase = 0
        elif instructions[i][0] == "addx":
            cycle_increase = 2
            register_x_increase = int(instructions[i][1])
        else:
            cycle_increase = 0
            register_x_increase = 0

        if signal_cycle < len(important_cycles):
            if important_cycles[signal_cycle] <= cycle + cycle_increase:
                signal_strength_sum += important_cycles[signal_cycle] * register_x
                signal_cycle += 1
        for _ in range(cycle_increase):
            x_register_by_cycles.append(register_x)
        register_x += register_x_increase
        cycle += cycle_increase
    print(f"Sum of signal strengths is {signal_strength_sum}")
    return x_register_by_cycles


if __name__ == '__main__':
    main('../../inputs/dec_10_input.txt')
