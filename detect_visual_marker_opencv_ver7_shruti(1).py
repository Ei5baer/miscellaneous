# Author : Shruti Patkar ( with help from https://github.com/pierre-rouanet/hampy/tree/master/hampy and SBP )
# 29th June 2018




import cv2
import matplotlib.pyplot as plt
import math

import numpy as np
from numpy.random import randint as np_randint


msg_size = 7
data_size = 4
marker_size = msg_size + 2

#screen_size = 1000

parity_bits = [0, 1, 3]
data_bits = [2, 4, 5, 6]

G = np.array(((1, 1, 0, 1),
           (1, 0, 1, 1),
           (1, 0, 0, 0),
           (0, 1, 1, 1),
           (0, 1, 0, 0),
           (0, 0, 1, 0),
           (0, 0, 0, 1)))

H = np.array(((0, 0, 0, 1, 1, 1, 1),
           (0, 1, 1, 0, 0, 1, 1),
           (1, 0, 1, 0, 1, 0, 1)))


def hamming_encode(B):
    B = np.array(B)

    C = np.dot(G, B.T).T % 2

    return C


def hamming_decode(C):
    print "In Hamming decode"
    C = np.array(C)
    if np.any( np.dot(H, C.T).T % 2 == 1 ) :
      raise ValueError("Incorrect Hamming code word")
    B = C[:, data_bits]
    return B


test_b1 = np.array([0, 0, 1, 1])
test_b2 = [[0, 0, 0, 1], [0, 1, 0, 1]]

test_c1 = [1, 0, 0, 0, 0, 1, 1]
test_c2 = np.array([[1, 1, 0, 1, 0, 0, 1],
                             [0, 1, 0, 0, 1, 0, 1]])



B = []
hamming_codeword = []

for i in range(3):
  a = np_randint(2, size=(1000, data_size))
  B.append(a)
   
  x = hamming_encode( a )
  hamming_codeword.append(x)
# end for
print "printing B ", B
print "printing hamming_codeword hamming_encode(B) ", hamming_codeword

print "calling hamming_decode"
decodedC = hamming_decode( hamming_codeword[0])
print "hamming decoded word is ", decodedC

raw_input("press any key to continue : ")

raw_input("pausing a bit .... press any key to continue ... " )


def generate_markers( ) :

  TL = [ {'x':50,'y':50} , {'x':250, 'y':300} , { 'x':350, 'y':100 }   ]


  img = np.zeros( (500, 500) )

  for i in range( 3 ) :
    for col in range( msg_size ) :
      for row in range( msg_size ) :
        img[ TL[i]['x'] + 10*(row+2)+1: TL[i]['x']+10*(row+3)-1 , 
             TL[i]['y']+10*(col+2)+1: TL[i]['y']+10*(col+3)-1 ] = hamming_codeword[i][ row, col ] 
      # end for
    # end for
    for row in range( marker_size+2 ) :
      img[ TL[i]['x']+10*(row):TL[i]['x'] + 10*(row+1) , TL[i]['y']+0:TL[i]['y']+10 ] = 1
      img[ TL[i]['x']+10*(row): TL[i]['x']+ 10*(row+1) , TL[i]['y']+10*(marker_size+1): TL[i]['y']+10*(marker_size+2) ] = 1
    # end for
    for col in range( marker_size+2 ) :
      img[ TL[i]['x'] + 0: TL[i]['x']+10 , TL[i]['y'] + 10*(col) : TL[i]['y']+10*(col+1) ] = 1
      img[ TL[i]['x']+10*(marker_size+1): TL[i]['x']+10*(marker_size+2) , TL[i]['y']+10*(col):TL[i]['y']+10*(col+1) ] = 1
    # end for
  # end for


  img = (1 - img) * 255

  cv2.imwrite('./mrkrs_shrt.png', img)

# end def



#generate_markers()



img = cv2.imread('./mrkrs_shrt.png')
img = cv2.cvtColor(img, cv2.cv.CV_BGR2RGB)
width, height, _ = img.shape
print "width and height of img are ", width, height 

#img = cv2.resize(img,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
#width, height, _ = img.shape
print "width and height of img are ", width, height 


plt.imshow( img )
plt.show()

