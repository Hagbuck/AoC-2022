f = open("input.txt","r")
lines = f.readlines()

def getCommonItem(rucksack):
    compartmentA = rucksack[0:int((len(rucksack) - 1)/ 2)]
    compartmentB = rucksack[int((len(rucksack) - 1)/ 2):len(rucksack)]
    for item in compartmentA:
        if item in compartmentB:
            return item
    return None
    
def computePriorityOfItem(item):
    priority = ord(item) - ord('a') + 1 if item > 'a' else ord(item) - ord('A') + 27
    #print(item + " : " + str(priority))
    return priority
    
def getCommonItemBetweenRucksacks(rucksacks):   
    commons = list(rucksacks[0])
    
    for item in rucksacks[0]:
        for i in range(1, len(rucksacks)):
            rucksack = rucksacks[i]
            if item not in rucksack:
                commons.remove(item)
                #print(str(commons) + " : rm " + item)
                break;
    
    """    
    print("#####################")
    print(rucksacks[0])
    print(rucksacks[1])
    print(rucksacks[2])
    print(commons)
    print("#####################")"""
    return commons[0]

# Part 1
total = 0
for line in lines:
    item = getCommonItem(line)
    total += computePriorityOfItem(item)
    
print("Part 1 : " + str(total))

# Part 2
total = 0
i = 0
while i < len(lines):
    rucksacks = []
    rucksacks.append(lines[i])
    rucksacks.append(lines[i+1])
    rucksacks.append(lines[i+2])
    
    i += 3
    
    badge = getCommonItemBetweenRucksacks(rucksacks)
    total += computePriorityOfItem(badge)

print("Part 2 : " + str(total))

f.close()