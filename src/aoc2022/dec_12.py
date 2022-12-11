import os


def main(input_file):
    with open(input_file) as file:
        for line in file:
            line = line[:-1]



if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_12_input.txt')
