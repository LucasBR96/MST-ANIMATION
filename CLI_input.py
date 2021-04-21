import string

# GLOBAL VARS --------------------------------------------------
EXIT_CHAR = "*"

# KRUSKAL = 0
# PRIM    = 1

# RANDOM  = 0
# CUSTOM  = 1

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
    
if __name__ == "__main__":
    algo_choice()
    mode_choice()
    if input_info["build"] == "RANDOM":
        random_build()
    
    print( *input_info.items() , sep = "\n")