edges = cv2.Canny(img, 10, 100)
#edges = cv2.Laplacian(img, cv2.CV_64F)
#edges = cv2.cvtColor(edges, cv2.COLOR_BGR2GRAY)
plt.imshow( edges )
plt.show()

contours_wrap = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# We only keep the big enough contours
min_area = width * height * .004
print "minimum area is ", min_area
raw_input("continue ? press any key ")
contours = [c for c in contours_wrap[0] if cv2.contourArea(c) > min_area]
print "number of contours is ", len( contours )
raw_input("continue ?")

warped_size = 9 * 10
canonical_marker_coords = np.array(((0, 0),
                                     (warped_size - 1, 0),
                                     (warped_size - 1, warped_size - 1),
                                     (0, warped_size - 1)),
                                     dtype='float32')
markers = []
mrkctr = []


for c in contours:
#    print "drawing contour"
#    print c
    cv2.drawContours(img, [c], -1, (255, 255, 0), 3)
    plt.imshow(img)
#    plt.show()
#    x = raw_input( "continue ? (y/n)" )
#    if ( not ( x == "y" ) ) :
#      exit()

    approx_curve = cv2.approxPolyDP(c, cv2.arcLength(c,True) * 0.1, True)
#    approx_curve = cv2.approxPolyDP(c, len(c) * 0.01, False)
    if not (len(approx_curve) == 4 and cv2.isContourConvex(approx_curve)):
        print " Continue not having a suitable number of points or is not convex : Continue"
        continue

    
    sorted_curve = np.array(cv2.convexHull(approx_curve, clockwise=False), dtype='float32')
    print "sorted curve\n", sorted_curve
    
#    continue

    persp_transf = cv2.getPerspectiveTransform(sorted_curve,canonical_marker_coords)
    print persp_transf

    warped_img = cv2.warpPerspective(img, persp_transf, (warped_size, warped_size))


    warped_gray = cv2.cvtColor(warped_img, cv2.COLOR_BGR2GRAY)
    _, warped_bin = cv2.threshold(warped_gray, 50, 255, cv2.THRESH_BINARY)

    print "size of warped_binary image is ", warped_bin.shape

    plt.imshow( warped_bin ) 
    plt.show() 

    marker = cv2.resize( warped_bin, None, fx=1.0/10 , fy = 1.0/10 )

    markers.append( marker )
    mrkctr.append( cv2.contourArea(c) )
#    plt.imshow( marker ) 
#    plt.show() 





distance = []
focal_lnt = 5
z = 10
x = [3,4,5]
y = [5,4,5]
mrkr_area = 6

for i in range(3):
    distance.append( focal_lnt*math.sqrt (mrkctr[i]/6) )
    

plt.imshow(img)
plt.show()


#scipy.optimize.fsolve

#scipy.optimize.fsolve(func, x0, args=(), fprime=None, full_output=0, col_deriv=0, xtol=1.49012e-08, maxfev=0, band=None, epsfcn=None, factor=100, diag=None)



import scipy
import scipy.optimize


def f ( x , mat_3x4  ) :
#  print "f called with mat_3x4 as ", mat_3x4
  result = [0 for i in range(3)]
  result[0] =   (
                  ( x[0] - mat_3x4[0][0] )**2 +
                  ( x[1] - mat_3x4[0][1] )**2 +
                  ( x[2] - mat_3x4[0][2] )**2
                  - mat_3x4[0][3]
                )
 
  result[1] =   (
                  ( x[0] - mat_3x4[1][0] )**2 +
                  ( x[1] - mat_3x4[1][1] )**2 +
                  ( x[2] - mat_3x4[1][2] )**2   
                  - mat_3x4[1][3]
                )
 
  result[2] =   (
                  ( x[0] - mat_3x4[2][0] )**2 +
                  ( x[1] - mat_3x4[2][1] )**2 +
                  ( x[2] - mat_3x4[2][2] )**2   
                  - mat_3x4[2][3]
                )
 
  return result

# end def


d = distance
#d=[1.0,1.0,1.0]

mat_3x4 = [ [ 1,0,0,d[0]] , [0,1,0,d[1]], [0,0,1,d[2]]  ]

print scipy.optimize.fsolve( f , [0.5,0.5,0.5] , mat_3x4 )
