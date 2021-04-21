import string

# GLOBAL VARS --------------------------------------------------
EXIT_CHAR = "*"
END_CHAR = "-1"
MAX_NODES = 100

input_info = dict()

# FUNCITONS ----------------------------------------------------
def algo_choice():

    print( "escolha o algoritimo:" )
    print( "0 - kruskal" )
    print( "1 - prim" )

    while True:

        c = input()
        if c == EXIT_CHAR: raise InterruptedError

        if c == "0":
            input_info[ "algo" ] = "KRUSKAL"
            break
        elif c == "1":
            input_info[ "algo" ] = "PRIM"
            break
        else:
            print( "entrada invalida, digite novamente")
    
    print()

def mode_choice():

    print( "escolha o modo:" )
    print( "0 - random" )
    print( "1 - custom" )

    while True:

        c = input()
        if c == EXIT_CHAR: raise InterruptedError

        if c == "0":
            input_info[ "build" ] = "RANDOM"
            break
        elif c == "1":
            input_info[ "build" ] = "CUSTOM"
            break
        else:
            print( "entrada invalida, digite novamente")
    
    print()

def exec_choice():

    print( "escolha a execução:" )
    print( "0 - direta" ) # Runs a step after the other, pausing after pressing enter
    print( "1 - iterativa" ) # Runs a step each time the key 'enter' is pressed

    while True:

        c = input()
        if c == EXIT_CHAR: raise InterruptedError

        if c == "0":
            input_info[ "exec" ] = "DIRECT"
            break
        elif c == "1":
            input_info[ "exec" ] = "ITERACT"
            break
        else:
            print( "entrada invalida, digite novamente")

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

def get_user_input():

    try:
        algo_choice()
        mode_choice()
        exec_choice()
        if input_info["build"] == "RANDOM":
            random_build()
        elif input_info["build"] == "CUSTOM":
            custom_build()
        
        print( *input_info.items() , sep = "\n")

    except InterruptedError:
        return

if __name__ == "__main__":
    get_user_input()