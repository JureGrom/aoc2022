from aoc2022.dec_9 import calculate_tail_position


def test_move_head():
    assert calculate_tail_position((2, 2), (0, 0)) == (1, 1)
    assert calculate_tail_position((2, 2), (0, 1)) == (1, 2)
    assert calculate_tail_position((2, 2), (0, 2)) == (1, 2)
    assert calculate_tail_position((2, 2), (0, 3)) == (1, 2)
    assert calculate_tail_position((2, 2), (0, 4)) == (1, 3)

    assert calculate_tail_position((2, 2), (1, 0)) == (2, 1)
    assert calculate_tail_position((2, 2), (1, 1)) == (1, 1)
    assert calculate_tail_position((2, 2), (1, 2)) == (1, 2)
    assert calculate_tail_position((2, 2), (1, 3)) == (1, 3)
    assert calculate_tail_position((2, 2), (1, 4)) == (2, 3)

    assert calculate_tail_position((2, 2), (2, 0)) == (2, 1)
    assert calculate_tail_position((2, 2), (2, 1)) == (2, 1)
    assert calculate_tail_position((2, 2), (2, 2)) == (2, 2)
    assert calculate_tail_position((2, 2), (2, 3)) == (2, 3)
    assert calculate_tail_position((2, 2), (2, 4)) == (2, 3)

    assert calculate_tail_position((2, 2), (3, 0)) == (2, 1)
    assert calculate_tail_position((2, 2), (3, 1)) == (3, 1)
    assert calculate_tail_position((2, 2), (3, 2)) == (3, 2)
    assert calculate_tail_position((2, 2), (3, 3)) == (3, 3)
    assert calculate_tail_position((2, 2), (3, 4)) == (2, 3)

    assert calculate_tail_position((2, 2), (4, 0)) == (3, 1)
    assert calculate_tail_position((2, 2), (4, 1)) == (3, 2)
    assert calculate_tail_position((2, 2), (4, 2)) == (3, 2)
    assert calculate_tail_position((2, 2), (4, 3)) == (3, 2)
    assert calculate_tail_position((2, 2), (4, 4)) == (3, 3)
