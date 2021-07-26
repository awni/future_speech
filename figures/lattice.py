import gtn

symbols = {0: "the", 1: "cat", 2: "sat", 3: "that", 4: "sit", 5: "hat"}

g = gtn.Graph()
g.add_node(start=True)
g.add_node()
g.add_node()
g.add_node()
g.add_node(accept=True)

g.add_arc(0, 1, 0, 0, 1.2)
g.add_arc(0, 2, 3, 3, 6.4)
g.add_arc(1, 2, 1, 1, 2.8)
g.add_arc(1, 3, 1, 1, 1.7)
g.add_arc(2, 4, 2, 2, 3.1)
g.add_arc(2, 4, 4, 4, 0.9)
g.add_arc(3, 4, 5, 5, 1.1)

gtn.draw(g, "lattice.pdf", isymbols=symbols)
