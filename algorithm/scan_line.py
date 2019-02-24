intervals = [[0,15], [3, 7], [2,10], [9,15], [16,17], [3,8]]
start_arr=[i[0] for i in intervals]
end_arr = [i[1] for i in intervals]
start_arr.sort()
end_arr.sort()
max_conflict, cnt, start, end = 0, 0, 0, 0
while start<len(start_arr):
    if start_arr[start]<=end_arr[end]:
        start+=1
        cnt+=1
        max_conflict = max(max_conflict, cnt)        
    else:
        cnt=0
        end+=1
print(max_conflict)
