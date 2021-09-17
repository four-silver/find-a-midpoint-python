import sys

dfs = []
dist = {}
path = " "

def DFS(current_station, sum, s, cost, station_info):
    if not current_station in dist:
        dist[current_station] = sys.maxsize

    if dist[current_station] < sum:
        return
    else:
        dist[current_station] = sum

    if sum > cost:
        return

    for next_station in station_info[current_station]['time'].keys():
      if not next_station in dfs:
        dfs.append(next_station)
        DFS(next_station,sum + station_info[current_station]['time'][next_station],s+next_station,cost,station_info)
        dfs.remove(next_station)

def start(start, station_info):
    cost = sys.maxsize
    dist[start] = cost
    dfs.append(start)
    DFS(start, 0, " ", cost, station_info)
    return dist
