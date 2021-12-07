def part1(filename):
    with open(filename,'r') as f:
        lines = f.read().split(',')
    for i in range(0,len(lines)):
        lines[i] = int(lines[i])
    print(lines)
    leftmost = min(lines)
    rightmost = max(lines)
    print(leftmost,rightmost)
    lowestfuel = ""
    for i in range(leftmost,rightmost+1):
        fuelused = 0
        for line in lines:
            fuelused = fuelused + abs(i-line)
        if lowestfuel == "" or fuelused < lowestfuel:
            lowestfuel = fuelused 
    return lowestfuel


def part2(filename):
    with open(filename,'r') as f:
        lines = f.read().split(',')
    for i in range(0,len(lines)):
        lines[i] = int(lines[i])
    print(lines)
    leftmost = min(lines)
    rightmost = max(lines)
    print(leftmost,rightmost)
    lowestfuel = ""
    for i in range(leftmost,rightmost+1):
        fuelused = 0
        for line in lines:
            fuelused = fuelused + abs(i-line)*(abs(i-line)+1)/2 
        if lowestfuel == "" or fuelused < lowestfuel:
            lowestfuel = fuelused 
    return lowestfuel


print("Part 1 test answer=",part1('day07input_test1.txt'))
print("Part 1 answer=",part1('day07input.txt'))
#Correct first try

print("Part 2 test answer=",part2('day07input_test1.txt'))
print("Part 2 answer=",part2('day07input.txt'))
#Correct first try!!!  Hooray for math knowledge!