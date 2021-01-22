graph ={
    1 : [2,3,4],
    2 : [5],
    3 : [5,7],
    4 : [],
    5 : [6,7],
    6 : [],
    7 : []
}

def dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = dfs(w,discovered)
    return discovered

print(dfs(1))