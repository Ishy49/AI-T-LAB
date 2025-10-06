graph = {
 'A':['B','C'], 'B':['A','C','D'],
 'C':['A','B','D'], 'D':['B','C']
}
colors = ['R','G','B']
assign = {}

def safe(node, color):
    for n in graph[node]:
        if assign.get(n)==color: return False
    return True

def backtrack(nodes):
    if not nodes: return True
    node = nodes[0]
    for c in colors:
        if safe(node,c):
            assign[node]=c
            if backtrack(nodes[1:]): return True
            assign.pop(node)
    return False

backtrack(list(graph.keys()))
print(assign)
