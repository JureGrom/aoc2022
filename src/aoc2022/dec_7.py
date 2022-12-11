import json
import os
import re


def get_directory(file_system, current_path):
    directory = file_system[current_path[0]]
    for d in current_path[1:]:
        directory = directory[d]
    return directory


def calculate_directory_sizes(file_system, directory_sizes, path):
    size = 0
    for i in file_system:
        if type(file_system[i]) is dict:
            dir_path = path + "/" + i
            dir_size = calculate_directory_sizes(file_system[i], directory_sizes, dir_path)
            directory_sizes[dir_path] = dir_size
            size += dir_size
        else:
            size += file_system[i]
    return size


def main(input_file):
    file_system = {
        "/": {}
    }
    current_path = ["/"]
    current_directory = get_directory(file_system, current_path)
    with open(input_file) as file:
        ls_directory = re.compile(r"dir (.+)")
        ls_file = re.compile(r"(\d+) (.+)")
        for line in file:
            # remove /n
            line = line[:-1]
            if line.startswith("$ cd /"):
                current_path = ["/"]
                current_directory = get_directory(file_system, current_path)
            elif line.startswith("$ cd .."):
                current_path = current_path[:-1]
                current_directory = get_directory(file_system, current_path)
            elif line.startswith("$ cd "):
                directory = line[5:]
                current_path.append(directory)
                current_directory = get_directory(file_system, current_path)
            elif line.startswith("$ ls"):
                continue
            else:
                if ls_directory.match(line):
                    directory = ls_directory.search(line).group(1)
                    current_directory[directory] = {}
                elif ls_file.match(line):
                    file = ls_file.search(line)
                    current_directory[file.group(2)] = int(file.group(1))
                else:
                    print(f"ERROR: unhandled output {line}")
    # print(json.dumps(file_system, indent=4))

    directory_sizes = {}
    calculate_directory_sizes(file_system, directory_sizes, "")
    # print(json.dumps(directory_sizes, indent=4))
    total_small_dirs_size = 0
    small_directory_sizes2 = []
    for d in directory_sizes:
        if directory_sizes[d] < 100000:
            small_directory_sizes2.append(directory_sizes[d])
            total_small_dirs_size += directory_sizes[d]
    print(f"Small directory total size is {total_small_dirs_size}")

    deletion_candidate = "//"
    needed_space = directory_sizes[deletion_candidate] - (70000000 - 30000000)
    for d in directory_sizes:
        if directory_sizes[d] > needed_space:
            if directory_sizes[deletion_candidate] > directory_sizes[d]:
                deletion_candidate = d
    print(f"Candidate for deletion is {deletion_candidate} with size {directory_sizes[deletion_candidate]}")


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_7_input.txt')
