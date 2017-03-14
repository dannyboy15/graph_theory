from graph import *

def test_1():
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
	# e5 = G.add_edge(v3, v3, dirn=True, label="e5")

	# G.has_parallel_edges()
	print G

	# Expected answer: True
	print "\nIs graph G a digraph?"
	print G.is_directed()

	# Expected answer: False
	print "\nIs graph G a simple graph?"
	print G.is_simple_graph()

	# Expected answer: True
	print "\nIs v1 adjacent to v2?"
	print v1.is_adjacent_to(v2)

	# Expected answer: False
	print "\nIs v1 adjacent to v3?"
	print v1.is_adjacent_to(v3)

	# Expected answer: True and True
	# 	Second function tests them together
	# 	Expected answer: True
	print "\nIs e1 incident on v1 and v2?"
	print str( e1.is_incident_on(v1) ) + " and " + str( e1.is_incident_on(v2) )
	# print e1.is_incident_on(v1, v2)

	# Expected answer: False
	print "\nIs e1 incident on v2 and v3?"
	print e1.is_incident_on(v2, v3)

	# Expected answer: True and True
	print "\nIs v1 incident on e1 and e2?"
	print str( v1.is_incident_on(e1) ) + " and " + str( v1.is_incident_on(e2) )

	# Expected answer: False
	print "\nIs v1 incident on e3?"
	print v1.is_incident_on(e3)

	# Expected answer: True
	print "\nIs v4 isolated?"
	print v4.is_isolated()

	# Expected answer: False
	print "\nIs v1 isolated?"
	print v1.is_isolated()

	# Expected answer: True
	print "\nIs e4 a loop?"
	print e4.is_loop()

	# Expected answer: False
	print "\nIs e3 a loop?"
	print e3.is_loop()

	# Expected answer: True
	print "\nAre e1 and e2 parallel edges?"
	print e1.is_parallel_to(e2)

	# Expected answer: False
	print "\nAre e1 and e3 parallel edges?"
	print e1.is_parallel_to(e3)

def test_2():
	G = Graph(name="G")
	v1 = G.add_vertex(1,1,label="v1")
	v2 = G.add_vertex(1,2,label="v2")
	v3 = G.add_vertex(2,2,label="v3")
	v4 = G.add_vertex(2,1,label="v4")
	e1 = G.add_edge(v1, v2, dirn=True, label="e1")
	e2 = G.add_edge(v2, v1, dirn=True, label="e2")
	e3 = G.add_edge(v2, v3, dirn=True, label="e3")
	e4 = G.add_edge(v3, v3, dirn=True, label="e4")
	e5 = G.add_edge(v3, v3, dirn=True, label="e5")

	# Expected answer: True
	print "Is (v1, v2, v3) a path in G"
	print G.is_path((v1, v2, v3))

	# Expected answer: False
	print "\nIs (v1, v2, v3, v4) a path in G"
	print G.is_path((v1, v2, v3, v4))

	# Expected answer: True
	print "\nIs (v1, v2, v3, v2, v1) a path in G"
	print G.is_path((v1, v2, v3, v2, v1))

def test_3():
	G = Graph(name="G")
	v1 = G.add_vertex(1,1,label="v1")
	v2 = G.add_vertex(3,1,label="v2")
	v3 = G.add_vertex(2,2,label="v3")
	v4 = G.add_vertex(1,3,label="v4")
	v5 = G.add_vertex(3,3,label="v5")
	e1 = G.add_edge(v1, v4, dirn=True, label="e1")
	e2 = G.add_edge(v1, v3, dirn=True, label="e2")
	e3 = G.add_edge(v3, v2, dirn=True, label="e3")
	e4 = G.add_edge(v2, v4, dirn=True, label="e4")
	e5 = G.add_edge(v4, v5, dirn=True, label="e5")

	F = Graph(name="G")
	v1 = F.add_vertex(1,2,label="v1")
	v2 = F.add_vertex(2,1,label="v2")
	v3 = F.add_vertex(3,2,label="v3")
	v4 = F.add_vertex(4,1,label="v4")
	e1 = F.add_edge(v1, v2, dirn=True, label="e1")
	e2 = F.add_edge(v2, v2, dirn=True, label="e2")
	e3 = F.add_edge(v2, v3, dirn=True, label="e3")

	K_2_3 = Graph(name="G")
	v1 = K_2_3.add_vertex(2,1,label="v1")
	v2 = K_2_3.add_vertex(1,2,label="v2")
	v3 = K_2_3.add_vertex(2,3,label="v3")
	v4 = K_2_3.add_vertex(1,4,label="v4")
	v5 = K_2_3.add_vertex(2,5,label="v5")
	e1 = K_2_3.add_edge(v2, v1, dirn=True, label="e1")
	e2 = K_2_3.add_edge(v2, v3, dirn=True, label="e2")
	e3 = K_2_3.add_edge(v2, v5, dirn=True, label="e3")
	e4 = K_2_3.add_edge(v4, v1, dirn=True, label="e4")
	e5 = K_2_3.add_edge(v4, v3, dirn=True, label="e5")
	e6 = K_2_3.add_edge(v4, v5, dirn=True, label="e6")

	print "Bipartite Test:"

	# Expected answer: True
	print "\nIs graph G bipartite?"
	print G.is_bipartite()

	# Expected answer: False
	print "\nIs graph F bipartite?"
	print F.is_bipartite()

	# Expected answer: True
	print "\nIs graph K_2_3 bipartite?"
	print K_2_3.is_bipartite()

def test_x():
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
	e_2 = g.add_edge(Vertex(g,9,9),Vertex(g,-9,-9))
	# print g.verts
	print v3
	print e_2
	g.is_directed()
	print v2
	print e1

	print v_1
	print e_1

	print "\nPrinting Graph:"
	print g
	print g.verts
	for v in g.verts:
		print g.verts[v].graph
	for v, v1 in g.verts.items():
		print v1.graph


def main():

	# test_1()
	# test_2()	# Path test
	test_3()	# Bipartite Test
	# test_x()


if __name__ == '__main__':
	main()
