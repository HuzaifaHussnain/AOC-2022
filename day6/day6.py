f = open('input.txt', 'r')
lines = f.readlines()
input_string = lines[0].strip('\n')

def find_marker_pos(data, length):
    marker_pos = 0
    for i in range(len(data)):
        window = data[i: i + length]
        if len(set(window)) == length:
            marker_pos = i + length
            break
    return marker_pos

print(f"Part 1: {find_marker_pos(input_string, 4)}")
print(f"Part 2: {find_marker_pos(input_string, 14)}")
