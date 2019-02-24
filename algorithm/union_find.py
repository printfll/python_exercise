class UF():
    def __init__(self, arr):
        self.arr=[]
        for i, n in enumerate(arr):
            if n==1:
                self.arr.append(i)
            else:
                self.arr.append(-1)   
    
    def find(self,i):
        if i!=self.arr[i]:
            self.arr[i]=self.find(self.arr[i])
        return self.arr[i]
    
    def union(self, i, j):
        i_id, j_id = self.find(i), self.find(j)
        print(f"union {i} and {j}, {self.arr}")
        if i_id!=j_id:
            self.arr[j]=i_id
    
    def count_connect(self):
        cnt = 0
        for i, n in enumerate(self.arr):
            if i==n:
                cnt+=1
        return cnt
        
islands =[0,0,1,1,0,0,1,0,0,1,1,1]
dire = [1,-1]
uf = UF(islands)
for i, n in enumerate(islands):
    if n==1:
        for x in dire:
            new_x =i+x
            if 0<=new_x<len(islands) and islands[new_x]:
                uf.union(new_x, i)
print(uf.arr)
print(f"the number of island is {uf.count_connect()}")

