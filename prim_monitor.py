from collections import deque

Va = set()
Ea = set()
Possible_neighbors = deque([])
Adj_lst = dict()
rejected = False
E_val = dict()

def intercal( arr1 , arr2 , foo ):

    i , j = 0 , 0
    seq = []

    while i < len( arr1 ) or j < len( arr2 ):

        if i >= len( arr1 ):
            seq.append( arr2[ j ] )
            j += 1
        elif j >= len( arr2 ):
            seq.append( arr1[ i ] )
            i += 1
        elif foo( arr1[ i ] ) < foo( arr2[ j ] ):
            seq.append( arr1[ i ] )
            i +=1
        else:
            seq.append( arr2[ j ] )
            j += 1
    
    return seq

def _init( V , E ):

    global E_val
    E_val = E

    E_set = list( tup for tup in E )
    E_set.sort( key = lambda x: E[ x ] )

    global Adj_lst
    for edge in E_set:
        ( a , b ) = edge
        Adj_lst[ a ] = Adj_lst.get( a , [] ) + [ edge ]
        Adj_lst[ b ] = Adj_lst.get( b , [] ) + [ edge ]
    
    global Possible_neighbors , Va
    Possible_neighbors.extend( Adj_lst[ a ] )
    Va.add( a )

def _next():

    global Possible_neighbors
    if len( Possible_neighbors ) == 0:
        return False

    neigh = Possible_neighbors.popleft()
    
    a , b = neigh
    r1 = a in Va
    r2 = b in Va
    global rejected
    rejected = not r1^r2
    if not rejected:

        Ea.add( neigh )
        y = b if r1 else a
        Va.add( y )

        global Adj_lst, E_val
        new_edges = [ tup for tup in Adj_lst[ y ] if tup != ( a , b ) ]
        Possible_neighbors = deque( intercal( Possible_neighbors , new_edges , lambda x: E_val[ x ] ) )

    return True
if __name__ == "__main__":

    # E = dict()
    E = {
        ('a','b') :1 ,
        ('a', 'd'): 2,
        ('a', 'i'): 7,
        ('b', 'c'): 3,
        ('b', 'd'): 5,
        ('c', 'd'): 3,
        ('c', 'e'): 2,
        ('d', 'i'): 1,
        ('d', 'e'): 2,
        ('e', 'f'): 3,
        ('e', 'g'): 4,
        ('e', 'h'): 2,
        ('f', 'g'): 8,
        ('g', 'h'): 2,
        ('h', 'i'): 10
    }
    V = set()

    # print( "give us the edges" )

    # while True:

    #     tup = input()
    #     if not tup: break

    #     ( v1 , v2 , w ) = tup.split()
    #     V.add( v1 )
    #     V.add( v2 )

    #     E[ ( v1 , v2 ) ] = int( w )
    
    _init( V , E )
    cond = True
    while cond:

        print('*'*5)
        print( Possible_neighbors )
        print( Va )
        print( Ea )
        print( rejected )

        input()
        cond = _next()



