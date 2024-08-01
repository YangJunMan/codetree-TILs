array=[[[0]*4]*4]

n=int(input())

x, y=0,0

arraydict={'E':[1,0],'S':[0,-1],'W':[-1,0],'N':[0,1]}

for i in range (n):
    a,b=list(input().split())
    for i in range (int(b)):
        y+=arraydict[a][1]
        x+=arraydict[a][0]

print(x,y)