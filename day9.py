import re
from math import ceil, floor

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

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __hash__(self):
        return 0

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

class Rope:
    def __init__(self, tail_size = 1, x = 0, y = 0):
        self.start = Pos(x,y)
        self.head = Pos(x,y)
        self.tail = [Pos(x,y) for i in range(0, tail_size) ]
        self.visited = { Pos(x,y) } # Set to kepp only unique
        
    def move(self, dir, step):
        #print("ASK FOR : {} {}".format(dir, step))
        mx = 0
        my = 0
        
        if dir == 'U': my = 1
        elif dir == 'D': my = -1
        elif dir == 'L': mx = -1
        elif dir == 'R': mx = 1
        else:
            print("UNKNOW direction : " + dir)
            return
        
        for i in range(0, step):
            #print("Head move from ({}:{}) to ({}:{})".format(self.head.x, self.head.y, self.head.x + mx, self.head.y + my))
            self.head.x += mx
            self.head.y += my
            
            self.strafe(self.head, self.tail[0], 0)
                
            #print(self)
            
    def strafe(self, p1, p2, p2_i):
       
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        
        tmx, tmy = 0, 0
        
        if dx * dx + dy * dy > 2:
            #print("> Tail move {}:{} with dx={} dy={}".format(ceil(dx/2), ceil(dy/2), dx, dy))
            if dx != 0: tmx += ceil(dx/2) if dx >= 0 else floor(dx/2)
            if dy != 0: tmy += ceil(dy/2) if dy >= 0 else floor(dy/2)
            
            p2.x += tmx
            p2.y += tmy
            #print("> Tail[{}] move to ({}:{})".format(p2_i, p2.x, p2.y))
            if p2_i == len(self.tail) -1:
                self.visited.add(Pos(p2.x, p2.y))
            else:
                self.strafe(p2, self.tail[p2_i + 1], p2_i + 1)
    
    def __str__(self):
        out = ""
        
        maxx = self.head.x if self.head.x > self.tail.x else self.tail.x
        maxy = self.head.y if self.head.y > self.tail.y else self.tail.y
        
        for i in range(0, maxy+1):
            for x in range(0, maxx+1):
                y = maxy - i
                if y == self.head.y and x == self.head.x: out += 'H'
                elif y == self.tail.y and x == self.tail.x: out += 'T'
                else: out += '.'
            out += '\n'
        
        return out


r1 = Rope(1)
r2 = Rope(9)

for line in lines:
    groups = re.search(r"([UDLR]) (\d*)", line)
    #print("{} {}".format(groups[1], groups[2]))
    r1.move(groups[1], int(groups[2]))
    r2.move(groups[1], int(groups[2]))
    

print("Part 1 : " + str(len(r1.visited)))
print("Part 2 : " + str(len(r2.visited)))

f.close()