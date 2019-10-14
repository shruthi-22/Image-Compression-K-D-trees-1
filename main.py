from PIL import Image
import csv
from Tree import KD
import time 


t = KD()  # black
# points = []
# with open('css16.txt', 'r')as f:
#     data = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         row = [int(x) for x in row]
#         points.append(row)
# for i in range(len(points)):
#     t.root = t.insert(t.root, points[i])
    # print(i)
    
    
    # t.LevelOrder(t.root)

    # inp=1
    # while(inp):
    #     m=[int(x) for x in input().split(',')]
    #     m=tuple(m)
    #     print(t.nearestNeighbour(t.root, m[0],m[1],m[2], 0, 1000000))

    # file=open('Output1.txt','w')

    # im = Image.open('index.jpeg')
    # pix = im.load()
    # for x in range(im.size[0]):
    #     for y in range(im.size[1]):
    #         m = pix[x, y]
    #         # file.write(str(m)+' ')
    #         n = t.nearestNeighbour(t.root, m[0],m[1],m[2], 0, 1000000)
    #         pix[x, y] = tuple(n[0])
            # file.write(str(pix[x,y])+'\n')
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

    # im.save('iterative16.png')
