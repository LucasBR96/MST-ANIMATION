import string
import sys

# GLOBAL VARS --------------------------------------------------
EXIT_CHAR = "*"
END_CHAR = "-1"
MAX_NODES = 100

CHAR_TERMS = {
    "a":"algo" , 
    "r":"exec" , 
    "b":"build"  
}

VALID_CHOICES = {
    "algo" :[ "PRIM", "KRUSKAL" ],
    "exec" :[ "DIRECT", "ITER" ],
    "build":[ "CUSTOM" , "RANDOM"],
}

input_info = dict()

# FUNCTIONS ---------------------------------------------------

def random_build():

    # setting number of nodes
    print("digite a quantidade de nos")
    print("maximo -> {}".format( MAX_NODES ) )

    while True:

        c = input()
        if c == EXIT_CHAR: raise InterruptedError
        if all( x in string.digits for x in c ):
            m = int( c )
            if m <= MAX_NODES:
                input_info[ "num_nodes" ] = m
                break
        print( "entrada invalida, digite novamente")
    print()
    
    min_edges = m - 1    # A tree, Basicaly
    max_edges = m**2 - m # Fully connected
    print("digite a quantidade de arestas")
    print("maximo -> {}".format( max_edges ) ) 
    print("minimo -> {}".format( min_edges ) )
    while True:

        c = input()
        if c == EXIT_CHAR: raise InterruptedError
        if all( x in string.digits for x in c ):
            m = int( c )
            if min_edges <= m <= max_edges:
                input_info[ "num_edges" ] = m
                break
        print( "entrada invalida, digite novamente")  
    print()

def custom_build( ):

    print( "digite os vertices do grafo" )
    print( 'formato: m m i' )
    print( "m -> minuscula")
    print( "i -> inteiro" )
    print( "digite -1 se acabou")

    input_info[ "nodes" ] = set()
    input_info[ "edges" ] = dict()
    while True:
        tup = input().rstrip()
        if tup == END_CHAR:
            break
        elif tup == EXIT_CHAR: raise InterruptedError

        s = tup.split()
        if len( s ) != 3 or s[-1] not in string.digits:
            print( "entrada invalida, digite novamente") 
        
        a , b , c = s
        input_info[ "edges" ][ ( a , b ) ] = int( c )
        input_info[ "nodes" ].add( a )
        input_info[ "nodes" ].add( b )
    print()

def char_choice( ch , nome ):

    if ch not in CHAR_TERMS:
        raise ValueError
    term = CHAR_TERMS[ ch ]

    nom = nome.upper()
    if nom not in VALID_CHOICES[ term ]:
        raise ValueError
    
    input_info[ term ] = nom
    
def main( args ):

    i = 0
    while i < len( args ):
        m = args[i]
        if m[ 0 ] == '-':
            char_choice( m[1] , args[ i + 1 ] )
            i += 2

    build_fun = custom_build
    if input_info[ "build" ] == "RANDOM":
        build_fun = random_build
    build_fun()
        
    print( *input_info.items() , sep = "\n")


if __name__ == "__main__":
    main( sys.argv[ 1: ] )
