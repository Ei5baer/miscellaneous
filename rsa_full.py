msg = "101010110000101010110000101010110000101010110000101010110000101010"
print "msg is" + msg



def encryprsa(msg):
  pq = 91
  ecrexp = 11
  dcrexp = 59
  blk_size_msg = 6
  blk_size_msg_encrypted_string = 7
  intValueOfBlks = []
  blkbegin_idx = 0

  while(True):
    blkend_idx = blkbegin_idx + blk_size_msg
    if (blkend_idx > len (msg)):
      break
    val = 0
    for j in range (blkbegin_idx, min(blkend_idx,len(msg))):
      val = val + (ord(msg [j]) - ord('0'))* (2**(j -blkbegin_idx))
    intValueOfBlks.append( val )
    blkbegin_idx = blkend_idx
  print intValueOfBlks

  encryptedintval = []
  for val in intValueOfBlks:
    encryptedintval.append(pow(val, ecrexp, pq))
  
  
  encr_string = ""
  for i in range(len(encryptedintval)):
    zeroOneString = ""
    intval = encryptedintval[i]
    for i in range (0, blk_size_msg_encrypted_string):
      if (intval%2 == 0):
        zeroOneString += "0"
      else:
        zeroOneString += "1"
      intval = intval // 2
    encr_string += zeroOneString
  print encr_string
  return encr_string #printsfiletobedecrypted
  
new_msg = encryprsa ("101010110000101010000100101000101010101100001010100001001010001010101011000010101000010010100010101010110000101010000100101000101010101100001010100001001010001010101011000010101000010010100010")
  




def decryprsa(msg):
  pq = 91
  ecrexp = 11
  dcrexp = 59
  blk_size_msg = 7
  blk_size_msg_decrypted_string = 6
  intValueOfBlks = []
  blkbegin_idx = 0

  while(True):
    blkend_idx = blkbegin_idx + blk_size_msg
    if (blkend_idx > len (msg)):
      break
    val = 0
    for j in range (blkbegin_idx, min(blkend_idx,len(msg))):
      val = val + (ord(msg [j]) - ord('0'))* (2**(j -blkbegin_idx))
    intValueOfBlks.append( val )
    blkbegin_idx = blkend_idx
  print intValueOfBlks

  decryptedintval = []
  for val in intValueOfBlks:
    decryptedintval.append(pow(val, dcrexp, pq))
  
  
  dcr_string = ""
  for i in range(len(decryptedintval)):
    zeroOneString = ""
    intval = decryptedintval[i]
    for i in range (0, blk_size_msg_decrypted_string):
      if (intval%2 == 0):
        zeroOneString += "0"
      else:
        zeroOneString += "1"
      intval = intval // 2
    dcr_string += zeroOneString
  print "decrypted string is " + dcr_string #printsfiletobedecrypted
  
decryprsa ( new_msg )
  
