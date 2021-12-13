
def incrementenergy(octopodes):
    for i in range(0,len(octopodes)):
        for j in range(0,len(octopodes[0])):
            octopodes[i][j] = octopodes[i][j] + 1
    return octopodes
    
def checkflashableoctopodes(octopodes):
    flashableoctopodes = 0
    for i in range(0,len(octopodes)):
        for j in range(0,len(octopodes[0])):
            if octopodes[i][j] > 9:
                flashableoctopodes += 1
    return flashableoctopodes


def flashoctopodes(octopodes):
    flashcounter = 0
    while checkflashableoctopodes(octopodes) > 0:
        #print("Flashing! Flashable Octopodes = ",checkflashableoctopodes(octopodes))
        for i in range(0,len(octopodes)):
            for j in range(0,len(octopodes[0])):
                if octopodes[i][j] > 9:
                    octopodes[i][j] = 0 
                    flashcounter += 1
                    if i > 0 and j > 0 and octopodes[i-1][j-1] != 0:
                        octopodes[i-1][j-1] += 1
                    if i > 0 and octopodes[i-1][j] != 0:
                        octopodes[i-1][j] += 1
                    if i > 0 and j < len(octopodes[0])-1 and octopodes[i-1][j+1] != 0:
                        octopodes[i-1][j+1] += 1
                    if j > 0 and octopodes[i][j-1] != 0:
                        octopodes[i][j-1] += 1
                    if j < len(octopodes[0])-1 and octopodes[i][j+1] != 0:
                        octopodes[i][j+1] += 1
                    if i < len(octopodes)-1 and j > 0 and octopodes[i+1][j-1] != 0:
                        octopodes[i+1][j-1] += 1
                    if i < len(octopodes)-1 and octopodes[i+1][j] != 0:
                        octopodes[i+1][j] += 1
                    if i < len(octopodes)-1 and j < len(octopodes[0])-1 and octopodes[i+1][j+1] != 0:
                        octopodes[i+1][j+1] += 1
        #print("end of loop # of flashable octopodes=",checkflashableoctopodes(octopodes))         
    return [octopodes,flashcounter]

def checksync(octopodes):
    totaloctopodes = len(octopodes) * len(octopodes[0])
    synccounter = 0
    for i in range(0,len(octopodes)):
        for j in range(0,len(octopodes[0])):
            if octopodes[i][j] == 0:
                synccounter += 1
    if synccounter == totaloctopodes:
        return True
    else:
        return False



def part1(filename, steps):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    octopodes = []
    flashcounter = 0
    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        octopodes.append(row)
    for i in range(0,steps):
        #print("after step #",i+1)
        octopodes = incrementenergy(octopodes)
        #print(octopodes)
        #print("# of flashable octopodes = ",checkflashableoctopodes(octopodes))
        flashreturn = flashoctopodes(octopodes)
        octopodes = flashreturn[0]
        flashcounter += flashreturn[1]
        #print("postflash octopodes = ",octopodes)
    return flashcounter
    
def part2(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    octopodes = []
    firstsync = 0
    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        octopodes.append(row)
    i = 1
    while 1:
        #print("after step #",i+1)
        octopodes = incrementenergy(octopodes)
        #print(octopodes)
        #print("# of flashable octopodes = ",checkflashableoctopodes(octopodes))
        flashreturn = flashoctopodes(octopodes)
        octopodes = flashreturn[0]
        #print("postflash octopodes = ",octopodes)
        if firstsync == 0 and checksync(octopodes):
            return i
        i += 1
    return firstsync





print("Part 1 test 1 answer=",part1('day11input_test1.txt',100))
#print("Part 1 test 2 answer=",part1('day11input_test2.txt',2))
print("Part 1 answer=",part1('day11input.txt',100))
#Got it!  (1661)


print("Part 2 test 1 answer=",part2('day11input_test1.txt'))
print("Part 2 answer=",part2('day11input.txt'))
#Got there! (334)   Pretty easy because of how I did part one, but I had some trouble removing the step counter, and just looping until it's complete
# I think I could have a cleaner solution here