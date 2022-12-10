FILENAME = 'input.txt'


f = open(FILENAME, 'r')

overlap_assignments_count = 0
partial_overlap_count = 0

for line in f:
    line = line.strip()
    assignments = line.split(',')
    first_pair = assignments[0].split('-')
    second_pair = assignments[1].split('-')
    if int(first_pair[0]) <= int(second_pair[0]) and int(first_pair[1]) >= int(second_pair[1]):
        overlap_assignments_count += 1
    elif int(second_pair[0]) <= int(first_pair[0]) and int(second_pair[1]) >= int(first_pair[1]):
        overlap_assignments_count += 1

    #sol for partial overlaped count
    first_pair_list = set(range(int(first_pair[0]), int(first_pair[1]) + 1))
    second_pair_list = set(range(int(second_pair[0]), int(second_pair[1]) + 1))

    if first_pair_list & second_pair_list:
        partial_overlap_count += 1
f.close()
print('Overlapping count = ', overlap_assignments_count)    
print('Partial count = ', partial_overlap_count)
