def dp(weights, values, target):
    arr = []
    for i in range(len(weights)+1):
        _t=[]
        for j in range(target+1):
            _t.append(0)
        arr.append(_t)
            
    for i in range(1,len(weights)+1):
        for j in range(1,target+1):
            if weights[i-1]<=j:
                arr[i][j]=max(arr[i-1][j], arr[i-1][j-weights[i-1]]+values[i-1])
    print(arr[-1][-1])

    
weights=[4,3,1,1]
values=[300,200,150,200]
dp(weights, values, 4)
