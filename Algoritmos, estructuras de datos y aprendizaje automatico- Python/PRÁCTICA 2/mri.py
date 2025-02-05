#############################################################################
#
#  Project: Auxiliary code for the ALGED labs
#  File:    p3-code.py
#  Rev.     1.1
#  Date:    10/04/2022
#           10/27/2021
#
#  This is the auxiliary code for the implementation of the tumor
#  measuring program. It coutains all the sub-funcions you need to
#  implement the required function following the directives of the
#  statement and the instructions given in class.
#
#  The parts where you are supposed to intervene are marked as
#  TO-DO. The rest wiull stay as it is, but we urge you to have a look
#  at it, as it contains useful examples of programming techniques.
#
#  (C) ALGED Lecturers, 2021, 2022
#
import sys

#############################################################################
#
# TO-DO
# Here you must import your own List and stack modules, using the name
# of the file that you have used for them. The files must be copied in
# this directory for things to work properly.
#
import list as lstf
import stack as s
import queue as q


#############################################################################
#############################################################################
#
#  The functions defined in this part are used to create a sequence of
#  pixel addresses that spiral out of a given pixel and are enclosed
#  in an image of given size. 
#
#  These functions are used to find the seed that you will use to
#  start the algorithm.
#
#  The way they work is a bit tricky. You don't use them directly, so
#  you can safely ignore all this part.
#

#
# Return a list with the values that transition from lim1 to lim2,
# excluding both extrema. The function works in both cases: whether it
# is lim2>=lim1 or lim1>lim2.
#
# If lim1=lim2, returns the empty list
#
def transition(lim1, lim2):
    lst = []
    if lim2 >= lim1:
        for k in range(lim1+1,lim2):
            lst = lst + [k]
    else:
        for k in range(lim1-1,lim2,-1):
            lst = lst + [k]
    return lst

#
# Generates the sequence of row indices that compose the
# spiral. Returns a sequence of n row indices
#
def rgen(n):
    rows = [0, 0]
    stay = 3
    lim = -1

    while len(rows) < n:
        rows = rows + stay*[lim] #dostay(lim, stay)
        if lim > 0:
            newlim = -(lim+1)
        else:
            newlim = -lim
        rows = rows + transition(lim, newlim)
        lim = newlim
        stay = stay + 1
    return rows[:n]

#
# Generates the sequence of column indices that compose the
# spiral. Returns a sequence of n column indices
#
def cgen(n):
    cols = [0]
    stay = 2
    lim = 1

    while len(cols) < n:
        cols = cols + stay*[lim] #dostay(lim, stay)
        if lim > 0:
            newlim = -lim
        else:
            newlim = -(lim-1)
        cols = cols + transition(lim, newlim)
        lim = newlim
        stay = stay + 1
    return cols[:n]
#
# Generates the spiral. The spiral starts at pixel (r, c) and contains
# at most n elements. Only the elements that are contained in the
# rectangle
#
#  [0,rmax) x [0,cmax)
#
#  are retained so, if the spiral goes out of the bounds of the
#  rectangle, it might actually contain mess than n elements
#
#  Returns a list of coordinates that, read in order, describes the
#  spiral:
#
#  [(r, c), (r1, c1), ...., (rn, cn)]
#
#  The first element is always (r,c), the starting point that is
#  passed as a parameter.
#
def spiral(n, r, c, rmax, cmax):
    rows = rgen(n)
    cols = cgen(n)
    sp = [(i+r,j+c) for (i,j) in zip(rows, cols) if i+r >= 0 and j+c>=0 and i+r < rmax and j+c<cmax]
    return sp

#############################################################################
#############################################################################

#############################################################################
#
# TO-DO
# We-ll try this in class. There are some incompatibilities between
# the different versions of python that may cause the function
# read_bmp not to work. We-ll do a test in class and, if the versio
# you are using has a problem, the problem can be solved by
# uncommenting this function

def ord(x):
  return x

