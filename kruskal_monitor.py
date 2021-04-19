
Va = set()
Ea = set()
E_prime = []
T = dict()
rejected = True

N = 0
pos = 0 

def _init( V1s , V2s , Ws ):

    global N , pos 

    N = len( V1s )
    idx = [ x for x in range( N ) ]
    
    foo = lambda x : Ws[ x ]
    idx.sort( key = foo )

    for i in idx:
        a = V1s[ i ]
        b = V2s[ i ]

        E_prime.append( ( a , b ) )

    V = set()
    for a , b in E_prime:
        V.add( a )
        V.add( b )

    for i , n in enumerate( V ):
        T[ n ] = i

def _next():
    global pos , N, rejected
    if pos >= N:
        return False
    
    ( x , y ) = E_prime[ pos ]
    r1 = T[ x ]
    r2 = T[ y ]
    rejected = ( r1 == r2 )
    if not rejected:
        Va.add( x )
        Va.add( y )
        Ea.add( ( x , y ) )
        for a in T:
            if T[ a ] == r2: T[ a ] = r1

    pos = pos + 1
    return True

if __name__ == "__main__":

    v1s = []
    v2s = []
    ws  = []

    print( "give us the edges" )

    while True:

        tup = input()
        if not tup: break

        ( v1 , v2 , w ) = tup.split()
        v1s.append( v1 )
        v2s.append( v2 )
        ws.append( int( w ) )
    
    _init( v1s , v2s , ws )
    print( E_prime )

    cond = True
    while cond:

        print('*'*5)
        print( Va )
        print( Ea )
        print( rejected )

        input()
        cond = _next()

        # pos += 1


