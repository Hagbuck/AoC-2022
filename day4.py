f = open("input.txt","r")
lines = f.readlines()

count_fully_contain = 0
count_overlap = 0

def isFullyContain(aa, ab, ba, bb):
    return True if aa >= ba and ab <= bb or ba >= aa and bb <= ab else False
    
def isOverlap(aa, ab, ba, bb):
    if aa >= ba and aa <= bb or ba >= aa and bb <= aa:
        return True
    return False

for line in lines:
    elfA, elfB = line.split(",")
    aa, ab = elfA.split("-")
    ba, bb = elfB.split("-")
    
    aa = int(aa)
    ab = int(ab)
    ba = int(ba)
    bb = int(bb)
    
    if isFullyContain(aa, ab, ba, bb):
        count_fully_contain += 1
   
    if isOverlap(aa, ab, ba, bb) or isOverlap(ba, bb, aa, ab) or isFullyContain(aa, ab, ba, bb):
        count_overlap += 1
    else:
        print("Not on : " + line)
    
print("Part 1 : " + str(count_fully_contain))
print("Part 2 : " + str(count_overlap))

f.close()