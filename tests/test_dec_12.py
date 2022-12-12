from aoc2022.dec_12 import *


def test_part1_input_result():
    grid = process_input(os.path.dirname(__file__) + '/../inputs/dec_12_test_input.txt')
    shortest_path = find_path(grid, (5, 2), [(0, 0)], {(0, 0): 0})
    assert shortest_path == 31


def test_get_next_steps():
    grid = process_input(os.path.dirname(__file__) + '/../inputs/dec_12_test_input.txt')

    assert get_next_steps((0, 0), grid) == [(0, 1), (1, 0)]
    assert get_next_steps((1, 0), grid) == [(0, 0), (1, 1), (2, 0)]
    assert get_next_steps((2, 0), grid) == [(1, 0), (2, 1)]
    assert get_next_steps((3, 0), grid) == [(2, 0), (3, 1), (4, 0)]
    assert get_next_steps((4, 0), grid) == [(3, 0), (5, 0)]
    assert get_next_steps((5, 0), grid) == [(4, 0), (6, 0)]
    assert get_next_steps((6, 0), grid) == [(5, 0), (7, 0)]
    assert get_next_steps((0, 1), grid) == [(0, 0), (0, 2), (1, 1)]
    assert get_next_steps((1, 1), grid) == [(0, 1), (1, 0), (1, 2), (2, 1)]
    assert get_next_steps((2, 1), grid) == [(1, 1), (2, 0), (2, 2)]
    assert get_next_steps((3, 1), grid) == [(2, 1), (3, 0), (3, 2)]
    assert get_next_steps((4, 1), grid) == [(3, 1), (4, 0), (4, 2), (5, 1)]
    assert get_next_steps((5, 1), grid) == [(4, 1), (5, 0), (6, 1)]
    assert get_next_steps((6, 1), grid) == [(5, 1), (6, 0), (6, 2), (7, 1)]
    assert get_next_steps((0, 2), grid) == [(0, 1), (0, 3)]
    assert get_next_steps((1, 2), grid) == [(0, 2), (1, 1), (1, 3), (2, 2)]
    assert get_next_steps((2, 2), grid) == [(1, 2), (2, 1), (2, 3)]
    assert get_next_steps((3, 2), grid) == [(2, 2), (3, 1), (3, 3)]
    assert get_next_steps((4, 2), grid) == [(3, 2), (4, 1), (4, 3), (5, 2)]
    assert get_next_steps((5, 2), grid) == [(4, 2), (5, 1), (5, 3), (6, 2)]
    assert get_next_steps((6, 2), grid) == [(6, 1), (6, 3), (7, 2)]
    assert get_next_steps((0, 3), grid) == [(0, 2), (0, 4)]
    assert get_next_steps((1, 3), grid) == [(0, 3), (1, 2), (1, 4), (2, 3)]
    assert get_next_steps((2, 3), grid) == [(1, 3), (2, 2), (2, 4)]
    assert get_next_steps((3, 3), grid) == [(2, 3), (3, 2), (3, 4), (4, 3)]
    assert get_next_steps((4, 3), grid) == [(3, 3), (4, 4), (5, 3)]
    assert get_next_steps((5, 3), grid) == [(4, 3), (5, 4), (6, 3)]
    assert get_next_steps((6, 3), grid) == [(5, 3), (6, 2), (6, 4), (7, 3)]
    assert get_next_steps((0, 4), grid) == [(0, 3), (1, 4)]
    assert get_next_steps((1, 4), grid) == [(0, 4), (1, 3)]
    assert get_next_steps((2, 4), grid) == [(1, 4), (2, 3), (3, 4)]
    assert get_next_steps((3, 4), grid) == [(2, 4), (4, 4)]
    assert get_next_steps((4, 4), grid) == [(3, 4), (5, 4)]
    assert get_next_steps((5, 4), grid) == [(4, 4), (6, 4)]
    assert get_next_steps((6, 4), grid) == [(5, 4), (7, 4)]


def test_check_for_points_within_grid():
    grid = process_input(os.path.dirname(__file__) + '/../inputs/dec_12_test_input.txt')
    assert is_point_in_grid((0, 0), grid) is True
    assert is_point_in_grid((-1, 0), grid) is False
    assert is_point_in_grid((0, -1), grid) is False
    assert is_point_in_grid((0, 1), grid) is True
    assert is_point_in_grid((1, 0), grid) is True


def test_point_reachability():
    assert is_point_reachable("a", "a") is True
    assert is_point_reachable("a", "b") is True
    assert is_point_reachable("S", "b") is True
    assert is_point_reachable("S", "b") is True
    assert is_point_reachable("y", "E") is True
    assert is_point_reachable("a", "c") is False
    assert is_point_reachable("m", "n") is True
    assert is_point_reachable("m", "o") is False
    assert is_point_reachable("b", "a") is True
