
stacks = []
for i in range(10):
    stacks.append(list())

def initialize_stacks():
    for line in open('input.txt', 'r'):
        if '[' in line:
            for i in range(1, len(line) - 1, 4):
                if line[i] != ' ':
                    stacks[(i)//4].append(line[i])

    for i in range(len(stacks)):
        stacks[i].reverse()

def move_crates():
    for line in open('input.txt', 'r'):
        if 'move' in line:
            instruction = line.split(" ")
            moves = int(instruction[1])
            source = int(instruction[3])
            dest = int(instruction[5])

            for i in range(moves):
                stacks[dest - 1].append(stacks[source - 1].pop())

def move_multiple_crates_at_once():
    for line in open('input.txt', 'r'):
        if 'move' in line:
            instruction = line.split(" ")
            moves = int(instruction[1])
            source = int(instruction[3])
            dest = int(instruction[5])

            temp = []
            for i in range(moves):
                if stacks[source - 1]:
                    temp.append(stacks[source - 1].pop())
            temp.reverse()
            stacks[dest - 1].extend(temp)


initialize_stacks()
# move_crates()
move_multiple_crates_at_once()
for item in stacks:
    if item:
        print(item.pop())