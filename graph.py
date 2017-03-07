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

	def __str__(self):
		pass

	def auto_gen_label(self, method="vtx"):
		pass

	def connect_to_vertex(self, vert, edge):
		pass

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
		pass

	def auto_gen_label(self, method="edg"):
		pass

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

	def get_name(self):
		pass

	def add_vertex(self, x, y, label=None):
		pass
	
	def add_edge(self, vert_1, vert_2, label=None):
		pass

	def get_vertex(self, label):
		pass
	
	def get_edge(self, label):
		pass

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
