def get_item_priority(item):
    priority = ord(item)
    if priority > 95:
        # lower case
        return priority - 96
    else:
        # upper case
        return priority - 65 + 27


def main(input_file):
    with open(input_file) as file:
        priorities_sum = 0
        group_priorities_sum = 0
        group_backpacks = []
        for line in file:
            backpack = line.strip('\n')
            compartment_1, compartment_2 = backpack[:-len(backpack)//2], backpack[len(backpack)//2:]
            group_backpacks.append(backpack)
            for item in compartment_1:
                if item in compartment_2:
                    priorities_sum += get_item_priority(item)
                    break
            if len(group_backpacks) % 3 == 0:
                badge = set(group_backpacks[0]).intersection(group_backpacks[1]).intersection(group_backpacks[2])
                for badge_item in badge:
                    group_priorities_sum += get_item_priority(badge_item)
                group_backpacks = []
        print(f"Sum of priorities is {priorities_sum}")
        print(f"Sum of group item priorities is {group_priorities_sum}")


if __name__ == '__main__':
    main('../../inputs/dec_3_input.txt')
