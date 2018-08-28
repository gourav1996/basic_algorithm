"""该算法的思路：选取覆盖最多的一个，然后重复这一步，哪怕有重复也没关系"""

# 需要被覆盖的州的集合
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# 每个广播站可以覆盖州
stations = {}
stations["kone"] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfout'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# 最终选定的广播站的集合
final_stations = set()

# 当所有的州都被覆盖，停止循环,循环选区最好的站
while states_needed:
    best_station = None # 创建记录广播站站的变量，
    states_covered = set()
    
    # 循环选取覆盖未覆盖最多州的广播站
    for station, states in stations.items():
        covered = states & states_needed
        if len(covered) > len(states_covered): # 如果覆盖的州多于
            states_covered = covered
            best_station = station
    
    states_needed -= states_covered # 如果覆盖了该州，则从需求集合中减去
    final_stations.add(best_station)

print(final_stations)