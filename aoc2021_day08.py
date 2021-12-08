
#o = abcefg
#1 = cf
#2 = acdeg
#3 = acdfg
#4 = bcdf
#5 = abdfg
#6 = abdefg
#7 = acf
#8 = abcdefg
#9 = abcdfg

def getdigitpatterns(signalpatterns):
    digitpatterns = dict(one = '', two = '', three = '', four = '', five = '', six = '', seven = '', eight = '', nine = '', zero = '')
    digitpatterns = dict(one = '', two = '', three = '', four = '', five = '', six = '', seven = '', eight = '', nine = '', zero = '')
    for signalpattern in signalpatterns:
        if len(signalpattern) == 2:
            digitpatterns['one'] = signalpattern
        elif len(signalpattern) == 4:
            digitpatterns['four'] = signalpattern
        elif len(signalpattern) == 3:
            digitpatterns['seven'] = signalpattern
        elif len(signalpattern) == 7:
            digitpatterns['eight'] = signalpattern
    #find 6, because it had exactly one item missing from 7
    for signalpattern in signalpatterns:
        missingfromseven = 0
        if len(signalpattern) == 6:
            for char in digitpatterns['seven']:
                #print("signalpattern=",signalpattern,"char=",char)
                if char not in signalpattern:
                    missingfromseven += 1
                    #print("seven=",digitpatterns['seven'],char,"NOT IN SEVEN","missingfromseve=",missingfromseven)

            if missingfromseven == 1:
                digitpatterns['six'] = signalpattern
                #print("found the six!!!")
    #find the 5, because all of the values are in the six
    for signalpattern in signalpatterns:
        if len(signalpattern) == 5:
            #print("looking for five: signalpattern=",signalpattern)
            presentinsix = 0
            for char in signalpattern:
                if char in digitpatterns['six']:
                    presentinsix += 1
            if presentinsix == 5:
                digitpatterns['five'] = signalpattern
                #print("found the five!!")
    #find the 9, because it includes everything from the five and it's not the six
    for signalpattern in signalpatterns:
        if len(signalpattern) == 6 and signalpattern != digitpatterns['six']:
            presentinnine = 0
            for char in digitpatterns['five']:
                if char in signalpattern:
                    presentinnine += 1
            if presentinnine == 5:
                digitpatterns['nine'] = signalpattern
                #print("found the nine!!")
    #find the 3, because they're all in nine, and we haven't otherwise found it
    for signalpattern in signalpatterns:
        if len(signalpattern) == 5 and signalpattern != digitpatterns['five']:
            presentinnine = 0
            for char in signalpattern:
                if char in digitpatterns['nine']:
                    presentinnine +=1 
            if presentinnine == 5:
                #print("foundthethree!!")
                digitpatterns['three'] = signalpattern
    #find the 2 and six because they're the only ones left of their lengths
    for signalpattern in signalpatterns:
        if len(signalpattern) == 5 and signalpattern != digitpatterns['three'] and signalpattern != digitpatterns['five']:
            digitpatterns['two'] = signalpattern
            #print("found the two!")
        elif len(signalpattern) == 6 and signalpattern != digitpatterns['six'] and signalpattern != digitpatterns['nine']:
            digitpatterns['zero'] = signalpattern
            #print("found the zero!")
    return digitpatterns




def part1(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    digitcount = dict(one = 0, two = 0, three = 0, four = 0, five = 0, six = 0, seven = 0, eight = 0, nine = 0, zero = 0)
    for line in lines:
        s = line.split('|')
        s2 = s[1].split()
        #print("s2=",s2)
        for char in s2:
            if len(char) == 2:
                digitcount['one'] +=  1
            elif len(char) == 4:
                digitcount['four'] +=  1
            elif len(char) == 3:
                digitcount['seven'] +=  1
            elif len(char) == 7:
                digitcount['eight'] +=  1
    part1answer = digitcount['one'] + digitcount['four'] + digitcount['seven'] + digitcount['eight']
    return part1answer

def part2(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    totalvalue = 0
    for line in lines:
        s = line.split('|')
        signalpatterns = s[0].split()
        outputvalues = s[1].split()
        digits = getdigitpatterns(signalpatterns)
        #print("digits=",digits)
        #print("outputvalues=",outputvalues)
        linevalue = ""
        for outputvalue in outputvalues:
            #print("outputvalue=",outputvalue)
            for key, value in digits.items():
                #print("key=",key,"value=",value)
                charcount = 0
                for char in outputvalue:
                    if char in value:
                        charcount += 1
                if charcount == len(value) and charcount == len(outputvalue):
                    if key == 'one':
                        appendvalue = 1
                    elif key == 'two':
                        appendvalue = 2
                    elif key == 'three':
                        appendvalue = 3
                    elif key == 'four':
                        appendvalue = 4
                    elif key == 'five':
                        appendvalue = 5
                    elif key == 'six':
                        appendvalue = 6
                    elif key == 'seven':
                        appendvalue = 7
                    elif key == 'eight':
                        appendvalue = 8
                    elif key == 'nine':
                        appendvalue = 9
                    elif key == 'zero':
                        appendvalue = 0
                    #print("appendvalue=",appendvalue)
                    linevalue = linevalue + str(appendvalue)
        #print("linevalue=",linevalue)
        totalvalue += int(linevalue)
    return totalvalue
                    


        



#print("Part 1 test 1 answer=",part1('day08input_test1.txt'))
#print("Part 1 test 2 answer=",part1('day08input_test2.txt'))
print("Part 1 answer=",part1('day08input.txt'))
#first try!   

#print("Part 2 test 1 answer=",part2('day08input_test1.txt'))
#print("Part 2 test 2 answer=",part2('day08input_test2.txt'))
print("Part 2 answer=",part2('day08input.txt'))
#Yeesh, that was really fiddly, and I know this is super inefficient.
# I'm guessing I can figure out the numbers in fewer passes, but whatever
#Got there first try!  (1011823)
