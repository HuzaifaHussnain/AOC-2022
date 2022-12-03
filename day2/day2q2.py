FILENAME = 'q2.txt'


SCORE_MAPPING = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

RESULT_SCORE_MAPPING = {
    'X': 0,
    'Y': 3,
    'Z': 6,
    'lost': 0,
    'draw': 3,
    'win': 6
}

def get_game_outcome(opponent_move, my_move):
    result = 'lost'
    if (opponent_move == 'A' and my_move == 'X') or (opponent_move == 'B' and my_move == 'Y') or (opponent_move == 'C' and my_move == 'Z'):
        result = 'draw'
    elif opponent_move == 'A' and my_move in ['Y']:
        result = 'win'
    elif opponent_move == 'B' and my_move == 'Z':
        result = 'win'
    elif opponent_move == 'C' and my_move == 'X':
        result = 'win'
    return result

def decide_my_move(opponent_move, desired_result):
    # X means lose, Y Means draw, Z win
    my_move = ''
    if desired_result == 'X':
        if opponent_move == 'A':
            my_move = 'Z'
        elif opponent_move == 'B':
            my_move = 'X'
        elif opponent_move == 'C':
            my_move = 'Y'
    if desired_result == 'Y':
        if opponent_move == 'A':
            my_move = 'X'
        elif opponent_move == 'B':
            my_move = 'Y'
        elif opponent_move == 'C':
            my_move = 'Z'
    if desired_result == 'Z':
        if opponent_move == 'A':
            my_move = 'Y'
        elif opponent_move == 'B':
            my_move = 'Z'
        elif opponent_move == 'C':
            my_move = 'X'
    return my_move



f = open(FILENAME, 'r')

my_total_score = 0
score_part_2 = 0
# question 1
for line in f:
    line = line.strip()
    opponent_move = line.split(' ')[0]
    my_move = line.split(' ')[1]
    result = get_game_outcome(opponent_move, my_move)
    score  = SCORE_MAPPING[my_move] + RESULT_SCORE_MAPPING[result]
    my_total_score += score
f.close()

f = open(FILENAME, 'r')
#q2
for line in f:
    line = line.strip()
    opponent_move = line.split(' ')[0]
    result = line.split(' ')[1]
    my_move = decide_my_move(opponent_move, result)
    score  = SCORE_MAPPING[my_move] + RESULT_SCORE_MAPPING[result]
    score_part_2 += score

print('Total score = ', my_total_score)
print('Score in Q2 = ', score_part_2)