
def getneighbors(lines,i,j):
    neighbors = []
    #getnorth
    if i != 0:
        neighbors.append(int(lines[i-1][j]))

    #getsouth
    if i != len(lines)-1:
        neighbors.append(int(lines[i+1][j]))

    #getwest
    if j != 0:
        neighbors.append(int(lines[i][j-1]))

    #geteast
    if j != len(lines[i])-1:
        neighbors.append(int(lines[i][j+1]))
    return neighbors



def part1(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    #print("lines=",lines)
    totalrisk = 0
    for i in range(0,len(lines)):
        for j in range(0,len(lines[i])):
            neighbors = getneighbors(lines,i,j)
            #print("neighbors=",neighbors)
            point = int(lines[i][j])
            if point < min(neighbors):
                totalrisk = totalrisk + point + 1
    return totalrisk

def part2(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    



print("Part 1 test 1 answer=",part1('day09input_test1.txt'))
print("Part 1 answer=",part1('day09input.txt'))
#First try!


#print("Part 2 test 1 answer=",part2('day09input_test1.txt'))
#print("Part 2 answer=",part2('day09input.txt'))