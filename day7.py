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


class Node():
    def __init__(self, name, size = 0, parent = None):
        self.children = []
        self.name = name
        self.size = size
        self.parent = parent
   
    def buildChild(self, name, size = 0):
        n = Node(name, size, self)
        self.children.append(n)
        if n.isLeaf():
            self.computeSize()
        return n
        
    def computeSize(self):
        if self.isLeaf() == False:
            self.size = sum(c.size for c in self.children)

        if self.parent:
            self.parent.computeSize()
    
    def getChildByName(self, name):
        for child in self.children:
            if child.name == name:
                return child
    
    def isLeaf(self):
        return len(self.children) == 0
        
    def __str__(self, deep = 0):
        out = ""
        
        for i in range(0, deep):
            out += "  "
        
        out += "-{} {} ({}, {}) {}\n".format(bcolors.OKGREEN if self.isLeaf() else bcolors.OKCYAN, self.name, "file" if self.isLeaf() else "dir", self.size, bcolors.ENDC)
        for child in self.children:
            out += child.__str__(deep + 1)
        return out


f = open("input.txt","r")
lines = f.readlines()

root = Node('/')
node = root

dir_list = [root]

for line in lines:
    match_root = re.search(r"\$ cd \/", line)
    match_ls = re.search(r"\$ ls", line)
    match_move = re.search(r"\$ cd (.*)", line)
    match_dir = re.search(r"dir (.*)", line)
    match_file = re.search(r"(\d*) (.*)", line)
    
    if match_root:
        node = root
        
    elif match_ls:
        pass#print(node)
        
    elif match_move:
        dest = match_move.group(1)
        node = node.getChildByName(dest) if dest != ".." else node.parent
        
    elif match_dir:
        dir_list.append(node.buildChild(match_dir.group(1)))
        
    elif match_file:
        node.buildChild(match_file.group(2), int(match_file.group(1)))

print(root)

dir_list_filtered = [d for d in dir_list if d.size <= 100000]

size_needed = 30000000
total_space = 70000000
used_space = root.size

print("SPACE {}/{}, needed for update {}".format(used_space, total_space, size_needed))

dir_list_to_del = [d for d in dir_list if total_space - used_space + d.size >= size_needed]

for d in dir_list_to_del:
    print("{} {}".format(d.name, d.size))
    
to_del = min(dir_list_to_del, key=lambda x : x.size)

print("Del {}<{}> ---> free space {}".format(to_del.name, to_del.size, total_space - used_space + to_del.size))

print("\nPart 1 : " + str(sum(n.size for n in dir_list_filtered)))
print("Part 2 : " + str(to_del.size))

f.close()