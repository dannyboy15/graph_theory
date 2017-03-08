from graph import *

def main():
	
# From first example in class
# G = (V, E)
# V = {v1, v2, v3, v4}
# E = {e1, e2, e3, e4}

	G = Graph(name="G")
	v1 = G.add_vertex(1,1,label="v1")
	v2 = G.add_vertex(1,2,label="v2")
	v3 = G.add_vertex(2,2,label="v3")
	v4 = G.add_vertex(2,1,label="v4")
	e1 = G.add_edge(v1, v2, dirn=True, label="e1")
	e2 = G.add_edge(v2, v1, dirn=True, label="e2")
	e3 = G.add_edge(v2, v3, dirn=True, label="e3")
	e4 = G.add_edge(v3, v3, dirn=True, label="e4")

	print G

	print "\nIs digraph?"
	print G.is_directed()

	print "\nIs v1 adjacent to v2?"
	print v1.is_adjacent_to(v2)


	# g = Graph()
	# # print g.name
	# v1 = Vertex(g,1,2)
	# v2 = Vertex(g,1,2)
	# # v3 = Vertex(g,1,2)
	# v3 = g.add_vertex(1,1)
	# # v2 = g.add_vertex(2,2)
	# e1 = g.add_edge(v1, v2)
	# v_1 = g.get_vertex("v1")
	# e_1 = g.get_edge("e1")
	# e_2 = g.add_edge(Vertex(g,9,9),Vertex(g,-9,-9))
	# # print g.verts
	# print v3
	# print e_2
	# g.is_directed()
	# print v2
	# print e1

	# print v_1
	# print e_1

	# print "\nPrinting Graph:"
	# print g
	# print g.verts
	# for v in g.verts:
	# 	print g.verts[v].graph
	# for v, v1 in g.verts.items():
	# 	print v1.graph

if __name__ == '__main__':
	main()