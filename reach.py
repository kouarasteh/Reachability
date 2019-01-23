from collections import deque

#problem statement
#We have a robot starting at (x1,y1) that needs to reach (x2,y2), but can only move in one of two ways:
#-----1. robot can move from (x,y) to (x+y,y)
#-----2. robot can move from (x,y) to (x,y+x)

#unique properties of this problem
#-----1.continuous travel in x direction uses a constant step size(y) and vice versa
#-----2.if a point (xa,ya) can reach (x2,y2), and (x1,y1) can reach (xa,ya), then (x1,y1)'origin' can reach (x2,y2)'target'

#implementation notes
#-----1.this problem can be solved through dynamic programming if we set our grid space to be the 2d rectangular space between x1,y1 and x2,y2 and call all points in this grid space 'valid'
#-----2.We will push all valid points in the row y2 and the column x2 that can reach target to a queue
#-----3.We will then add valid points that can reach each queue point, xq,yq to the queue, and stop once we reach origin or the queue is empty

#Data Structure Choice
#-----1.here i'm using collections.deque to implement a queue, as it has O(1) indexed access at both ends and O(1) pop&push from both ends
def canReach(x1,y1,x2,y2):
    q = deque()
    q.appendleft((x2,y2))
    while len(q) != 0:
        #grab the coord point to evaluate
        curr = q.pop()
        #if we found our origin, return True
        if (curr[0] == x1 and curr[1] == y1):
            return True
        #if we passed to the left or below our origin, return False, we failed
        if (curr[0] < x1 or curr[1] < y1):
            return False

        #add all vertical neighbors of our current point to the queue
        y = curr[1] - curr[0]
        while (y >= y1):
            q.appendleft((curr[0],y))
            y -= curr[0]

        #add all horizontal neighbors of our current point to the queue
        x = curr[0] - curr[1]
        while (x >= x1):
            q.appendleft((x,curr[1]))
            x -= curr[1]
    #if our queue is empty, return False, we failed
    return False

print(canReach(2,3,7,5))
print(canReach(1,1,1,1))
print(canReach(2,4,2,8))

print(canReach(2,3,4,5))
print(canReach(100,1,1,1))
print(canReach(1,100,1,1))

#Complexity Notes
#-----This implementation utilizes backtracking to avoid evaluating all points in the grid and avoid the naive implementation of recursive subproblems. In the case of needing to reference the evaluated map again, we would implement a DP approach.
#-----In the case of unit travel length, the worst case runtime complexity would be O(n^2), where n is the displacement between (x1,y1) and (x2,y2)
 
