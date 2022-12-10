lines = []
x = 1
interesting_cycle_values = 0
cycle = 1

crt_row = 0
screen = [[x for x in  '.'*40], [x for x in  '.'*40], [x for x in  '.'*40], [x for x in  '.'*40], [x for x in  '.'*40], [x for x in  '.'*40]]

def draw_pixel():
    pixel = (cycle - 1)%40
    stripe = [x - 1, x, x+1]
    if pixel in stripe:
        screen[crt_row][pixel] = '#'

if __name__ == "__main__":
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.strip('\n')
        command = line.split(' ')[0]

        if command == 'addx':
            arg = int(line.split(' ')[1])
            
            for i in range(2):
                draw_pixel()
                if (cycle - 20) % 40 == 0 or cycle == 20:
                    interesting_cycle_values += (x * cycle)
                if i == 1:
                    x += arg
                cycle += 1
                crt_row = cycle // 40
        else:
            draw_pixel()
            if (cycle - 20) % 40 == 0 or cycle == 20:
                interesting_cycle_values += (x * cycle)
            cycle += 1
            crt_row = cycle // 40

    print(f'Part 1 : {interesting_cycle_values}')

    for i in screen:
        print(''.join(i))