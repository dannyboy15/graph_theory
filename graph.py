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

	# def __repr__(self):
	# 	return self.label # "Vertex: '{}' at ({}, {}) in Graph '{}'".format(self.label, self.x, self.y, self.graph.name)

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

	# Usable functions

	def is_adjacent_to(self, vert):
		return self.adj_vertices.has_key(vert.label)

	def is_incident_on(self, edge):
		return self.incd_edges.has_key(edge.label)

	def is_isolated(self):
		return self.incd_edges == {}

	def has_loop(self):
		for label, edge in self.incd_edges.items():
			if edge.is_loop:
				return True
		return False


class Edge():
	auto_label = 0

	def __init__(self, graph, vert_1, vert_2, dirn=False, label=None, weight=0):
		self.graph = graph
		self.vert_1 = vert_1
		self.vert_2 = vert_2				# Need to decide whether to use 2
		self.verts = (vert_1, vert_2)		#  vert instances or a tuple
		self.dirn = dirn
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

	# Usable functions

	def is_incident_on(self, vert_1, vert_2=None):
		if vert_2 is not None:
			return vert_1 in self.verts and vert_2 in self.verts
		return vert_1 in self.verts

	def is_loop(self):
		return self.vert_1 is self.vert_2

	def is_parallel_to(self, edge):
		return sorted(self.verts) == sorted(edge.verts)


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
		s =  "     Graph: " + self.name + "(V, E) with\n"
		s += "Vertex set: V = " + str([v for v in self.verts]) + "\n"
		s += " Edges set: E = " + str([e for e in self.edges])
		return s 

	def add_vertex(self, x, y, label=None, vert=None):
		# TODO: Handle adding vert versus creating vert
		if vert is not None:
			self.verts[vert.label] = vert
			return vert
		return Vertex(self, x, y, label)
	
	def add_edge(self, vert_1, vert_2, label=None, edge=None, dirn=False):
		if edge is not None:
			self.edges[edge.label] = edge
			return edge
		return Edge(self, vert_1, vert_2, dirn=dirn, label=label)

	def get_vertex(self, label):
		return self.verts[label]
	
	def get_edge(self, label):
		return self.edges[label]

	def num_loops(self):
		loops = 0
		for label, edge in self.edges.items():
			if edge.is_loop:
				loops += 1
		return loops

	def is_directed(self):
		for label, edge in self.edges.items():
			if edge.dirn:
				return True
		return False

	def has_parallel_edges(self):
		# TODO: Implement this
		# 	Check 1st item w/ whole list
		# 	move to next item an check w/
		# 	rest of list

		edge_list = self.edges.values()
		# for e in edge_list:
		# 	print e.label
		n = len(edge_list) - 1
		count = 1
		for i in range(n):
			for j in range(n - count + 1):
				# print str(i) + " " + str(j + i + 1)
				# print str(count) + ": " + edge_list[i].label + " => " + edge_list[j+ i + 1].label
				if edge_list[i].is_parallel_to(edge_list[i + j + 1]):
					return True
			count += 1
		# for label, edge in self.edges.items():
		# 	for label
		# 	if edge.:
		# 		return True
		return False

	# A simple graph is a graph with no loops or parallel edges
	def is_simple_graph(self):
		return not self.has_parallel_edges() and self.num_loops() == 0
	
	def is_path(self, path):
		for i in range(len(path) - 1):
			if not path[i].is_adjacent_to(path[i + 1]):
				return False
		return True
	
	def is_simple_cycle(self, path):
		pass

	def is_cycle(self, path):
		pass

	def is_bipartite(self):
		V1 = []
		V2 = []
		vrts = list(self.verts.values())
		vrts_len = len(vrts)		# Original length of vrts
		tmp_v = []

		tmp_1 = []
		tmp_2 = []


		l = 1
		

		tmp_cnt = 1
		# raw_input( "vrts: {}".format(vrts) )

		while len(vrts) > 0:
			v0 = vrts.pop(0)

			# raw_input( "{} v0: {}".format(tmp_cnt, v0) )

			# Add the first vertex to V1
			V1.append(v0)

			# Add all of its vertices to V2
			tmp_v = list(v0.adj_vertices.values())
			for i in range( len(tmp_v) ):
				V2.append(tmp_v[i])
				tmp_2.append( (tmp_v[i], v0) )

			l = 2

			tmp_cnt_2 = 1
			while True:
				if l is 1:

					# raw_input( "l is 1 {} tmp_1: {}".format(tmp_cnt_2, tmp_1) )

					# Cycle through tmp_1
					while len(tmp_1) > 0:
						v = tmp_1.pop(0)

						# raw_input( "{} v: {}".format(tmp_cnt_2, v) )

						# raw_input( "{} tmp_v: {}".format(tmp_cnt_2, tmp_v) )

						tmp_v = list(v[0].adj_vertices.values())
						for i in range( len(tmp_v) ):
							if tmp_v[i] is not v[1]:
								if tmp_v[i] not in V2:
									V2.append(tmp_v[i])
								tmp_2.append( (tmp_v[i], v) )
								
								# raw_input( "{} will attempt to remove: {} from {}".format(tmp_cnt_2, tmp_v[i], vrts) )
								if tmp_v[i] in vrts:
									vrts.remove( tmp_v[i] )
					l = 2

					# raw_input("break")
					break

				elif l is 2:

					# raw_input( "l is 2 {} tmp_2: {}".format(tmp_cnt_2, tmp_2) )

					# Cycle throught tmp_2
					while len(tmp_2) > 0:
						v = tmp_2.pop(0)

						# raw_input( "{} v: {}".format(tmp_cnt_2, v) )

						tmp_v = list(v[0].adj_vertices.values())

						# raw_input( "{} tmp_v: {}".format(tmp_cnt_2, tmp_v) )

						for i in range( len(tmp_v) ):
							if tmp_v[i] is not v[1]:
								if tmp_v[i] not in V1:
									V1.append(tmp_v[i])
								tmp_1.append( (tmp_v[i], v) )

								# raw_input( "{} will attempt to remove: {} from {}".format(tmp_cnt_2, tmp_v[i], vrts) )
								if tmp_v[i] in vrts:
									vrts.remove(tmp_v[i])
					l = 1

				tmp_cnt_2 += 1
			tmp_cnt += 1


		
		# # If they're already there return false
		# curr_vtx = vrts[0]
		# tmp_1 = []
		# tmp_2 = curr_vtx.adj_vertices.values()
		# for i in range( len(tmp_2) ):
		# 	if tmp_2[i] not in V2:
		# 		tmp_2.append(tmp_1[i])
		# 		V2.append(tmp_vert_list[i])
		# 	else:
		# 		False

		# for i in range( len(tmp_2) )



		# Length check. length of V1 + V2 = self.verts
		len_test = len(V1) + len(V2) == vrts_len
		intersect_test = len( [val for val in V1 if val in V2] ) == 0

		# print "V1: {}".format(V1)
		# print "V2: {}".format(V2)
		# print "vrts len: ".format(vrts_len )
		# print "len_test: {}".format(len_test)
		# print "inter_test: {}".format(intersect_test)

		if len_test and intersect_test:
			return (V1, V2)
		else:
			return None


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
