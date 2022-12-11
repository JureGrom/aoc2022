import os

moves = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3, # Scissors
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3, # Scissor
}

outcomes = {
    "X": 0, # Loose
    "Y": 3, # Draw
    "Z": 6, # Win
}

wins = {
    1: 2,
    2: 3,
    3: 1
}

losses = {
    1: 3,
    2: 1,
    3: 2
}


def calculate_round_outcome(opponent_move, own_move):
    if opponent_move == own_move:
        return 3
    elif wins[opponent_move] == own_move:
        return 6
    else:
        return 0


def calculate_round_own_move(opponent_move, outcome):
    if outcome == 3:
        return opponent_move
    elif outcome == 0:
        return losses[opponent_move]
    else:
        return wins[opponent_move]


def main(input_file):
    with open(input_file) as file:
        score = 0
        score_outcome = 0
        for line in file:
            round_moves = line.strip('\n').split(" ")
            if len(round_moves) == 2:
                round_opponent_move = moves[round_moves[0]]
                round_own_move = moves[round_moves[1]]
                round_outcome = outcomes[round_moves[1]]
                score += calculate_round_outcome(round_opponent_move, round_own_move) + round_own_move
                score_outcome += calculate_round_own_move(round_opponent_move, round_outcome) + round_outcome

        print(f"Total score is {score}.") # 13675
        print(f"Total score by calc own move is {score_outcome}.") # 14184


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_2_input.txt')
