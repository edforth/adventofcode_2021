
"""
#THis didn't work out
def part1(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    totalsyntaxerror = 0
    for line in lines:
        charcount = dict(startcurl = 0, endcurl = 0, 
            startparen = 0, endparen = 0, startsquare = 0, 
            endsquare = 0, startangle = 0, endangle = 0)
        firstillegalchar = ''
        #print(charcount)
        for char in line:
            if char == '{':
                charcount['startcurl'] +=1
            elif char == '}':
                charcount['endcurl'] +=1
            elif char == '(':
                charcount['startparen'] +=1
            elif char == ')':
                charcount['endparen'] +=1
            elif char == '[':
                charcount['startsquare'] +=1
            elif char == ']':
                charcount['endsquare'] +=1
            elif char == '<':
                charcount['startangle'] +=1
            elif char == '>':
                charcount['endangle'] +=1
            
            if firstillegalchar == '' and (charcount['endcurl'] > charcount['startcurl']
                or charcount['endparen'] > charcount['startparen'] or charcount['endsquare'] > charcount['startsquare']
                or charcount['endangle'] > charcount['startangle']):
                firstillegalchar = char
        if firstillegalchar == '':
            totalsyntaxerror += 0
        elif firstillegalchar == ')':
            totalsyntaxerror += 3
        elif firstillegalchar == ']':
            totalsyntaxerror += 57
        elif firstillegalchar == '}':
            totalsyntaxerror += 1197
        elif firstillegalchar == '>':
            totalsyntaxerror += 25137 
        print(line)
        print(charcount)
        print(firstillegalchar)

    return totalsyntaxerror
            
"""

def part1(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    totalsyntaxerror = 0
    for line in lines:
        openednestings = []
        firstillegalcharacter = ''
        for char in line:
            if firstillegalcharacter != '':
                #print("BROKE!","firstillegal=",firstillegalcharacter,"totalsyntax",totalsyntaxerror)
                break
            if char == '(' or char == '[' or char == '{' or char == '<':
                openednestings.append(char)
            elif char == ')':
                if openednestings[len(openednestings) - 1] == '(':
                    openednestings.pop()
                else:
                    firstillegalcharacter = ')'
                    totalsyntaxerror += 3
            elif char == '}':
                if openednestings[len(openednestings) - 1] == '{':
                    openednestings.pop()
                else:
                    firstillegalcharacter = '}'
                    totalsyntaxerror += 1197
            elif char == ']':
                if openednestings[len(openednestings) - 1] == '[':
                    openednestings.pop()
                else:
                    firstillegalcharacter = ']'
                    totalsyntaxerror += 57
            elif char == '>':
                if openednestings[len(openednestings) - 1] == '<':
                    openednestings.pop()
                else:
                    firstillegalcharacter = '>'
                    totalsyntaxerror += 25137
        #print("line=",line,"opennestings=",openednestings,"firstillegal=",firstillegalcharacter,"totalsyntax",totalsyntaxerror)
    return totalsyntaxerror

def part2(filename):
    import math
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    linescores = []
    for line in lines:
        openednestings = []
        incompletelinescores = []
        linecorrupted = False
        for i in range(0,len(line)):
            char = line[i]
            if char == '(' or char == '[' or char == '{' or char == '<':
                openednestings.append(char)
            elif char == ')':
                if openednestings[len(openednestings) - 1] == '(':
                    openednestings.pop()
                else:
                    linecorrupted = True
            elif char == '}':
                if openednestings[len(openednestings) - 1] == '{':
                    openednestings.pop()
                else:
                    linecorrupted = True
            elif char == ']':
                if openednestings[len(openednestings) - 1] == '[':
                    openednestings.pop()
                else:
                    linecorrupted = True
            elif char == '>':
                if openednestings[len(openednestings) - 1] == '<':
                    openednestings.pop()
                else:
                    linecorrupted = True
            if i == len(line) - 1 and linecorrupted == False:
                linescore = 0 
                #print("line=",line,"opennestings=",openednestings)
                
                openednestings.reverse()
                #print("22222line=",line,"opennestings=",openednestings)

                for char in openednestings:
                    #print("char=",char)
                    linescore = linescore * 5
                    if char == '(':
                        linescore = linescore + 1
                        #print(char,"= )")
                    elif char == '[':
                        linescore = linescore + 2
                        #print(char,"= ]")
                    elif char == '{':
                        linescore = linescore + 3
                        #print(char,"= }")
                    elif char == '<':
                        linescore = linescore + 4
                        #print(char,"= >")
                    #print("linescore=",linescore)
                linescores.append(linescore)
    #print("linescores=",linescores)
    linescores.sort()
    #print("linescores=",linescores)
    return linescores[math.floor(len(linescores)/2)]
            

            






print("Part 1 test 1 answer=",part1('day10input_test1.txt'))
print("Part 1 answer=",part1('day10input.txt'))
#Got it right! (367059)

print("Part 2 test 1 answer=",part2('day10input_test1.txt'))
print("Part 2 answer=",part2('day10input.txt'))
#Wrong answer - Too high :(  (2026371161)
#Guess I need to round down?   It's grabbing the 27th out of 51 and not the 26th.  Not sure why it worked on the test.
#Switching over to math.floor worked