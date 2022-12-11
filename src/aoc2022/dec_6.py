import os


def main(input_file):
    with open(input_file) as file:
        for line in file:
            find_sequence_index(line, 4)
            find_sequence_index(line, 14)


def find_sequence_index(line, length):
    for i in range(0, len(line) - length):
        if len(set(line[i:i + length])) == length:
            print(f"Sequence of {length} starts after {i + length} with {line[i:i + length]}.")
            break


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_6_input.txt')
