arr = [10,-1,5,7,47,30,0,15,21,9,25]
dic = {}
res = []
target = 30
for i, n in enumerate(arr):
    if target - n in dic:
        res.append([dic[target-n],i])
    else:
        dic[n]=i
print(res)
# [[5, 6], [8, 9], [2, 10]]