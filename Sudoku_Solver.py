import sys

sys.setrecursionlimit(200000)

array = [[9, 0, 4, 5, 0, 0, 0, 3, 0],[5, 0, 0, 6, 0, 7, 0, 0, 0],[7, 8, 0, 0, 0, 0, 0, 0, 0],[4, 0, 0, 0, 0, 9, 5, 0, 0],[2, 3, 0, 0, 6, 0, 0, 7, 8],[0, 0, 9, 2, 0, 0, 0, 0, 3],[0, 0, 0, 0, 0, 0, 0, 2, 9],[0, 0, 0, 8, 0, 3, 0, 0, 6],[0, 9, 0, 0, 0, 2, 3, 0, 7]]

def isCellEmpty(arr,row,col):
  if(arr[row][col] == 0):
    return True
  else:
    return False


def issafe_old(arr, row, col, num):
  i=0
  j=0
  for i in range(0,9):
    if(num == arr[row][i]):
      return False
    else:
      for j in range(0,9):
        if(num == arr[j][col]):
          return False
        else:
          r = row // 3 
          c = col // 3  
          r = r*3 
          c = c*3 
          for i in range (r, r + 3):
            for j in range (c, c + 3):
              if (arr[i][j] == num):
                return False
              else:
                return True

def ifrowsafe(arr, row, num):
  for i in range(0,9):
    if(num == arr[row][i]):
      return False
  return True
    
def ifcolumnsafe(arr, col, num):
  for j in range(0,9):
    if(num == arr[j][col]):
      return False
  return True

def gridsafe(arr, row, col, num):
  r = row // 3 
  c = col // 3  
  r = r*3 
  c = c*3 
  for i in range (r, r + 3):
    for j in range (c, c + 3):
      if (arr[i][j] == num):
        return False
  return True

def issafe(arr, row, col, num):
  count = 0
  if (ifrowsafe(arr, row, num) == True):
    count = count + 1
  if (ifcolumnsafe(arr, col, num) == True):
    count = count + 1
  if (gridsafe(arr,row, col, num) == True):
    count = count + 1
  if (count == 3):
    return True
  else:
    return False


def solve_sudoku_old(arr):
  nums = [x for x in range (1, 10)]
  isterminalcase = True
  for i in range(0,9):
    for j in range (0,9):
      if (isCellEmpty(arr, i, j) == True):
        isterminalcase = False
        for p in nums:
          if (issafe (arr, i, j, p) == True):
            arr[i][j] = p
            # solve_sudoku( arr )
            if (solve_sudoku(arr)==True):
              print "returning true"
              return True
            # end if
          # end if
        # end for 
      # end if
    # end for
  # end for
  if ( isterminalcase ) :
    print "A terminal case : returning True "
  else :
    print "Not a terminal case : and could not fill : returning false "
  return isterminalcase        
# end def 
  

def findEmptyCell ( arr ) :
  for i in range(9) :
    for j in range(9) :
      if ( arr[i][j]==0 ) :
        return (i,j)
      # end if
    # end for
  # end for
  return None
# end def

def solve_sudoku(arr):
  nums = [x for x in range (1, 10)]
  isterminalcase = True

  cell = findEmptyCell( arr ) 
  
  if ( cell == None ) :
    print "A terminal case : returning True "
    return True
  
  row = cell[0]
  col = cell[1]

  for p in nums:
    if (issafe (arr, row, col, p) == True):
      arr[row][col] = p
      # solve_sudoku( arr )
      if (solve_sudoku(arr)==True):
        print "returning true"
        return True
      else :
        arr[row][col] = 0
      # end if
    # end if
  # end for 

  print "Not a terminal case : and could not fill : returning false "
  return False        
# end def 

solve_sudoku (array)

print (array)

   
          
    
  
