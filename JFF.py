from math import sqrt
def distance (x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    d = sqrt(dx**2 + dy**2)
    return d
def areatriangle(x1,y1,x2,y2,x3,y3):
    side1 = distance(x1,y1,x2,y2)
    side2 = distance(x2,y2,x3,y3)
    side3 = distance(x3,y3,x1,y1)
    p = (side1 + side2 + side3)/2
    t1 = p-side1
    t2 = p-side2
    t3 = p-side3
    if t1==0 or t2==0 or t3==0:
        print('Does not form a triangle')
    area = sqrt(p*(p-side1)*(p-side2)*(p-side3))
    return(area)
ans = areatriangle(0,0, 0,2, 2,0)
print(ans)