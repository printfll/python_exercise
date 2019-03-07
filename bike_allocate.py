import sys
def distance(user, bike):
    return abs(user[0]-bike[0])+abs(user[1]-bike[1])
    
def allocate(bike_pos, user_pos, my_pos):
    total_dis = {}
    for i, u in enumerate(user_pos):
        dis = []
        for j, b in enumerate(bike_pos):
            d = distance(u, b)
            dis.append([d, j])
        dis.sort(key=lambda x:x[0])
        total_dis[i] = dis
    
    my_dis = []
    for j, b in enumerate(bike_pos):
        d = distance(my_pos, b)
        my_dis.append([d, j])
    my_dis.sort(key=lambda x:x[0])
    
    used_bike = set()
    for dis in my_dis:
        bike_id, bike_dis = dis[1], dis[0]
        while total_dis:
            min_user, min_dis, min_bike = 0, sys.maxsize, 0
            for user, dis_row in total_dis.items():
                if dis_row[0][0]<min_dis:
                    min_user = user
                    min_dis = dis_row[0][0]
                    min_bike = dis_row[0][1]
            if min_bike == bike_id:
            used_bike.add(min_bike)
            total_dis.pop(min_user)
    return -1

bikes = [[0,0],[2,4],[3,3],[]]
    