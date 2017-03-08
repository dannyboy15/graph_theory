class Vertex():
	auto_label = 96 # ord('a') - 1

	def __init__(self, graph, x, y, label=None):
		# TODO: Error checking in case the right
		#		arguement isn't passed in

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
			Vertex.auto_label += 1
			return chr(Vertex.auto_label)
		elif method == "vtx":	
			Vertex.auto_label += 1
			return "v" + str(Vertex.auto_label - 96)

	def connect_to_vertex(self, vert, edge):
		self.adj_vertices[vert.label] = vert
		self.incd_edges[edge.label] = edge
		self.degree += 1

	def has_edge_with(self, vert):
		pass

	def is_adjacent_to(self, vert):
		return vert in self.adj_vertices

	def is_incident_on(self, edge):
		return edge in self.incd_edges

	def is_isolated(self):
		return self.incd_edges == {}


class Edge():
	auto_label = 0

	def __init__(self, graph, vert_1, vert_2, dir=False, label=None, weight=0):
		self.graph = graph
		self.vert_1 = vert_1
		self.vert_2 = vert_2
		self.verts = (vert_1, vert_2)
		self.dir = dir
		if label is None:
			self.label = self.auto_gen_label()
		else:
			self.label = label
		self.weight = weight
		vert_1.connect_to_vertex(vert_2, self)
		vert_2.connect_to_vertex(vert_1, self)
		self.graph.add_edge(-1,-1,edge=self)

	def __str__(self):
		return "Edge  : '{}' with vertices ({}, {}) in Graph '{}'".format(self.label, self.vert_1.label, self.vert_2.label, self.graph.name)

	def auto_gen_label(self, method="edg"):
		if method == "123":
			Edge.auto_label += 1
			return str(Edge.auto_label)
		if method == "edg":	
			Edge.auto_label += 1
			return "e" + str(Edge.auto_label)

	def has_verts(self, vert_1, vert_2):
		pass

	def has_loop(self):
		pass

	def has_parallel(self):
		pass


class Graph():
	graph_count = 0
	
	def __init__(self, verts=None, edges=None, name=None):
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
		s =  "Graph     : " + self.name + " with\n"
		s += "Vertex set: " + str([v for v in self.verts]) + " and \n"
		s += "Edges set : " + str([e for e in self.edges])
		return s 

	def add_vertex(self, x, y, label=None, vert=None):
		# TODO: Handle adding vert versus creating vert
		if vert is not None:
			self.verts[vert.label] = vert
			print vert.label
			return vert
		return Vertex(self, x, y, label)
	
	def add_edge(self, vert_1, vert_2, label=None, edge=None):
		if edge is not None:
			self.edges[edge.label] = edge
			print edge.label
			return edge
		return Edge(self, vert_1, vert_2, label=label)

	def get_vertex(self, label):
		return self.verts[label]
	
	def get_edge(self, label):
		return self.edges[label]

	def num_loops(self):
		pass

	def is_directed(self):
		for k, e in self.edges.items():
			print e.dir
			if e.dir:
				return True
		return False

	def has_parallel():
		pass

	# A simple graph is a graph with no loops or parallel edges
	def is_simple(self):
		return not has_parallel and num_loops == 0
	
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
