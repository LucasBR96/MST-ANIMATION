import kruskal_monitor as krus
import prim_monitor as prim

import networkx as nx
from matplotlib import animation, rc
import matplotlib.pyplot as plt



modo = 1
KRUSKAL = 0
PRIM    = 1
G = nx.Graph()
E = dict()
V = set()
advance = True
clicked = False
fig, ax = plt.subplots(figsize=(10,8))

# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

def solution_generator():
    global advance, modo

    monitor = krus
    if algo == PRIM:
        monitor = prim
    
    monitor._init( V , E )
    while True:
        if(advance):
            if(modo == 1):
                advance = False
            seq = [ monitor._next() for i in range( 3 ) ]
            if(seq.pop()):
                yield pretty_vars(monitor.get_variables(), False)
            else:
                break
        else: 
            yield pretty_vars(monitor.get_variables(), False)
    yield pretty_vars(monitor.get_variables(), True)

def pretty_vars( mst_vars , end):

    global edge_status , current_edge , Va , Ea
    edge_status , current_edge , Va , Ea = mst_vars
    s = ''
    s += "edge_status = {}".format( edge_status ) + "\n"
    s += "current_edge = {} {}".format( *current_edge ) + "\n"
    s += "nodes in tree: " + "\n"
    s += "\t" + ' '.join( Va ) + "\n"
    s += "edges in tree:" + "\n"
    for a , b in Ea:
        s += "\t" + "{} {}".format( a , b ) +"\n"
    if end:
        current_edge = None
    return s

def do_nothing():
    # FuncAnimation requires an initialization function. We don't
    # do any initialization, so we provide a no-op function.
    pass

#FIXME - reduce only to drawing
def update(mst_edges):
    current_edges = set()
    current_edges.add(current_edge)
    ax.clear()

    all_edges = set(tuple(sorted((n1, n2))) for n1, n2 in G.edges())
    node_labels = {}

    for idx, node in enumerate(G.nodes()): 
        node_labels[node] = node

    nx.draw_networkx_edges(
        G, pos, edgelist=all_edges-Ea - current_edges, alpha=0.1,
        edge_color='g', width=1, ax=ax
    )

    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edges(
        G, pos, edgelist=Ea - current_edges , alpha=1.0,
        edge_color='green', width=1, ax=ax
    )
    if(current_edge != None):
        nx.draw_networkx_edges(
            G, pos, edgelist=current_edges , alpha=1.0,
            edge_color='r', width=1, ax=ax
        )
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes()-Va, node_color='gray', alpha=0.5, node_size=300, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=Va, node_color='b', alpha=0.5, node_size=300, ax=ax)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels, alpha=0.5, ax=ax)
    nx.draw_networkx_labels(G, pos, node_labels, alpha=1, ax=ax)


def on_press(event):
    global advance, modo
    if (modo == 1):
        advance = not advance

fig.canvas.mpl_connect('key_press_event', on_press)

def main():
    global pos, algo, ani, modo
    print( "escolha o algoritimo:" )
    print( "0 - kruskal" )
    print( "1 - prim" )
    algo = int( input() )

    print( "selecione o modo:" )
    print( "0 - direto" )
    print( "1 - controlado" )
    modo = int( input() )

    print()
    print( "digite os vertices do grafo" )
    print( 'formato: m m i' )
    print( "m -> minuscula")
    print( "i -> inteiro" )
    print( "digite -1 se acabou")

    while True:
        tup = input().rstrip()
        if tup == "-1":
          break
        a , b , m = tup.split()
        E[ ( a , b ) ] = int( m )
        V.add( a )
        V.add( b )

    
    G.add_nodes_from(V)

    for key in E.keys():
        print(key[0], key[1], E[key])
        G.add_edge(key[0], key[1], weight = E[key])

    pos = nx.random_layout(G)

    node_labels = {}

    for idx, node in enumerate(G.nodes()): 
        node_labels[node] = node


    #ani = Player(fig, krus, ax, G, V, E, pos, nx.get_edge_attributes(G,'weight') ,node_labels)
    ani = animation.FuncAnimation(
           fig,
           update,
           init_func=do_nothing,
          frames=solution_generator,
           interval=500,
           repeat = False
    )
    plt.show()



main()