FILENAME = 'input.txt'

total_score = 0
badge_score = 0
elf_groups = []

def calc_priority(item):
    priority = 0
    if item.islower():
        priority = ord(item) - 96
    else:
        priority = ord(item) - 38

    return priority


file = open(FILENAME, 'r')
i = 1
for line in file:
    line = line.strip()
    n = len(line)
    first_compartment_items = list(line[:n//2])
    second_compartment_items = list(line[n//2:])
    commom_item = list(set(first_compartment_items).intersection(second_compartment_items))[0]

    total_score += calc_priority(commom_item)

    # solution for 2nd Part below:
    elf_groups.append(line)
    if i%3 == 0:
        group_sticker_item = list(set(elf_groups[0]).intersection(elf_groups[1], elf_groups[2]))[0]
        badge_score += calc_priority(group_sticker_item)
        elf_groups = []

    i += 1

print('Priorities of incorrect items = ',total_score)
print('Elf badge score = ', badge_score)