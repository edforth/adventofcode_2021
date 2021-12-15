def part1(filename,steps):
    import copy
    with open(filename,'r') as f:
        s = f.read().split('\n\n')
    polymer = s[0]
    pairrules = s[1].splitlines()
    #print(polymer,pairrules)
    for i in range(0,len(pairrules)):
        s = pairrules[i].split(' -> ')
        pairrules[i] = dict(pair = s[0], insert = s[1])
    #print(polymer,pairrules)
    for i in range(0,steps):
        print("step",i+1,"of",steps)
        template = polymer + ''
        polymer = template[0]
        insert = ''
        for j in range(1,len(template)):
            pair = template[j-1] + template[j]
            #print(pair)
            for pairrule in pairrules: 
                #print("pair = ",pair,"pairrule['pair']=",pairrule['pair'],pair == pairrule['pair'], len(pair),len(pairrule['pair']))
                
                if pairrule['pair'] == pair:
                    insert = pairrule['insert']
                    #print("insert=",insert)
                    break
            polymer = polymer + insert + template[j]
    maxelement = max(set(polymer), key=polymer.count)
    minelement = min(set(polymer), key=polymer.count)
    return polymer.count(maxelement) - polymer.count(minelement)







print("Part 1 test 1 answer=",part1('day14input_test1.txt',10))
print("Part 1 answer=",part1('day14input.txt',10))
#First try! (3342)
#print("Part 2 answer=",part1('day14input.txt',40))
# Nope. Waaaaaaay too slow
