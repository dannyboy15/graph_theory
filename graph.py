class Vertex():
	current_label = 0 + ord('a') - 1

	def __init__(self, graph, x, y, label=None):
		# super(Vertex, self).__init__()
		# if not isinstance(graph, Graph):
		# 	return None
		self.graph = graph
		self.x = x
		self.y = y
		self.incd_edges = {}
		self.adj_vertices = {}
		self.degree = 0
		if label is None:
			self.label = self.auto_gen_label()
		else:
			self.label = label
		self.graph.add_vertex(-1, -1, vert=self)

	def __str__(self):
		return "Vertex: '{}' at ({}, {}) in Graph '{}'".format(self.label, self.x, self.y, self.graph.name)

	def auto_gen_label(self, method="vtx"):
		if method == "abc":
			Vertex.current_label += 1
			return chr(Vertex.current_label)
		elif method == "vtx":	
			Vertex.current_label += 1
			return "v" + str(Vertex.current_label - 96)

	def connect_to_vertex(self, vert, edge):
		self.adj_vertices[vert.label] = vert
		self.incd_edges[edge.label] = edge
		self.degree += 1

	def has_edge_with(self, vert):
		pass


class Edge():
	current_label = 0

	def __init__(self, graph, vert_1, vert_2, label=None, weight=0):
		# super(Edge, self).__init__()
		self.graph = graph
		self.vert_1 = vert_1
		self.vert_2 = vert_2
		self.verts = (vert_1, vert_2);
		if label is None:
			self.label = self.auto_gen_label()
		else:
			self.label = label
		self.weight = weight
		vert_1.connect_to_vertex(vert_2, self)
		vert_2.connect_to_vertex(vert_1, self)

	def __str__(self):
		return "Edge  : '{}' with vertices ({}, {}) in Graph '{}'".format(self.label, self.vert_1.label, self.vert_2.label, self.graph.name)

	def auto_gen_label(self, method="edg"):
		if method == "123":
			Edge.current_label += 1
			return str(Edge.current_label)
		if method == "edg":	
			Edge.current_label += 1
			return "e" + str(Edge.current_label)

	def are_verts(self, vert_1, vert_2):
		pass

	def has_loop(self):
		pass


class Graph():
	graph_count = 0
	def __init__(self, verts=None, edges=None, name=None):
		# super(Graph, self).__init__()
		if verts is None:
			self.verts = {}
		else:
			self.verts = verts
		if edges is None:
			self.edges = {}
		else:
			self.edges = edges
		if name is None:
			self.name = "Graph" + str(Graph.graph_count)
			Graph.graph_count += 1
		else:
			self.name = name

	def __str__(self):
		s =  "Graph     : " + self.name + "\n"
		s += "Vertex set: " + str([v for v in self.verts]) + "\n"
		s += "Edges set : " + str([e for e in self.edges])
		return s 

	def add_vertex(self, x, y, label=None, vert=None):
		# TODO: Handle adding vert versus creating vert
		if vert is not None:
			print "Not none"
			print vert
			print vert.label
			self.verts[vert.label] = vert
			return vert
		print "me first"
		v = Vertex(self, x, y, label)
		print "********* Do I ever get printed????"
		self.verts[v.label] = v
		return v
	
	def add_edge(self, vert_1, vert_2, label=None):
		e = Edge(self, vert_1, vert_2, label)
		self.edges[e.label] = e
		return e

	def get_vertex(self, label):
		return self.verts[label]
	
	def get_edge(self, label):
		return self.edges[label]

	def num_loops(self):
		pass

	def is_path(self, path):
		pass
	
	def is_simple_cycle(self, path):
		pass

	def is_cycle(self, path):
		pass

	def print_adj_mtx():
		pass

	def print_incd_mtx():
		pass

	def find_shortest_path(start_vert, end_vert):
		pass
		
	def is_Hamiltonian_cycle():
		pass

	def is_Euler_cycle():
		pass

	def is_barpartite():
		pass
