def part1(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()

    bitarray = []
    for i in range(0,len(lines[0])):
        bitarray.append(0)
    for line in lines:
        for i in range(0,len(line)):
            bitarray[i] = bitarray[i] + int(line[i])
        
    #assemble gama 
    gamarate = ""
    epsilonrate = ""
    for i in range(0,len(line)):
        if bitarray[i] > len(lines)/2:
            gamarate = gamarate + "1"
            epsilonrate = epsilonrate + "0"
        else:
            gamarate = gamarate + "0"
            epsilonrate = epsilonrate + "1"
    gamarate = int(gamarate,2)
    epsilonrate = int(epsilonrate,2)
    #print("gama-",gamarate,"epsilon=",epsilonrate)
    return(gamarate*epsilonrate)


print("Part 1 test answer = ",part1('day03input_test1.txt'))
print("Part 1 answer = ",part1('day03input.txt'))
#Correct first try! (1307354)


#Part 2
def part2(filename):
    import copy
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    bitposition = 0
    while len(lines) > 1:
        newlines = []
        bitsum = 0 
        for line in lines:
            bitsum = bitsum + int(line[bitposition])
        if bitsum >= len(lines) / 2:
            mostcommonbit = '1'
        else:
            mostcommonbit = '0'
        for i in range(0,len(lines)):
            if lines[i][bitposition] == mostcommonbit:
                newlines.append(lines[i])
        lines = copy.deepcopy(newlines)
        bitposition = bitposition + 1
        print("lines = ",lines)
        print("newlines = ",newlines)
    oxygengeneratorrating = int(lines[0],2)


    #get CO2 scrubber
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    bitposition = 0
    while len(lines) > 1:
        newlines = []
        bitsum = 0 
        for line in lines:
            bitsum = bitsum + int(line[bitposition])
        if bitsum >= len(lines) / 2:
            leastcommonbit = '0'
        else:
            leastcommonbit = '1'
        for i in range(0,len(lines)):
            if lines[i][bitposition] == leastcommonbit:
                newlines.append(lines[i])
        lines = copy.deepcopy(newlines)
        bitposition = bitposition + 1
    CO2scrubberrating = int(lines[0],2)
    print("O2=",oxygengeneratorrating,"CO2=",CO2scrubberrating)
    return (oxygengeneratorrating * CO2scrubberrating)



print("Part 2 answer = ",part2('day03input.txt'))
#Correct first try! (482500)
 



