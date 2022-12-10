import math

head = [0,0]
tail = [0,0]
samll_rope = [[0,0], [0,0]]
large_rope = [
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0]
]
tail_positions = [[0,0]]

def move_tail(leading_knot, trailing_knot, knot_position=None):
    if math.dist(leading_knot, trailing_knot) >= 2.0:
        # if abs(leading_knot[0] - trailing_knot[0]) > abs(leading_knot[1] - trailing_knot[1]):
        if leading_knot[0] > trailing_knot[0]:
            trailing_knot[0] += 1
        if leading_knot[0] < trailing_knot[0]:
            trailing_knot[0] -= 1
        # if abs(leading_knot[1] - trailing_knot[1]) > abs(leading_knot[0] - trailing_knot[0]):
        if leading_knot[1] > trailing_knot[1]:
            trailing_knot[1] += 1
        if leading_knot[1] < trailing_knot[1]:
            trailing_knot[1] -= 1

        if trailing_knot not in tail_positions and knot_position==9:
            tail_positions.append(list(trailing_knot))
    print(math.dist(head, trailing_knot))

if __name__ == "__main__":
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()

    for line in lines:
        line = line.strip('\n')
        direction = line.split(' ')[0]
        moves = int(line.split(' ')[1])

        for i in range(moves):
            head = samll_rope[0]
            if direction == 'R':
                head[0] += 1
            if direction == 'L':
                head[0] -= 1
            if direction == 'U':
                head[1] += 1
            if direction == 'D':
                head[1] -= 1
            
            move_tail(head, samll_rope[1],9)

        # Part two
        # for i in range(moves):
        #     head = large_rope[0]
        #     if direction == 'R':
        #         head[0] += 1
        #     if direction == 'L':
        #         head[0] -= 1
        #     if direction == 'U':
        #         head[1] += 1
        #     if direction == 'D':
        #         head[1] -= 1
            
        #     for i in range(1, 10):
        #         move_tail(large_rope[i-1], large_rope[i], i)

    print(len(tail_positions))
    # print(tail_positions)