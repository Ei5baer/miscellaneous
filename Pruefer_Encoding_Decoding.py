# Pruefer_Encoding_Decoding_Ei5baer

import random
import copy

N = 10

V = range( N )

pruefer_seq = [ int( random.random( ) * N )   for i in range( N-2 ) ]

degree_array = [ None for i in range( N ) ]
neighbors = [ [] for i in range( N ) ]


for j in range(N) :
  degree_array[ j ] = 1

for i in range(0,N-2) :
  degree_array[ pruefer_seq[ i ] ] += 1 

degree_array_copy = copy.deepcopy( degree_array )

for i in range( 0, N-2 ) :
  k = pruefer_seq[i]
  # let j be the smallest i such that degree[i]=1
  j = degree_array_copy.index( 1 )
  # add the edge (j,k) to the graph T
  neighbors[j].append(k)
  neighbors[k].append(j)
  degree_array_copy[j] = degree_array_copy[j] - 1
  degree_array_copy[k] = degree_array_copy[k] - 1

#let j and k be the only two values of i such that deg[i]=1
j = degree_array_copy.index( 1 )
j = degree_array_copy.index( 1, j+1 )
#add the edge (j,k) to the graph T
degree_array_copy[j] = degree_array_copy[j] - 1
degree_array_copy[k] = degree_array_copy[k] - 1

print pruefer_seq
print degree_array
print neighbors

neighbors_copy = copy.deepcopy( neighbors )

encoded_pruefer_seq = [ None for i in range( N-2 ) ]

for i in range(0, N-2) :
  # let j be the leaf with the smallest label
  j = min( [ ii if degree_array[ii]==1 else N+1  for ii in range(N) ] )
  # let k be the (unique) node attached to j
  k = neighbors_copy[ j ][0]
  encoded_pruefer_seq[ i ] = k
  # remove node j and edge (j,k) from the tree;
  degree_array[ j ] -= 1  
  degree_array[ k ] -= 1  
  neighbors_copy[ j ].remove( k )
  neighbors_copy[ k ].remove( j )

print encoded_pruefer_seq

print "Note that the original Pruefer Sequence that we decoded into a tree \n"
print " and Pruefer sequence obtained by encoding that tree are verified to be equal \n"

print "\n"

print pruefer_seq
print encoded_pruefer_seq

print "The unique Tree corresponding to this Pruefer sequence is\n"

print neighbors
