import os


def main(input_file):
    with open(input_file) as file:
        pairs_with_containment = 0
        pairs_with_overlap = 0
        for line in file:
            elves_ranges = line.strip('\n').split(",")
            elf_a_range = [int(i) for i in elves_ranges[0].split("-")]
            elf_b_range = [int(i) for i in elves_ranges[1].split("-")]
            if elf_a_range[0] <= elf_b_range[0] and elf_b_range[1] <= elf_a_range[1] \
                    or elf_b_range[0] <= elf_a_range[0] and elf_a_range[1] <= elf_b_range[1]:
                pairs_with_containment += 1
            if elf_a_range[0] <= elf_b_range[0] <= elf_a_range[1] or \
                    elf_b_range[0] <= elf_a_range[0] <= elf_b_range[1]:
                pairs_with_overlap += 1
        print(f"In total there are {pairs_with_containment} pairs with full containment.")
        print(f"In total there are {pairs_with_overlap} pairs with range overlap.")


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_4_input.txt')
