
# 음료수 얼려 먹기

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False
    
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result) 



# import sys
# sys.setrecursionlimit(10**7)
#
# def dfs(graph, v):
# 	v = '1'
# 	global count
# 	for i in graph:
# 		for j in range(m-1):
# 			if i[j] == '0':
# 				dfs(graph, i[j])
# 			else:
# 				count += 1
#
# n, m = map(int, input().split())
# graph = []
# count = 0
# for i in range(n):
# 	num = input()
# 	graph.append(list(num))
#
# dfs(graph, graph[0][0])
# print(count)
