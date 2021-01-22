graph ={
    1 : [2,3,4],
    2 : [5],
    3 : [5,7],
    4 : [],
    5 : [6,7],
    6 : [],
    7 : []
}

def iterativ_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered