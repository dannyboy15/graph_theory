from graph import *

def test_1():

	# From first example in class
	# G = (V, E)
	# V = {v1, v2, v3, v4}
	# E = {e1, e2, e3, e4}

	# Create graph, vertex set and edge set
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

	# Begin test
	num_fail = 0
	print "|========= Graph Basics Test Begin =========|"

	num_fail +=	run_test("Print graph G",\
						"     Graph: G(V, E) with\n" +
						"Vertex set: V = ['v1', 'v2', 'v3', 'v4']\n" +
						" Edges set: E = ['e4', 'e1', 'e3', 'e2']",\
						G.__str__)

	# # G.has_parallel_edges()
	# print G

	num_fail +=	run_test("Is graph G a digraph?",\
						True,\
						G.is_directed)

	# # Expected answer: True
	# print "\nIs graph G a digraph?"
	# print G.is_directed()

	num_fail +=	run_test("Is graph G a simple graph?",\
						False,\
						G.is_simple_graph)

	# # Expected answer: False
	# print "\nIs graph G a simple graph?"
	# print G.is_simple_graph()

	num_fail +=	run_test("Is v1 adjacent to v2?",\
						True,\
						v1.is_adjacent_to, v2)

	# # Expected answer: True
	# print "\nIs v1 adjacent to v2?"
	# print v1.is_adjacent_to(v2)

	num_fail +=	run_test("Is v1 adjacent to v3?",\
						False,\
						v1.is_adjacent_to, v3)

	# # Expected answer: False
	# print "\nIs v1 adjacent to v3?"
	# print v1.is_adjacent_to(v3)

	num_fail +=	run_test("Is e1 incident on v1 and v2?",\
						True,\
						e1.is_incident_on, v1, v2)

	# # Expected answer: True and True
	# # 	Second function tests them together
	# # 	Expected answer: True
	# print "\nIs e1 incident on v1 and v2?"
	# print str( e1.is_incident_on(v1) ) + " and " + str(e1.is_incident_on(v2))
	# # print e1.is_incident_on(v1, v2)

	num_fail +=	run_test("Is e1 incident on v2 and v3?",\
						False,\
						e1.is_incident_on, v2, v3)

	# # Expected answer: False
	# print "\nIs e1 incident on v2 and v3?"
	# print e1.is_incident_on(v2, v3)

	num_fail +=	run_test("Is v1 incident on e1 and e2?",\
						True,\
						v1.is_incident_on, e1, e2)

	# # Expected answer: True and True
	# print "\nIs v1 incident on e1 and e2?"
	# print str( v1.is_incident_on(e1) ) + " and " + str( v1.is_incident_on(e2) )

	num_fail +=	run_test("Is v1 incident on e3?",\
						False,\
						v1.is_incident_on, e3)

	# # Expected answer: False
	# print "\nIs v1 incident on e3?"
	# print v1.is_incident_on(e3)

	num_fail +=	run_test("Is v4 isolated?",\
						True,\
						v4.is_isolated)

	# # Expected answer: True
	# print "\nIs v4 isolated?"
	# print v4.is_isolated()

	num_fail +=	run_test("Is v1 isolated?",\
						False,\
						v1.is_isolated)

	# # Expected answer: False
	# print "\nIs v1 isolated?"
	# print v1.is_isolated()

	num_fail +=	run_test("Is e4 a loop?",\
						True,\
						e4.is_loop)

	# # Expected answer: True
	# print "\nIs e4 a loop?"
	# print e4.is_loop()

	num_fail +=	run_test("Is e3 a loop?",\
						False,\
						e3.is_loop)

	# # Expected answer: False
	# print "\nIs e3 a loop?"
	# print e3.is_loop()


	num_fail +=	run_test("Are e1 and e2 parallel edges?",\
						True,\
						e1.is_parallel_to, e2)

	# # Expected answer: True
	# print "\nAre e1 and e2 parallel edges?"
	# print e1.is_parallel_to(e2)

	num_fail +=	run_test("Are e1 and e3 parallel edges?",\
						False,\
						e1.is_parallel_to, e3)

	# # Expected answer: False
	# print "\nAre e1 and e3 parallel edges?"
	# print e1.is_parallel_to(e3)

	print "\n|========== Graph Basics Test End ==========|"
	print "\nTest finished with {} failures. {}".format(num_fail,\
			"Great job!" if num_fail == 0 else \
			"Sorry. Let's try again.")
	# End test

def test_2():

	# Create graph, vertex set and edge set
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

	# Begin test
	num_fail = 0
	print "|============= Path Test Begin =============|"

	num_fail +=	run_test("Is (v1, v2, v3) a path in G",\
						True,\
						G.is_path,(v1, v2, v3))

	# # Expected answer: True
	# print "\nIs (v1, v2, v3) a path in G"
	# print G.is_path((v1, v2, v3))

	num_fail +=	run_test("Is (v1, v2, v3, v4) a path in G",\
						False,\
						G.is_path,(v1, v2, v3, v4))

	# # Expected answer: False
	# print "\nIs (v1, v2, v3, v4) a path in G"
	# print G.is_path((v1, v2, v3, v4))

	num_fail +=	run_test("Is (v1, v2, v3, v2, v1) a path in G",\
						True,\
						G.is_path,(v1, v2, v3, v2, v1))

	# # Expected answer: True
	# print "\nIs (v1, v2, v3, v2, v1) a path in G"
	# print G.is_path((v1, v2, v3, v2, v1))

	print "\n|============== Path Test End ==============|"
	print "\nTest finished with {} failures. {}".format(num_fail,\
			"Great job!" if num_fail == 0 else \
			"Sorry. Let's try again.")
	# End test

def test_3():
	# Create graphs and their vertex sets and edge sets
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

	F = Graph(name="F")
	v1 = F.add_vertex(1,2,label="v1")
	v2 = F.add_vertex(2,1,label="v2")
	v3 = F.add_vertex(3,2,label="v3")
	v4 = F.add_vertex(4,1,label="v4")
	e1 = F.add_edge(v1, v2, dirn=True, label="e1")
	e2 = F.add_edge(v2, v2, dirn=True, label="e2")
	e3 = F.add_edge(v2, v3, dirn=True, label="e3")

	K_2_3 = Graph(name="K_2_3")
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

	H = Graph(name="H")
	v1 = H.add_vertex(1,1,label="v1")
	v2 = H.add_vertex(2,1,label="v2")
	v3 = H.add_vertex(3,2,label="v3")
	v4 = H.add_vertex(1,2,label="v4")
	v5 = H.add_vertex(2,2,label="v5")
	v6 = H.add_vertex(3,2,label="v6")
	v7 = H.add_vertex(4,1,label="v7")
	v8 = H.add_vertex(5,2,label="v8")
	v9 = H.add_vertex(3,3,label="v9")
	v10 = H.add_vertex(4,3,label="v10")
	e1 = H.add_edge(v1, v4, dirn=True, label="e1")
	e2 = H.add_edge(v4, v5, dirn=True, label="e2")
	e3 = H.add_edge(v5, v2, dirn=True, label="e3")
	e4 = H.add_edge(v5, v6, dirn=True, label="e4")
	e5 = H.add_edge(v6, v3, dirn=True, label="e5")
	e6 = H.add_edge(v6, v7, dirn=True, label="e6")
	e7 = H.add_edge(v6, v8, dirn=True, label="e7")
	e8 = H.add_edge(v6, v9, dirn=True, label="e8")
	e9 = H.add_edge(v6, v10, dirn=True, label="e9")

	# Begin test
	num_fail = 0
	print "|=========== Bipartite Test Begin ==========|"

	num_fail +=	run_test("Is graph G bipartite?",\
						([v4, v3], [v1, v2, v5]),\
						G.is_bipartite)

	# # Expected answer: ([v1, v2, v5], [v3, v4])
	# print "\nIs graph G bipartite?"
	# print G.is_bipartite()

	num_fail +=	run_test("Is graph F bipartite?",\
						None,\
						F.is_bipartite)

	# # Expected answer: None
	# print "\nIs graph F bipartite?"
	# print F.is_bipartite()

	num_fail +=	run_test("Is graph K_2_3 bipartite?",\
						([v1, v3, v5], [v2, v4]),\
						K_2_3.is_bipartite)

	# # Expected answer: ([v1, v3, v5], [v2, v4])
	# print "\nIs graph K_2_3 bipartite?"
	# print K_2_3.is_bipartite()

	num_fail +=	run_test("Is graph H bipartite?",\
						([v1, v3, v5, v7, v8, v10, v9], [v2, v4, v6]),\
						H.is_bipartite)

	# # Expected answer: ([v1, v3, v5, v7, v8, v10, v9], [v2, v4, v6])
	# print "\nIs graph H bipartite?"
	# print H.is_bipartite()

	print "\n|=========== Bipartite Test End ============|"
	print "\nTest finished with {} failures. {}".format(num_fail,\
			"Great job!" if num_fail == 0 else \
			"Sorry. Let's try again.")
	# End test
	
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

def run_test(prompt, expected, function, *arg):
	print "\n" + prompt
	print "Expected result: {}".format(expected)
	if len(arg) == 0:
		result = function()
	else:
		result = function(*arg)
	print "Actual   result: {}".format( result )
	# print my_cmp(result , expected)
	test = my_cmp(expected, result)
	print "Success!" if test else "Failure!"
	return 0 if test else 1

def my_cmp(exp, res):
	# IF arg is 'None'
	if res is None:
		return  exp is res

	if type(res) is bool:
		return exp is res

	# If arg is a tuple
	elif type(res) is tuple:
		if len(res) != len(exp):
			return False

		e = []
		r = []
		for i in range(len(exp)):
			e.append(sorted(exp[i]))
			r.append(sorted(res[i]))

		e = sorted(e)
		r = sorted(r)

		return e == r
		# print e
		# print r
		# print cmp(e, r)

		# e = sorted(exp)
		# r = sorted(res)

		# print e
		# print r

		# for i in range(len(e)):
		# 	if sorted(e[i]) != sorted(r[i]):
		# 		# print e
		# 		# print r

		# 		print sorted(e[i])
		# 		print sorted(r[i])

		# 		return False
		# return True

	elif type(res) is str:
		return exp == res

	else:
		print "No comparison test for " + str(type(res))

def main():
	# Might want to change to eval_1 later
	test_1()	# Graph basics
	test_2()	# Path test
	test_3()	# Bipartite Test
	# test_x()


if __name__ == '__main__':
	main()
