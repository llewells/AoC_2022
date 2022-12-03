from aoc_utils.funcs import load_text_file

ROCK, PAPER, SCISSORS = 'rock', 'paper', "scissors"

CODE = {
    "X" : "lose",
    "Y" : "draw",
    "Z" : "win",
    "A" : ROCK,
    "B" : PAPER,
    "C" : SCISSORS,
}

STRATEGY = {
    ROCK : {
        "win" : PAPER,
        "lose" : SCISSORS,
        "draw" : ROCK,
    },
    SCISSORS : {
        "win" : ROCK,
        "lose" : PAPER,
        "draw" : SCISSORS,
    },
    PAPER : {
        "win" : SCISSORS,
        "lose" : ROCK,
        "draw" : PAPER,
    },
}

POINTS = {
    ROCK : 1,
    PAPER : 2,
    SCISSORS : 3,
}

WIN, LOSE, DRAW = 6, 0, 3

def extract_list_items(data):
    return [item.split(' ') for item in data]

def extract_guesses(address):
    return extract_list_items(load_text_file(address))

def score_for_round(round):
    opponent = CODE[round[0].upper()]
    result = CODE[round[1].upper()]
    me = STRATEGY[opponent][result]

    score = POINTS[me]

    if result == 'draw':
        score += DRAW
    elif result == 'win':
        score += WIN
    else:
        score += LOSE

    return score


def run():
    address = "input.txt"
    rounds = extract_guesses(address)
    total_score = sum([score_for_round(round) for round in rounds])
    return total_score

if __name__ == '__main__':
    print(run())