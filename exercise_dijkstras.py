def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if lowest_cost > cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 定义各个节点到邻居节点
graph = {}
graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2
graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7 
graph['c'] = {}
graph['c']['d'] = 6
graph['c']['fin'] =3
graph['d'] = {}
graph['d']['fin'] = 1
graph['fin'] = {}

# 定义从起始开始到各个节点的花销
infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['fin'] = infinity

# 父节点记录
parents = {}
parents['a'] = "staring"
parents['b'] = "staring"
parents['c'] = None
parents['d'] = None
parents['fin'] = None

# 记录已经处理过的节点
processed = []

# 寻找最低消费方法
node = find_lowest_cost_node(costs)
# 找到到当前节点的最低消费路径后，遍历该节点的邻居节点，寻找最低消费节点
while node is not None:
    cost = costs[node] # 记录当前位置的消费
    neighbers = graph[node] 
    for n in neighbers.keys():
        newcost = cost + neighbers[n]
        if newcost < costs[n]:
            costs[n] = newcost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print("The lowest cost is %d \n" %costs['fin'] )

# 消费方式
parent = parents['fin']
print("fin <- ", end='')
while parent in parents.keys():
    print(parent + '<- ', end='')
    parent = parents[parent]

print('starting')