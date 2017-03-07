from graph import Graph

def main():
	print "hello world"
	g = Graph()
	print g.name
	v1 = g.add_vertex(1,1)
	v2 = g.add_vertex(2,2)
	print v1
	print v2

if __name__ == '__main__':
	main()