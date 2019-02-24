import sys
def shortpath(s, tar, g, nodes):
    graph = []
    for _ in range(nodes):
        graph.append([sys.maxsize]*nodes)
    for e in g:
        graph[e[0]][e[1]]=e[2]
    graph[s][s]=0
    if s >=nodes or tar>=nodes:
        return -1
    visited=set()
    visited.add(s)
    while True:
        min_edge, min_node=sys.maxsize,-1
        for n in visited:
            for t in range(nodes):
                if t not in visited and graph[n][t]<min_edge:
                    min_node=t
                    min_edge=graph[n][t]
        if min_edge==sys.maxsize:
            break
        for i in range(nodes):
            if graph[min_node][i]<sys.maxsize:
                graph[s][i] = min(graph[s][i], graph[s][min_node]+graph[min_node][i])
                print(f"graph[{s}][{i}] is {graph[s][i]}")
        visited.add(min_node)
    print(tar)
    return graph[s][tar]
        
graph = [[0,1,5],[0,2,7],[0,3,10],[1,4,4],[2,3,3],[3,4,3],[4,5,2]]
source, target = 0,3
print(f"shortest path between {source} to {target} is:{shortpath(source, target, graph,6)}")