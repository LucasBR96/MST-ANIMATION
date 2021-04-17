# An for the resolution of the Minimum Spanning Tree problem

## About
UFF - UNIVERSIDADE FEDERAL FLUMINENSE
AUTHORS: Lucas Fuzato Cipriano, Mariana Suarez de Oliveira
CLASS: Algorithm Desingn and Analysis.
PROFESSOR: Mr. Celso da Cruz de Oliveira

## Overview

The goal of this project is to develop a desktop application that show
the step by step resolution of the minnimum spanning tree problem through
a simple graphic user interface. The animation should be clear enought for
the understanding of the execution and the user must be able to customize the
input through the command line interface

## The MST problem and its solutions

Supose the existance of a graph G( V , E ) that is undirected and have weighted
( positive ) edges. Find for G a tree T( Va , Ea ) that:
    - have all vertices of G ( Spanning )
    - the sum of the weights of its edges is the smallest possible ( Minimum )

The problem is solveable by the use of greedy algorithms for optimal value, and its generic solution is 
the one described below.

### Generic Solution

Algo Here

in this context, an edgde is said safe to a given set Va when at least one of her vertices
is not in Va. The greedy choice here is to choose the safe edge to Va with the smallest weight
, add it to Ea and uptdate Va with its new( s ) vertice( s ). When Va == V, we have no more safe edges
, then we quit.

Any solution that fits the description of the genereric one is solves the MST for optimal value. In this project,
two are of most interest for this project: Kruskall and Prim.

### Kruskall Solution

The algorithm, introduced in 1956, by joseph kruskall, have the following pseudocode

Algo Here



## References

