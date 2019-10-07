from PIL import Image
import csv
from Tree import KD
import time 

if __name__ == "__main__":
    t = KD([0, 0, 0])  # black
    points = []
    with open('css16.txt', 'r')as f:
        data = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            row = [int(x) for x in row]
            points.append(row)
    for i in range(len(points)):
        t.root = t.insert(t.root, points[i])


    im = Image.open('index.jpeg')
    pix = im.load()
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            m = pix[x, y]
            print(m,end=' ')
            n = t.nearestNeighbour(t.root, m[0],m[1],m[2], 0, 1000000)
            time.sleep(1)
            pix[x, y] = tuple(n[0])
            print(pix[x,y])
#     points=[]
#     with open('sample.txt', 'r')as f:
#         data = csv.reader(f)
#         for row in data:
#             row = [int(x) for x in row]
#             points.append(row)
# #     print(points)
#     for i in points:
#         n = t.nearestNeighbour(t.root, i[0],i[1],i[2], 0, 1000000)
#         print(i,n[0])

    im.save('changed2.png')
