import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

f = open("input.txt","r")
lines = f.readlines()


def isVisible(m, y, x):

    #print("LEFT  : " + str(m[y][x]) + " > " + str(max(m[y][:x])) + " : " + str(m[y][:x]))
    #print("RIGHT : " + str(m[y][x]) + " > " + str(max(m[y][x+1:])) + " : " + str(m[y][x+1:]))
    
    if y == 0 or y == len(m)-1 or x == 0 or x == len(m[y])-1: # On the Edge
        return True
        
    elif m[y][x] > max(m[y][:x]): # On the left
        return True
    elif m[y][x] > max(m[y][x+1:]): # On the right
        return True
    
    return False

def scoreOfOneDirection(m, y, x, my, mx):
    score = 0
    sx = x + mx
    sy = y + my
    
    while sx < len(m[y]) and sx >= 0 and sy < len(m) and sy >= 0:
        score += 1
        if m[sy][sx] < m[y][x]:
            sx += mx
            sy += my
        else:
            break
        
    #print("[" + str(m[y][x]) + "](" + str(x) + ":" + str(y) + ") got a score of (" + str(score) + ") on " + str(my) + ":" + str(mx))
    return score

def computeScore(m, y, x):   
    return scoreOfOneDirection(m, y, x, -1, 0) * scoreOfOneDirection(m, y, x, 1, 0) * scoreOfOneDirection(m, y, x, 0, -1) * scoreOfOneDirection(m, y, x, 0, 1)
    

def countVisibleTree(m):
    inv_map = list(zip(*map))

    out = ""
    count = 0
    
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            color = bcolors.ENDC

            if isVisible(m, y, x) or isVisible(inv_map, x, y):
                color = bcolors.OKGREEN
                count += 1
            else:
                color = bcolors.OKBLUE          
            
            out += color + str(m[y][x]) + bcolors.ENDC
        out += "\n"
    print(out)
    return count
    
def getBestSpotTreeScore(m):
    out = ""
    max_score = 0
    
    for y in range(1, len(m)-1):
        for x in range(1, len(m[y])-1):
            score = computeScore(m, y, x)
            #print(">>[" + str(m[y][x]) + "](" + str(x) + ":" + str(y) + ") got a score of  " + str(score))
            if score > max_score:
                max_score = score
                #print(">>> [" + str(m[y][x]) + "](" + str(x) + ":" + str(y) + ") is the best with " + str(max_score))

    return max_score
    
    
map = []
y = 0
for line in lines:
    map.append([])
    for c in line[0:-1]:
        map[y].append(int(c))
    y += 1

part1 = countVisibleTree(map)
part2 = getBestSpotTreeScore(map)

print("Part 1 : " + str(part1))
print("Part 2 : " + str(part2))

f.close()