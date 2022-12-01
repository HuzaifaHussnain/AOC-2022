FILENAME='q1.txt'

elfs_cals = []
file = open(FILENAME, 'r')
cal_sum = 0
max_calories = [0,0,0]
for line in file:
    if line.strip():
        cal_sum += int(line)
    else:
        elfs_cals.append(cal_sum)
        if cal_sum > min(max_calories):
            max_calories.remove(min(max_calories))
            max_calories.append(cal_sum)
        cal_sum = 0

print('MAX calories of a single elf = ', max(max_calories))
print('Total calories of top 3 elfs = ', sum(max_calories))
