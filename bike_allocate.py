import sys
def distance(user, bike):
    return abs(user[0]-bike[0])+abs(user[1]-bike[1])
    
def allocate(bike_pos, other_user_pos, my_pos):
    total_dis = []
    for u in other_user_pos:
        dis = []
        for j, b in enumerate(bike_pos):
            d = distance(u, b)
            dis.append([d, j])
        dis.sort(key=lambda x:x[0])
        total_dis.append(dis)
    
    used_bike = set()
    while total_dis:
        min_bike_id, min_dis, user_id = -1, sys.maxsize, -1
        for u, dis_list in enumerate(total_dis):
            while dis_list and dis_list[0][1] in used_bike:
                dis_list.pop(0)
            if dis_list and dis_list[0][0]<min_dis:
                min_dis = dis_list[0][0]
                min_bike_id = dis_list[0][1]
                user_id = u
        if min_bike_id>=0:
            total_dis.pop(user_id)
            used_bike.add(min_bike_id)
    
    if len(used_bike)<len(bike_pos):
        min_bike_id, min_dis = -1, sys.maxsize
        for j, b in enumerate(bike_pos):
            if j not in used_bike:
                d = distance(my_pos, b)
                if d<min_dis:
                    min_bike_id, min_dis = j, d
        return j
    return -1

    