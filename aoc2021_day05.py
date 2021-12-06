def getinput(filename):
    response = []
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        s = line.split('->')
        startcoords = s[0].strip().split(',')
        startx = startcoords[0]
        starty = startcoords[1]
        endcoords = s[1].strip().split(',')
        endx = endcoords[0]
        endy = endcoords[1]
        #s[1] = s[1].strip().split(',')
        #response.append(dict(start = s[0], end = s[1]))
        response.append(dict(start = dict(x = int(startx), y = int(starty)), end = dict(x = int(endx), y = int(endy))))
    return response


def getlinepoints(linecoords):  #dict(start,end) #start = dict(x,y) #end = dict(x,y)
    linepoints = []
    x1 = linecoords['start']['x']
    y1 = linecoords['start']['y']
    x2 = linecoords['end']['x']
    y2 = linecoords['end']['y']
    currentpoint = [x1,y1]
    linepoints.append(currentpoint)
    loopmax = max(abs(x2-x1),abs(y2-y1))
    #y = (slope)(x) + intercept
    #y-(slope)(x) = intercept
    if (x2-x1) == 0:
        slope = 'undefined'
    else: 
        slope = ((y2 - y1) / (x2 - x1))
    #intercept = 0 - (slope*x1)
    #print("x1=",x1,"y1=",y1,"x2=",x2,"y2=",y2,"slope=",slope)
    loopcount = 0
    while currentpoint != [x2,y2]:
        if x2 - x1 == 0:
            nextx = currentpoint[0]
            if y2 - y1 > 0:
                nexty = currentpoint[1]+1
            elif y2 -y1 < 0:
                nexty = currentpoint[1]-1
            else:
                print("This really shouldn't happen and I have no idea what to do")
                quit()
        elif x2 - x1 > 0:
            nextx = currentpoint[0] + 1
            nexty = int((slope*(nextx-currentpoint[0]))+currentpoint[1]) #pointslope: y=m(x−x1)+y1
        elif x2 - x1 < 0:
            nextx = currentpoint[0] - 1
            nexty = int((slope*(nextx-currentpoint[0]))+currentpoint[1]) #pointslope: y=m(x−x1)+y1
        #nexty = (slope*nextx)+intercept   #y=mx+b
      
        nextpoint = [nextx,nexty]
        
        #print("nextpoint=",nextpoint)
        linepoints.append(nextpoint)
        currentpoint = nextpoint
        loopcount += 1
        if loopcount > loopmax+20:
            print("WHY GOD WHY!!!!")

            break


    #print("slope=",slope)


    return linepoints 

    

def part1(input):
    data = getinput(input)
    #print(data)
    ventpoints = []
    for datum in data:
        if datum['start']['x'] == datum['end']['x'] or datum['start']['y'] == datum['end']['y']:
            linepoints = getlinepoints(datum)
            #print("datum=",datum)
            #print("linepoints=",linepoints)
            for linepoint in linepoints: 
                #print("linepoint=",linepoint)
                inventpoints = False
                for ventpoint in ventpoints:
                    #print("linepoint=",linepoint,"ventpoint['point']=",ventpoint['point'])
                    if ventpoint['point'] == linepoint:
                        ventpoint['qty'] += 1
                        inventpoints = True
                if inventpoints == False:
                    ventpoints.append(dict(point = linepoint, qty = 1))
    #print("ventpoints=",ventpoints)
    pointswithmultiplevents = 0
    for ventpoint in ventpoints:
        if ventpoint['qty'] > 1:
            pointswithmultiplevents += 1
    return pointswithmultiplevents


print("part 1 test answer = ",part1('day05input_test1.txt'))
#print("part 1 answer = ",part1('day05input.txt'))
#Test input finally worked with a lot of hacking.  Incorrect answer on full input (13) - 
# My "overflow" check is triggering a lot.  I'll need to figure out what's going on :(
#LOL.  The problem was still having the overflow check at all.  Some of the legit lines in the answer are very long.
#Correct answer after fixing that, although it took a SUPER LONG time to resolve, so I'm clearly missing some optimization (5147)


def part2(input):
    data = getinput(input)
    #print(data)
    ventpoints = []
    for datum in data:
        linepoints = getlinepoints(datum)
        #print("datum=",datum)
        #print("linepoints=",linepoints)
        for linepoint in linepoints: 
            #print("linepoint=",linepoint)
            inventpoints = False
            for ventpoint in ventpoints:
                #print("linepoint=",linepoint,"ventpoint['point']=",ventpoint['point'])
                if ventpoint['point'] == linepoint:
                    ventpoint['qty'] += 1
                    inventpoints = True
            if inventpoints == False:
                ventpoints.append(dict(point = linepoint, qty = 1))
    #print("ventpoints=",ventpoints)
    pointswithmultiplevents = 0
    for ventpoint in ventpoints:
        if ventpoint['qty'] > 1:
            pointswithmultiplevents += 1
    return pointswithmultiplevents


print("part 2 test answer = ",part2('day05input_test1.txt'))
print("part 2 answer = ",part2('day05input.txt'))
#Glad I guessed that Part 2 was going to use all lines
#took 35 minutes to run, but got it first try! (16925)