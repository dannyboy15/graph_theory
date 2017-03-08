from graph import *

def main():
	g = Graph()
	# print g.name
	v1 = Vertex(g,1,2)
	v2 = Vertex(g,1,2)
	# v3 = Vertex(g,1,2)
	v3 = g.add_vertex(1,1)
	# v2 = g.add_vertex(2,2)
	e1 = g.add_edge(v1, v2)
	v_1 = g.get_vertex("v1")
	e_1 = g.get_edge("e1")
	# print g.verts
	# print v1
	# print v2
	# print e1

	# print v_1
	# print e_1

	# print "\nPrinting Graph:"
	# print g
	# print g.verts
	for v in g.verts:
		print g.verts[v].graph
	for v, v1 in g.verts.items():
		print v1.graph

if __name__ == '__main__':
	main()