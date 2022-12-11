# content of test_sample.py
from aoc2022.dec_1 import dec_1_inc


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def test_dec1():
    assert dec_1_inc(3) == 4
