def find_lowest_cost_node(costs):
    """寻找花销最小的节点"""
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if lowest_cost > cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 定义起始节点，并更新到邻居节点的权重
graph = {}
# graph["start"] = {}
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2

# 定义子节点，更新其到邻居节点的权重
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph['fin'] = {}


# 定义花销节点，即从起始节点到该节点需要的花销
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = float('inf')

# 父节点储存列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 记录处理过的节点
processed = []

# 寻找到终点最小的开销节点    
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(costs)
print(parents)