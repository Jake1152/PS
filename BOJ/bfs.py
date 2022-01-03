# bfs 


 
def dfs():
	pass

def bfs():
	
	
	pass



# global distance, predecessor
# node count, command cnt, vertex number
N, M, V = map(int, input().split())
visited = [False for _ in range(N)]
node = [ [] for _ in range(N)]

	# distance = [ -1 for _ in range(N)]
	# predecessor = [ None for _ in range(N)]

def linked_node(from_node, to_node):
	node[from_node].append(to_node)

# __main__()


