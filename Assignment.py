from collections import defaultdict
  
n,h,x = input().split()
#c is list of cities that are infected
c=list(input().split())

#defining and creating a graph with input data
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
  
for i in range(int(n)-1):
    e1,e2=input().split()
    addEdge(graph,e1,e2)
    addEdge(graph,e2,e1)

#Shortest path between two cities
def find_shortest_path(graph, start, end, path =[]):
		path = path + [start]
		if start == end:
			return path
		shortest = None
		for node in graph[start]:
			if node not in path:
				newpath = find_shortest_path(graph, node, end, path)
				if newpath:
					if not shortest or len(newpath) < len(shortest):
						shortest = newpath
		return shortest
		
#list of all cities
list=graph.keys()
count=0
for j in list :
    l=0
    for i in range(len(c)):
        #finding maximum length of each city from each infected city
        l=max(l,len(find_shortest_path(graph,j,c[i])))
    #if l is greater than 3, the maximum of minimum length is 2 and hence the city can be the epicenter
    if(l<=3):
        count=count+1
print(count)

