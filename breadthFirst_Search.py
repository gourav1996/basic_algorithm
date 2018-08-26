from collections import deque

def person_is_seller(name):
    """判断是否为芒果经销商，以最后以为是否为字母'm'"""
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person] # 如果这个人不是芒果经销商，将他的邻居节点加入队列
                searched.append(person) # 将此人加入检查的队列，避免重复和循环
            
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["thom"] = []
graph["peggy"] = []
graph["jonny"] = []
search("you")