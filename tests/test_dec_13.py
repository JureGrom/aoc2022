from aoc2022.dec_13 import *


def test_is_pair_ordered():
    assert is_pair_ordered([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) is True
    assert is_pair_ordered([[1], [2, 3, 4]], [[1], 4]) is True
    assert is_pair_ordered([9], [[8, 7, 6]]) is False
    assert is_pair_ordered([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) is True
    assert is_pair_ordered([7, 7, 7, 7], [7, 7, 7]) is False
    assert is_pair_ordered([], [3]) is True
    assert is_pair_ordered([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]) is False
    assert is_pair_ordered([[[],[[4,3,0,10],[4,6,5]],[[4,0],4,[8],[0,5],10],[[3,9],[3],[8],9,7],0],[[[10,5,0,4]],[3,[1,6],[10,9,3,1]],[[10,2,1],0,6,[],0],0,[[7,8,3,5],[7,3,9],[7,3,0,9,1]]],[],[[8,[5,5,6],[0,6,8]],[[2,10,4,9]],2]],
                           [[0],[9,2,9,7,[[1,9,0,4],[5,2,2,9,8],6,0,[7,10]]],[]]
                           ) is True
    assert is_pair_ordered([[[[3,3,2,6],[],4,4,[9]]],[4,9],[3,[[5,2,10],[]]],[[[6,5],0,[]]],[[[5,4,8]],9,1]],
                           [[],[[6,0]]]) is False


def test_example_input():
    pairs = get_pairs(os.path.dirname(__file__) + '/../inputs/dec_13_test_input.txt')
    ordered_pair_index_sum = 0
    for i in range(len(pairs)):
        if is_pair_ordered(pairs[i][0], pairs[i][1]):
            ordered_pair_index_sum += i + 1
    assert ordered_pair_index_sum == 13