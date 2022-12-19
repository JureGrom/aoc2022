import os


def main(input_file):
    with open(input_file) as file:
        max_calories = 0
        elf_with_max_calories = 1

        elf_num = 1
        current_elf_calories = 0
        snacks = 0
        elves = []
        for line in file:
            # remove new line char
            if len(line) > 0:
                line = line[:-1]
            if line == "":
                elves.append((elf_num, current_elf_calories, snacks))
                if current_elf_calories > max_calories:
                    max_calories = current_elf_calories
                    elf_with_max_calories = elf_num
                elf_num += 1
                current_elf_calories = 0
                snacks = 0
            else:
                current_elf_calories += int(line)
                snacks += 1

        print(f"Max calories {max_calories} are with elf num {elf_with_max_calories}")
        # Max calories 72070 are with elf num 40

        elves_by_calories = sorted(elves, key=lambda x: x[1], reverse=True)
        top_calories = elves_by_calories[0][1] + elves_by_calories[1][1] + elves_by_calories[2][1]
        print(f"Top 3 elves have {top_calories} calories")


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_1_input.txt')
