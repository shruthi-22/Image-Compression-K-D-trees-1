import math 

import queue

def k():
    return 3

import random

def quickselect_median(l,d, pivot_fn=random.choice):
    return quickselect(l,d, len(l) // 2, pivot_fn)

def quickselect(l,d, k, pivot_fn):
    if len(l) == 1:
        assert k == 0
        return l[0]
    col= [el[d] for el in l]
    pivot = pivot_fn(col)
    lows = [el for el in l if el[d] < pivot]
    highs = [el for el in l if el[d] > pivot]
    pivots = [el for el in l if el[d] == pivot]

    if k < len(lows):
        return quickselect(lows,d, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[k-len(lows)]
    else:
        return quickselect(highs,d, k - len(lows)-len(pivots) , pivot_fn)

class Node:    #Base Node
    
    def __init__(self,value):
        self.rgb_value=value    #For Storing the RGB value of Named CSS
        self.left=None
        self.right=None

class KD:

    def __init__(self):
        self.root=None
        
    

    def insert(self,root,color_data,depth):
        depth=depth%3
        root=Node(quickselect_median(color_data,depth))
        # print(root.rgb_value)
        left_list=[]
        right_list=[]
        for x in color_data:
            if(x[depth]<root.rgb_value[depth]):
                left_list.append(x)
            elif(x[depth]>=root.rgb_value[depth] and x!=root.rgb_value):
                right_list.append(x)
        # print("left_list",left_list)
        # print("right_list",right_list)
        if(len(left_list)!=0):
            root.left=self.insert(root.left,left_list,depth+1)
        if(len(right_list)!=0):
            root.right=self.insert(root.right,right_list,depth+1)
    
        return root
        
    def searchRec(self,root,value,depth): #Searching for an element in the partitioned Set
        
        if(root==None):
            return False
        
        if(self.arePoints_Same(root.rgb_value,value)):
                return True;
        
        cd =depth % k()
        
        if(value[cd] < root.rgb_value[cd]): 
            return self.searchRec(root.left,value,depth+1)
        else:
            return self.searchRec(root.right,value,depth+1)
    
    def Search(self,root,value):
        return self.searchRec(root,value,0)
    
    def arePoints_Same(self,p1,p2):
        for i in range(k()):
            if(p1[i] != p2[i]):
                return False
        return True
    
    def Inorder(self,root):
        if(root==None):
            return 0
        self.Inorder(root.left)
        print("(",root.rgb_value[0],root.rgb_value[1],root.rgb_value[2],")")
        self.Inorder(root.right)

    def LevelOrder(self,root):
        q=queue.Queue(maxsize=2000)
        q.put(root)
        while(q.empty()!=1):
            temp=q.get()
            print(temp.rgb_value)
            if(temp.left!=None):
                q.put(temp.left)
            if(temp.right!=None):
                q.put(temp.right)
    
    def distance(self,root1,root2):
        a=root1.rgb_value
        b=root2

        # print(a,b)
        dist=0
        for x in range(len(a)):
            dist+=(a[x]-b[x])**2
        
        return math.sqrt(abs(dist))
    
    currentBest=0
    nearestDistance=1000000000000000

    def nearestNeighbour(self,root,r,g,b,currentBest_,nearestDistance):
        color=(r,g,b)
        while(root!=None):
            root_distance=self.distance(root,color)
            if root.left!=None:
                left_distance=self.distance(root.left,color)
        
            else :
                left_distance=100000000000000000

            if root.right!=None:
                right_distance=self.distance(root.right,color)
        
            else:
                right_distance=100000000000000000

            if left_distance < right_distance:
                minChildDistance=left_distance
                currentBest=root.left
            else:
                minChildDistance=right_distance
                currentBest=root.right

            # print(root_distance,left_distance,right_distance)

            if root_distance>minChildDistance:
                if(nearestDistance>minChildDistance):   
                    currentBest_=currentBest
                    nearestDistance=minChildDistance
                root=currentBest
            else:
                if(nearestDistance>root_distance):   
                    currentBest_=root
                    nearestDistance=root_distance
                root=currentBest
        
        return tuple([currentBest_.rgb_value,nearestDistance])


    # def nearestNeighbour(self,root,r,g,b,currentBest_,nearestDistance):
    #     color=(r,g,b)
    #     if root==None:
    #         return tuple([currentBest_.rgb_value,nearestDistance])
        
    #     else:
    #         root_distance=self.distance(root,color)

    #     # if root.left==None and root.right==None:
    #     #     if(nearestDistance>root_distance):
    #     #         currentBest_=root
    #     #         nearestDistance=root_distance
    #     #     return tuple([currentBest_.rgb_value,nearestDistance])
        
    #     if root.left!=None:
    #         left_distance=self.distance(root.left,color)
        
    #     else :
    #         left_distance=100000000000000000

    #     if root.right!=None:
    #         right_distance=self.distance(root.right,color)
        
    #     else:
    #         right_distance=100000000000000000

    #     if left_distance < right_distance:
    #         minChildDistance=left_distance
    #         currentBest=root.left
    #     else:
    #         minChildDistance=right_distance
    #         currentBest=root.right

    #     # print(root_distance,left_distance,right_distance)

    #     if root_distance>minChildDistance:
    #         if(nearestDistance>minChildDistance):   
    #             currentBest_=currentBest
    #             nearestDistance=minChildDistance
    #         m=self.nearestNeighbour(currentBest,r,g,b,currentBest_,nearestDistance)
    #         currentBest_.rgb_value=m[0]
    #         nearestDistance=m[1]
    #     else:
    #         if(nearestDistance>root_distance):   
    #             currentBest_=root
    #             nearestDistance=root_distance
    #         m=self.nearestNeighbour(currentBest,r,g,b,currentBest_,nearestDistance)
    #         currentBest_.rgb_value=m[0]
    #         nearestDistance=m[1]
        
    #     return tuple([currentBest_.rgb_value,nearestDistance])

# t = KD()

# points= [ (9, 3 ,6),(7, 9 ,8),(1, 7 ,3),(3, 8 ,9),(6, 5 ,1),(8, 3 ,6) ]
# # print(quickselect_median(points,0))
# t.root=t.insert(t.root,points,0)

# # print(t.root.rgb_value)
#     # no_elts=6
    
#     # for i in range(no_elts):
#     #     t.root= t.insert(t.root,points[i])
        
# t.LevelOrder(t.root)

    # m=t.nearestNeighbour(t.root,(10,4,3),0,100000000)
    
    # print("Nearest of (10,4,3) is "+ str(m))

#     p1= (9,3,6) 
#     p2= (2,2,1) 
    
#     test=[p1,p2]
#     for i in test:
#         ans=t.Search(t.root,i)
#         if(ans==True):
#             print("FOUND")
#         else:
#             print("NOT FOUND")
