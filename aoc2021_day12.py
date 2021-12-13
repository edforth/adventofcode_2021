

def part1(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    connectedrooms = []
    allrooms = []
    for line in lines:
        splits = line.split('-')
        connectedrooms.append(splits)
        for split in splits:
            if split not in allrooms:
                allrooms.append(split)
    print("allrooms=",allrooms)
    print("connectedrooms=",connectedrooms)
    for aroom in allrooms:
        adjacentrooms = []
        



    #paths = getgraph(lines)




    




print("Part 1 test 1 answer=",part1('day12input_test1.txt'))
#print("Part 1 test 2 answer=",part1('day12input_test2.txt'))
#print("Part 1 test 3 answer=",part1('day12input_test3.txt'))
#print("Part 1 answer=",part1('day12input.txt'))

#print("Part 2 test 1 answer=",part2('day12input_test1.txt'))
#print("Part 2 answer=",part2('day12input.txt'))
