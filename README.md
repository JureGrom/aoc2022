# Advent of Code 2022

Code for [Advent of Code 2022](https://adventofcode.com/2022) puzzles.

## Setup env

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run puzzle

```
source .venv/bin/activate
cd src/aoc2022
pyton dec_1.py

# or - issue with static input file import
export PYTHONPATH="$(pwd)/src:$PYTHONPATH"
python -m aoc2022.dec_1
```

## Run tests

```
source .venv/bin/activate
pytest
```