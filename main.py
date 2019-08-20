import random

N = 1000000
pointcount = 5
goodcount = 0
for i in range(N):
    points = []
    gaplist = []
    for j in range(pointcount):
        points.append(random.uniform(0, 360))
    points.sort()
    for k in range(pointcount):
        gap = points[pointcount - 1 - k] - points[0 - k]
        if (gap < 0):
            gap = gap + 360
        gaplist.append(gap)
    mingap = min(gaplist)
    if (mingap < 180):
        goodcount = goodcount + 1
ratio = goodcount / N
print(ratio)
