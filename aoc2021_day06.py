def part2(filename,days):
    import math
    with open(filename,'r') as f:
        lines = f.read().split(',')
    for i in range(0,len(lines)):
        lines[i] = int(lines[i])
    
    #Track how many fish are on each date, as they'll all behave the same
    fishdays = [0,0,0,0,0,0,0,0,0]
    for i in range(0,9):
        fishdays[i] = lines.count(i)
    #expected fishdays of test case = [0,1,1,2,1,0,0,0,0]
    #print("fishdays=",fishdays)
    #nextfishdays = [0,0,0,0,0,0,0,0,0]
    for i in range(0,days):
        print("fishday #",i,"=",fishdays)
        nextfishdays = [0,0,0,0,0,0,0,0,0]
        for j in range(0,len(fishdays)):
            if j < 6 or j == 7:
                nextfishdays[j] = fishdays[j+1]
            elif j == 6:
                nextfishdays[j] = fishdays[0] + fishdays[7]
            #nextfishdays[j] = fishdays[j]
        nextfishdays[8] = nextfishdays[8]+fishdays[0]
        
        fishdays = nextfishdays
    
    #sum the list to find the answer
    totalfish = 0
    for fishday in fishdays:
        totalfish = totalfish + fishday

    return totalfish





def part1(filename,days):
    with open(filename,'r') as f:
        lines = f.read().split(',')
    for i in range(0,len(lines)):
        lines[i] = int(lines[i])
    #days = 80
    #print(lines)
    
    for i in range(0,days):
        for j in range(0,len(lines)):
            if lines[j] == 0:
                lines[j] = 6
                lines.append(8)
            else:
                lines[j] -= 1
    return len(lines)


print("Part 1 test answer =",part1('day06input_test1.txt',80))
print("Part 1 answer =",part1('day06input.txt',80))
#First try!  (359999)


print("Part 2 test answer =",part2('day06input_test1.txt',256))
print("Part 2 answer =",part2('day06input.txt',256))
#First try!! (1631647919273)

