# An animation for the resolution of the Minimum Spanning Tree problem

## About
**UFF - UNIVERSIDADE FEDERAL FLUMINENSE**
**AUTHORS:**   Lucas Fuzato Cipriano, Mariana Suarez de Oliveira
**CLASS:**     Algorithm Desingn and Analysis.
**PROFESSOR:** Mr. Celso da Cruz de Oliveira

## Overview

The goal of this project is to develop a desktop application that show
the step by step resolution of the minnimum spanning tree problem through
a simple graphic user interface. The animation should be clear enought for
the understanding of the execution and the user must be able to customize the
input through the command line interface

## The MST problem and its solutions

Supose the existance of a graph **G( V , E )** that is undirected and have weighted
( positive ) edges. Find for G a tree **T( Va , Ea )** that:
    - have all vertices of G ( Spanning )
    - the sum of the weights of its edges is the smallest possible ( Minimum )

The problem is solveable by the use of greedy algorithms for optimal value, and its generic solution is 
the one described below.

### Generic Solution

```
GEN-MST( V , E )

    Va = {}
    Ea = {}

    while V - Va != {}

        safe_edges = { e | e in E , SAFE( e , Va ) }

        e = ARG-MIN-WEIGHT( safe_edges , E )
        Ea = Ea + { e }

        y = { y' | y' in e , y not in Va }
        Va = Va + y
    
    return Va , Ea

```

in this context, an edgde is said **safe** to a given set **Va** when at least one of her vertices
is not in **Va**. The greedy choice here is to choose the safe edge to Va with the smallest weight
, add it to Ea and uptdate **Va** with its new( s ) vertice( s ). When **Va == V**, we have no more 
safe edges, therefore we quit.

Any solution that fits the description of the genereric one is solves the MST for optimal value. In this project,
two are of most interest: Kruskall and Prim.

### Kruskall Solution

The algorithm, introduced in 1956, by joseph kruskall, have the following pseudocode

```
KRUSKALL-MST( V , E )

    Va = {}
    Ea = {}

    E' = SORT-WEIGHT( E )  //1
    T = { { x } | x in V } //2

    for e in E'
        ( a , b ) = e

        T1 = TREE( a , T ) // 3
        T2 = TREE( b , T )
        if T1 == T2
            continue

        Ea = Ea + { e }
        y = { y' | y' in e , y not in Va }
        Va = Va + y

        //4
        T = T - T1
        T = T - T2
        T = T + MERGE( T1 , T2 )
    return Va , Ea
```

1 - **E'** is a ordenation of de edges in **E**, ascending on weight. By iterating on **E'** every safe edge found
must be an edge of **Ea**. Thus **E'** must be iterated only once.

2 - **T** is the set of all trees present at each iteration. It is initialized with everey tree with one node of V.

3 - Find the Tree in **T** where node **a** is located. **T1** must be different from **T2**, if they aren't it means
that the current edge is not safe, so adding it will create a cycle.

4 - If the current edge have node in each tree, it means that it unites two distinc trees. So adding it to **Ea** 
implies that **T1** and **T2** must be replaced by the union of both.

### Prim Solution

```
PRIM-MST( V , E )

    x = RANDOM( V )
    Va = { x }
    Ea = {}

    P = CONNECTING-EDGES( x , E )

    while P != {}
        e = ARG-MIN-WEIGHT( P , E )
        P = P - { e }

        if not SAFE( e , Va )
            continue
        
        Ea = Ea + { e }

        y = { y' | y' in e , y not in Va }
        Va = Va + y

        x = RANDOM( y )
        P' = CONNECTING-EDGES( x , E )
        P = P + P'

    return Va , Ea
```

### Proof of correctness

## Command Line manual

## GUI design

## How to install

## References

