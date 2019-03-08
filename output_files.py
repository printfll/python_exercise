import collections 
def output_files(files): 
    cnt = collections.defaultdict(int) 
    readable_files = [] 
    for file_name, permission in files.items(): 
        arr = file_name.split("/")[:-1] 
        for i in range(len(arr)): 
            cnt["/".join(arr[:i+1])]+=1 
        if permission: 
            for i in range(len(arr)): 
                cnt["/".join(arr[:i+1])]-=1 
            readable_files.append(file_name) 
    result = set() 
    for file_name in readable_files: 
        find = False 
        arr = file_name.split("/")[:-1] 
        for i in range(len(arr)): 
            path = "/".join(arr[:i+1]) 
            if not cnt[path]: 
                find = True 
                result.add(path) 
                break 
        if not find: 
            result.add(file_name) 
    return result 
input = {"/etc/folder1/a":True, "/etc/folder1/b":False, "/tmp/folder1/a":True, "/tmp/folder1/b":True, "/tmp/folder2/c":True} 
print(output_files(input)) 