#############################################################################
#
#  image = read_bmp(file)
#
#  Reads a bmp (uncompressed bitmap) from a file and returns it as a
#  double array of pixels. If the image has r rows and c columns, then
#  "image" is a list of r lists with c elements each. The element
#  image[i][j] is the pixel in row number i and column number j.
#
#  Each one of these pixels is a three element touple containing three
#  integers in the range [0,255] corresponding to the values of the
#  three colors for that pixel. That is
#
#  image[i][j] = (r, g, b)
#
#  Are the values of the red, green, and blue component of pixel i, j.
#
#  This function is strongly limited: it works only with uncompressed,
#  24 bits per pixel images. It works for this exercize, but do not
#  attempt to use it in more general situations. Bad things will
#  happen.
#
def read_bmp(path):
    fp = open(path, "rb")
    # Read the interesting parts of the BMP header.
    fp.seek(2)
    buf = fp.read(4)
    fsize = ord(buf[0]) + 256*(ord(buf[1])+256*(ord(buf[2])+256*ord(buf[3])))
    fp.seek(10)
    buf = fp.read(4)
    offs = ord(buf[0]) + 256*(ord(buf[1])+256*(ord(buf[2])+256*ord(buf[3])))


    fp.seek(18)
    buf = fp.read(4)
    wdt = ord(buf[0]) + 256*(ord(buf[1])+256*(ord(buf[2])+256*ord(buf[3])))
    buf = fp.read(4)
    hgt = ord(buf[0]) + 256*(ord(buf[1])+256*(ord(buf[2])+256*ord(buf[3])))

    fp.seek(26)
    buf = fp.read(2)
    planes = ord(buf[0]) + 256*ord(buf[1])
    buf = fp.read(2)
    bpp = ord(buf[0]) + 256*ord(buf[1])

    print ("File size  : %d" % fsize)
    print ("Cols       : %d" % wdt)
    print ("Rows       : %d" % hgt)
    print ("Data Offs. : %d" % offs)
    print ("Planes     : %d" % planes)
    print ("bpp        : %d" % bpp)

    if 3*wdt % 4 != 0:      # bmp pads columns to have a length multiple of four
        pad = 4 - (3*wdt % 4)
        phlen = 3*wdt + pad
    else:
        phlen = 3*wdt


    fp.seek(offs)

    image = []

    for r in range(hgt):
        row = []
        buf = fp.read(phlen)
        if len(buf) != phlen:
            print ("Reading error: not enough bytes in row %d. Expected %d, found %d. Padding." % (r, phlen, len(buf)))
            buf = buf + phlen*[0]
            buf = buf[:phlen]
        for c in range(wdt):
            r =  ord(buf[2]) # bmp stores pixels as BGR
            g =  ord(buf[1])
            b =  ord(buf[0])
            buf = buf[3:]
            
            row = row + [(r, g, b)]
        image = [row] + image # bmp stores rows last-to-first

    fp.close()

    return image

#############################################################################
#
#  [r,c] = seed(img)
#
#  Returns the coordinates (r, c) of a point in the image that is
#  certainly a tumor
#
def seed(img):
    rows = len(img)
    cols = len(img[0])
    r = int(rows*0.35211)  # This is a bit of cheating: I place this in an area where I know there is a tumor
    c = int(cols*0.416)    # However, if I am wrong, the search will find it.
    sp = spiral(rows*cols, r, c, rows, cols)
    for k in range(len(sp)):
        r = sp[k][0]
        c = sp[k][1]
        if istumor(img[r][c]):
            return [r, c]
    return []



#############################################################################
#
#  These functions you are interested in: you will have to use them
#  for the implementation of your own function
#

#############################################################################
#
#  lst = neighbors(img, r, c)
#
#  returns a list of the coordinates of the neighbors of pixel
#  (r,c). The returned value is a list
#
#  lst = [(i1,j1), (i2,j2),....,(in,jn)]
#
#  that contains the coordinates of the pixels of the image that are
#  neighbors of pixel (r,c).
#  
def neighbors(img, r, c):
    rows = len(img)
    cols = len(img[0])
    lst1 = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]
    ngb = [ (r, c) for (r, c) in lst1 if r >=0 and c >=0 and r<rows and c<cols]
    return ngb


#############################################################################
#
#  val = istumor(pix)
#
#  Returns True if the pixel pix (which is a triple (r, b, g)) is part
#  of a tumor, returns False otherwise. It is geared to the image that
#  we are using: it returns True for reddish areas of the image, and
#  False for grayish ones
#
def istumor(pix):
    r = pix[0]
    g = pix[1]
    b = pix[2]
    return r > (b+g)/2 + 100
      

#############################################################################
#
# TO-DO
#
# Implement the mri_measure function. If you need to define auxiliary
# functions, these too must be placed in this section, after this
# comment.

#############################################################################
#
# size = mri_measure(img, r, c)
#
# Determines the size of a tumor in pixels. Receives an images in the
# form returned by read_bmp, and the coordinates of a pixel that is
# surely inside the tumor. Must run through the tumor using the
# algorithm explained in class and return the number of pixels found.
#
# This is the function that you have to implement for this lab.
#
###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 2
# Fichero: mri.py
# Autor: Laura Sánchez Garzón//Lidia Peña Morante
# Fecha: 01/11/2022
#
# Fichero auxiliar mri.py se ha competado adecuadamente para que funcione
# la función mri measure(img, r, c), la cual cuenta el número de píxeles, y los 
# imprime por pantalla 
# que contiene la imagen de un tumor cerebral (fichero mri-tumor 
# contiene la imagen de resonancia magnética)
# 
###############################################################
    
def mri_measure(image, r, c):
    Q=s.Stack()
    L=lstf.List()
    Q.push((r,c))
    
    while Q.empty() == False:
        (i,j)= Q.pop()
        L.insert_at_tail((i,j))
        n=neighbors(image,i,j)
        for (h,k) in n:
            if istumor(image[h][k])==True and L.buscar((h,k))==False:
                Q.push((h,k))
    return L.size
    
   


#############################################################################
#
#  This is the script. It loads an image, measures the tumor, and prints it
#
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("Usage: python mri.py <file>")
        sys.exit(1)
        
    image = read_bmp(sys.argv[1])
    [r, c] = seed(image)

    tumor_size = mri_measure(image, r, c)
    print (tumor_size)

# if __name__ == "__main__":
#     image=read_bmp("mri-tumor.bmp")
#     [r,c]=seed(image)
#     tumor_size=mri_measure(image,r,c)
#     print(tumor_size)