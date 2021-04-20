import kruskal_monitor as krus
import prim_monitor as prim

KRUSKAL = 0
PRIM    = 1

def solution_generator( V , E , algo ):

    monitor = krus
    if algo == PRIM:
        monitor = prim
    
    monitor._init( V , E )
    while monitor._next():
        yield monitor.get_variables()

def pretty_vars( mst_vars ):

    edge_status , current_edge , Va , Ea = mst_vars
    s = ''
    s += "edge_status = {}".format( edge_status ) + "\n"
    s += "current_edge = {} {}".format( *current_edge ) + "\n"
    s += "nodes in tree: " + "\n"
    s += "\t" + ' '.join( Va ) + "\n"
    s += "edges in tree:" + "\n"
    for a , b in Ea:
        s += "\t" + "{} {}".format( a , b ) +"\n"
    return s

def main():

    print( "escolha o algoritimo:" )
    print( "0 - kruskal" )
    print( "1 - prim" )
    n = int( input() )

    print()
    print( "digite os vertices do grafo" )
    print( 'formato: m m i' )
    print( "m -> minuscula")
    print( "i -> inteiro" )
    print( "digite -1 se acabou")

    E = dict()
    V = set()
    while True:
        tup = input().rstrip()
        if tup == "-1":
            break
        a , b , m = tup.split()
        E[ ( a , b ) ] = int( m )
        V.add( a )
        V.add( b )

    for x in solution_generator( V , E , n ):
        input()
        print( pretty_vars( x ) )

main()