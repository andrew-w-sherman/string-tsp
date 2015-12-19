import networkx as nx
import matplotlib.pyplot as plt

#modified from an example in the networkx docs
def plot_graph(positions, edges, outfile):
    try:
        G = nx.Graph()
        G.add_nodes_from(range(0,len(positions)))
        for edge in edges:
            G.add_edge(edge[0],edge[1])
        G.position = {}
        for i, position in enumerate(positions):
            G.position[i] = position

        plt.figure(figsize=(8,8))
        nx.draw(G,pos=G.position,with_labels=False,node_size=3)

        plt.xlim(0,max([x[0] for x in positions]))
        plt.ylim(0,max([x[1] for x in positions]))

        plt.savefig(outfile)
    except:
        pass
