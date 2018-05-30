# file HuffmanCoding.py

#  Eisbaer
#  Monday: 7 November 2016

"""
Example :

a:11, b:12, c:13, d:10, e:14, f:13, g:12

"""

syms=['a','b','c','d','e','f','g']

freqs=[11,12,13,10,14,13,12]

HTr = [[syms[i],freqs[i],-1,-1,-1,str(syms[i]),i] for i in range( len(syms) ) ]

print HTr

N = len(syms)

MAX=100000

def find_least_freq_pair_roots ( HTr ) :
  best_nd_id_so_far = -1
  second_best_nd_id_so_far = -1
  best_freq_so_far = MAX
  second_best_freq_so_far = MAX
  
  for i in range ( len( HTr ) ) :
    if ( HTr[ i ][4] == -1 ) :
      if ( HTr[ i ][1] < best_freq_so_far ) :
        best_freq_so_far = HTr[i][1]
        best_nd_id_so_far = i
    
  for i in range ( len( HTr ) ) :
    if ( HTr[ i ][4] == -1 and not ( i == best_nd_id_so_far ) ) :
      if ( HTr[ i ][1] < second_best_freq_so_far ) :
        second_best_freq_so_far = HTr[i][1]
        second_best_nd_id_so_far = i

  return ( best_nd_id_so_far , second_best_nd_id_so_far )

def find_root_id ( HTr ) :
  count = 0
  a_root_id = -1
  for i in range ( len( HTr ) ) :
    if ( count > 1 ) :
      return -1 
    if ( HTr[i][4] == -1 ) :
      count = count+1
      a_root_id = i
  return a_root_id

tree_ready_flag = False 
while ( not tree_ready_flag ) :
  nd1_id, nd2_id = find_least_freq_pair_roots ( HTr )
  if ( nd2_id == -1 ) :
    tree_ready_flag = True 
    break
  else :
    HTr.append( ['_', HTr[nd1_id][1]+HTr[nd2_id][1], nd1_id, nd2_id, -1, HTr[nd1_id][5]+HTr[nd2_id][5]+"_" ] )
    HTr[nd1_id][4] = len(HTr) - 1 
    HTr[nd2_id][4] = len(HTr) - 1 
    
print HTr
     
encoding_of_syms = [ "" for i in range(N) ]

for i in range( N ) :
  for j in range( len( HTr ) ) :
    if HTr[j][0]==syms[i] :
      enc_of_sym = ""
      cur_id = j
      while ( HTr[ cur_id ][4] != -1  ) :
        if ( cur_id == HTr[ HTr[cur_id][4] ][2] ) :
          enc_of_sym = "0" + enc_of_sym
        else :
          enc_of_sym = "1" + enc_of_sym
        cur_id = HTr[ cur_id ][ 4 ]
      print "enc_of_sym of ", syms[i], " is ", enc_of_sym
      encoding_of_syms[ i ] = enc_of_sym

print encoding_of_syms


message = "aabbccddeeffggaa"

encoded_message = ""
for i in range( len( message ) ) :
  encoded_message = encoded_message + encoding_of_syms[ syms.index( message[i] ) ]
    

print encoded_message

root_id = find_root_id ( HTr ) 
cur_id = root_id 
decoded_message = ""
for i in range( len ( encoded_message ) ) :
  cur_id = HTr[ cur_id ][2] if encoded_message[i]=='0'  else HTr[ cur_id ][3]
  if not ( HTr[ cur_id ][0] == '_' ) :
    decoded_message = decoded_message + HTr[ cur_id ][0]   
    cur_id = root_id

print decoded_message
   
