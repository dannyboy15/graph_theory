from graph import *

def main():
	print "hello world"
	g = Graph()
	print g.name
	v = Vertex(g,1,2)
	v1 = g.add_vertex(1,1)
	v2 = g.add_vertex(2,2)
	print v
	print v1
	print v2

if __name__ == '__main__':
	main()