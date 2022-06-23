from collections import defaultdict
def solution(tickets):
    answer = []
    def init_graph() :
        routes = defaultdict(list)
        for k,v in tickets :
            routes[k].append(v)
        return routes
    
    def dfs(key,footprint) :
        if len(footprint) == (len(tickets)+1):
            return footprint
        for idx,country in enumerate(routes[key]) :
            routes[key].pop(idx)
            
            fp = footprint[:]
            fp.append(country)
            
            ret = dfs(country,fp)
            
            if ret :
                return ret
            routes[key].insert(idx,country)
    
    routes = init_graph()
    for r in routes :
        routes[r].sort()
        print(routes[r])
        
    answer = dfs("ICN",["ICN"])
            
        
    return answer
