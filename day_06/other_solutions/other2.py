#from aoc_tools import *
import sys
#import pyperclip
sys.setrecursionlimit(1000000)

with open("input") as f:
    s = f.read().strip()

def printc(x):
    #print_(x)
    #pyperclip.copy(x)
    print(x)
    
ans = res = 0

# grid input
g = [list(r) for r in s.split("\n")]
n,m = len(g),len(g[0])

ix,iy = 0,0
for x in range(n):
    for y in range(m):
        if g[x][y] in "><^v":
            #print(g[x][y])
            ix,iy = x,y

dirs = [(-1,0), (0,1), (1,0), (0,-1)]

cx, cy, cd = ix, iy, 0
seen = set()
while cx in range(n) and cy in range(m):
    seen.add((cx,cy))
    while True:
        cdir = dirs[cd]
        nx,ny = cx + cdir[0], cy + cdir[1]
        if nx in range(n) and ny in range(m) and g[nx][ny] == "#":
            cd = (cd + 1) % 4
        else:
            cx,cy = nx,ny
            break
print(len(seen))

#g2 = [[y for y in r] for r in g]

for ox in range(n):
    #print(ox)
    for oy in range(m):
        if g[ox][oy] == "#" or g[ox][oy] == "^":
            continue

        g[ox][oy] = "#"
        
        seen = set()
        cd = 0
        cx, cy = ix, iy
        while cx in range(n) and cy in range(m) and (cx,cy,cd) not in seen:
            seen.add((cx,cy,cd))
            while True:
                cdir = dirs[cd]
                nx,ny = cx + cdir[0], cy + cdir[1]
                if nx in range(n) and ny in range(m) and g[nx][ny] == "#":
                    cd = (cd + 1) % 4
                else:
                    cx,cy = nx,ny
                    break

        if (cx,cy,cd) in seen:
            ans += 1
            #g2[ox][oy] = "?"

        g[ox][oy] = "."

printc(ans)


#print("\n".join("".join(g2[i][j] for j in range(m)) for i in range(n)))