#GLOBAL VARIABLE VISIBLE BY FILE ONLY ------------------------------------------------
END      = -1
SELECT   = 0
CONSIDER = 1
UPDATE   = 2
global_status = SELECT

E_prime = []
T = dict()

#GLOBAL VARIABLE VISIBLE BY OUTSIDERS------------------------------------------------
CONSIDERED = 0
REJECTED   = 1
ACCEPTED   = 2
edge_status = CONSIDERED
current_edge = ( -1 , -1 )

Va = set()
Ea = set()

N = 0
pos = 0 

#MONITOR FUNCTIONS------------------------------------------------------------------
def _select_fun():

    global current_edge, edge_status, global_status
    current_edge  = E_prime[ pos ]
    edge_status   = CONSIDERED
    global_status = CONSIDER

def _consider_fun( ):

    global edge_status, global_status
    ( x , y ) = current_edge
    r1 = T[ x ]
    r2 = T[ y ]
    edge_status = REJECTED 
    if r1 != r2: 
        edge_status = ACCEPTED
    global_status = UPDATE

def _update_fun( ):

    global Va, Ea, current_edge, edge_status, T, global_status
    if edge_status == ACCEPTED:
        ( x , y ) = current_edge
        Va.add( x )
        Va.add( y )
        Ea.add( ( x , y ) )
        n = T[ x ]
        for a in T:
            if T[ a ] == n: T[ a ] = T[ y ]
    
    global pos , N
    pos = pos + 1
    global_status = SELECT if pos < N else END

def _init( V , E ):

    global E_prime , N
    E_prime = [ tup for tup in E ]
    E_prime.sort( key = lambda x : E[ x ] )
    N = len( E_prime )

    global T
    T = { v:i for i , v in enumerate( V ) }    

def _next( ):

    if global_status == END:
        return False

    if global_status == SELECT:
        _select_fun()
    elif global_status == CONSIDER:
        _consider_fun()
    elif global_status == UPDATE:
        _update_fun()
    return True

def get_variables():

    return( edge_status , current_edge , Va.copy() , Ea.copy() )

if __name__ == "__main__":

    V = set( ["a" , "b" , "c" , "d", "e" ] )
    E = {
        ('a','b'):2,
        ('a','c'):3,
        ('a','d'):4,
        ('c','d'):1,
        ('b','d'):2,
        ('d','e'):7,
        ('c','e'):3,
        ('a','e'):2
    }

    _init( V , E )
    while _next():
        input()
        t = get_variables()
        print( "-"*25 )
        print( *t , sep = "\n" )

    pass


