class node:
    def __init__(self, name):
        self._name = name
        self._friends = []
        self._status = 0
        self._discoveredby = 0
    def getName(self):
        return self._name
    def getFriends(self):
        return self._friends
    def addFriend(self, friend_index):
        self._friends.append(friend_index)
    def isUnseen(self):
        if self._status == 0:
            return True
        else:
            return False
    def isSeen(self):
        if self._status == 1:
            return True
        else:
            return False
    def setUnseen(self):
        self._status = 0
    def setSeen(self):
        self._status = 1
    def discover(self, n):
        self._discoveredby = n
    def discovered(self):
        return self._discoveredby

def makefriends(name1, name2):
    for i in range(len(people)):
        if people[i].getName() == name1:
            n1 = i
        if people[i].getName() == name2:
            n2 = i
    people[n1].addFriend(n2)
    people[n2].addFriend(n1)
class queue:
    def __init__(self):
        self._queue = []
    def enqueue(self, x):
        self._queue.append(x)
    def dequeue(self):
        return self._queue.pop(0)
    def isEmpty(self):
        return len(self._queue) == 0


def retrievePath(nodelist, start, goal):
    #Return the path from start to goal
    if start == goal:
        path = []
        path.append(start)
        return path
    else:
        previous = nodelist[goal].discovered()
        previous_path = retrievePath(nodelist, start, previous)
        previous_path.append(goal)
        return previous_path

def BFS(nodelist, start, goal):
    to_visit = queue()
    nodelist[start].setSeen()
    to_visit.enqueue(start)
    found = False
    while (not found) and (not to_visit.isEmpty()):
        current = to_visit.dequeue()
        neighbors = nodelist[current].getFriends()
        for neighbor in neighbors:
            if nodelist[neighbor].isUnseen():
                nodelist[neighbor].setSeen()
                nodelist[neighbor].discover(current)
                if neighbor == goal:
                    found = True
                else:
                    to_visit.enqueue(neighbor)
    return retrievePath(nodelist, start, goal)

nodes = []
a = node('E')
nodes.append(a)
a = node('H')
nodes.append(a)
a = node('A')
nodes.append(a)
a = node('B')
nodes.append(a)
a = node('C')
nodes.append(a)
a = node('D')
nodes.append(a)
a = node('F')
nodes.append(a)
a = node('G')
nodes.append(a)
a = node('I')
nodes.append(a)
a = node('J')
nodes.append(a)
a = node('K')
nodes.append(a)
a = node('L')
nodes.append(a)
a = node('M')
nodes.append(a)
people = nodes
makefriends('M', 'A')
makefriends('M', 'B')
makefriends('A', 'K')
makefriends('D', 'K')
makefriends('L', 'K')
makefriends('J', 'L')
makefriends('J', 'G')
makefriends('G', 'F')
makefriends('G', 'I')
makefriends('F', 'B')
makefriends('B', 'C')
makefriends('C', 'I')
makefriends('I', 'E')
makefriends('E', 'C')
makefriends('E', 'H')
makefriends('H', 'K')
makefriends('K', 'I')
pathlist = BFS(people, 0, 7)
for index in pathlist:
    print(people[index].getName())