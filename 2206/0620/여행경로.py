from collections import defaultdict
def solution(tickets):
    answer = []
    n = len(tickets)
    def init_graph() :
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
            
        return routes
    
    def dfs(key, footprint) :
        if len(footprint) == n+1 :
            return footprint
        for idx, country in enumerate(routes[key]) :
            routes[key].pop(idx)
            fp = footprint[:]
            fp.append(country) 
            
            ret = dfs(country,fp) 
            
            if ret : 
                return ret
            print(country)
            routes[key].insert(idx,country)
            
            
    routes = init_graph()
    for r in routes:
        routes[r].sort()
        
    answer = dfs("ICN",["ICN"])
            
        
    return answer
