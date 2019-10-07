import numpy as np
def k():
    return 3

class Node:
    def __init__(self,value):
        self.rgb_value=value
        self.left=None
        self.right=None
class KD:
    def __init__(self,value):
        self.root=Node(value)
   
    def insRec(self,root,value,depth):
        if(root==None):
            return Node(value)
        cd =depth % k()
        
        if(value[cd] < root.rgb_value[cd]):
            root.left=self.insRec(root.left,value,depth+1)
        else:
            root.right=self.insRec(root.right,value,depth+1)
        return root
    
    def insert(self,root,value):
        return self.insRec(root,value,0)
    
    def searchRec(self,root,value,depth):
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

    
  
if __name__ == "__main__":
   
    t = KD((5,1,1))

    points=np.array( [ (9, 3 ,6),(7, 9 ,8),(1, 7 ,3),(3, 8 ,9),(6, 5 ,1),(8, 3 ,6) ])
    
    no_elts=points.shape[0]
    
    for i in range(no_elts):
        t.root= t.insert(t.root,points[i])
        
    t.Inorder(t.root)
    
    p1=np.array( (9,3,6) )
    p2=np.array( (2,2,1) )
    
    test=[p1,p2]
    for i in test:
        ans=t.Search(t.root,i)
        if(ans==True):
            print("FOUND")
        else:
            print("NOT FOUND")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
