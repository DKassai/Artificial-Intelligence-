import binary_heap.binary_heap as heap 
import binary_heap.node as node

open_list=heap.Heap([start_node])
shortest_path = []
closed_list = []
''' hey its your AI talking, i know what you did, dont do it again '''
def A_search (start_node, end_node):
	if start_node=end_node:
		shortest_path.append(end_node)
		temp = end_node.parent
		while temp:
			shortest_path.append(temp)
			temp=temp.parent
		return 1
	for n in start_node.neighbors():
		open_list.add(n)
	closed_list.append(start_node)
	shortest_option = open_list.pop()
	while open_list.peek() in closed_list:
		open_list.pop()
	A_search(shortest_option,end_node)




























































	# beginning_node = open_list.pop()
	# if beginning_node=end_node:
	# 	return -1
	# 	''' this will return when the begnning is also the end'''
	# if len(beginning_node.neighbors) ==0:
	# 	return -1
	# for n in beginning_node.neighbors:
	# 	open_list.add(n)
	# while len(open_list.heap):
	# 	shortest_length = open_list.pop()


