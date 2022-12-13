import os


def is_pair_ordered(left, right):
    """
    When comparing two values, the first value is called left and the second value is called right. Then:
    1. If both values are integers, the lower integer should come first. If the left integer is lower than the right
       integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs
       are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of
       the input.
    2. If both values are lists, compare the first value of each list, then the second value, and so on. If the left
       list runs out of items first, the inputs are in the right order. If the right list runs out of items first,
       the inputs are not in the right order. If the lists are the same length and no comparison makes a decision
       about the order, continue checking the next part of the input.
    3. If exactly one value is an integer, convert the integer to a list which contains that integer as its only value,
       then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list
       containing 2); the result is then found by instead comparing [0,0,0] and [2].
    :param left:
    :param right:
    :return:
    """
    if len(left) == 0:
        return True

    for i in range(len(left)):
        if i > (len(right) - 1):
            return False

        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] == right[i]:
                continue
            else:
                return left[i] < right[i]
        else:
            comparison = is_pair_ordered(left[i] if type(left[i]) == list else [left[i]],
                                         right[i] if type(right[i]) == list else [right[i]])
            return comparison

    return True


def get_pairs(file_name):
    pairs = []
    with open(file_name) as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            pairs.append((eval(lines[i]), eval(lines[i + 1])))
    return pairs


def main(file_name):
    pairs = get_pairs(file_name)
    ordered_pair_index_sum = 0
    for i in range(len(pairs)):
        if is_pair_ordered(pairs[i][0], pairs[i][1]):
            print(f"Pair {i+1} is in the right order")
            ordered_pair_index_sum += i + 1

    print(f"Sum of ordered pairs indexes is {ordered_pair_index_sum}")


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_13_input.txt')
