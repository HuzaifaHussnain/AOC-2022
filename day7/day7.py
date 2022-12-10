lines = []
total_size = 0
space_to_be_cleaned = 0
total_size_of_dir_to_be_cleaned = 0

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.dirs = []
    
    def get_dir(self, name):
        dir_ptr = None
        for i in self.dirs:
            if i.name == name:
                dir_ptr = i

        return dir_ptr

    def cal_dir_size(self):
        global total_size
        global total_size_of_dir_to_be_cleaned
        for i in self.dirs:
            self.size += i.cal_dir_size()
        if self.size <= 100000:
            total_size += self.size
        if self.size >= space_to_be_cleaned and self.size < total_size_of_dir_to_be_cleaned:
            total_size_of_dir_to_be_cleaned = self.size

        return self.size

def initialize_tree():
    root = Node('/', None)
    current = None

    for line in lines:
        line = line.strip('\n')
        if line.startswith('$'):
            # it is a command
            command = line.split(' ')[1]
            if command == 'cd':
                cd_arg = line.split(' ')[2]
                if cd_arg == '/':
                    current = root
                elif cd_arg == '..':
                    current = current.parent
                else:
                    # $ cd a
                    current = current.get_dir(cd_arg)
        else:
            p1 = line.split(' ')[0]
            p2 = line.split(' ')[1]
            
            if p1.isnumeric():
                # file
                current.size += int(p1)
            elif p1 == 'dir':
                current.dirs.append(Node(p2, current))
    
    return root

if __name__ == "__main__":
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()

    root = initialize_tree()
    root.cal_dir_size()
    print('Part 1: ', total_size)
    print('root size = ', root.size)
    space_to_be_cleaned = 30000000 - (70000000 - root.size)
    print('sapce to clean = ', space_to_be_cleaned)
    total_size_of_dir_to_be_cleaned = 70000000 # initalize with max possible size
    root = initialize_tree()
    root.cal_dir_size()

    print('Part 2: ', total_size_of_dir_to_be_cleaned)

    