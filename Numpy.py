import numpy as np
#1d array
a=np.array([6,7,8])
print("1d array:",a)
#2d array
b=np.array([[5,6,7],[4,5,8]])
print("2d array:",b)
#3d array
c=np.array([[[4,3,2],[5,6,7],[3,4,2]]])
print("3d array:",c)

#to get no. of dimensions
print(a.ndim)
print(b.ndim)
print(c.ndim)

#get shape
print(a.shape)
print(b.shape)
print(c.shape)

#get data type
print(a.dtype)
print(b.dtype)
print(c.dtype)

#we can explicitly change the type of data
d=np.array([6,9,8],dtype="int16")
print(d.dtype)

#get item size
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)
print(d.itemsize)

#get total size
print(a.nbytes)
print(b.nbytes)
print(c.nbytes)
print(d.nbytes)

#ACCESSING/CHANGING SPECIFIC ELEMENTS,ROWS,COLUMNS ,ETC

#for 2d array
e=np.array([[6,7,8,4,5,3,2],[11,12,13,14,15,16,17]])

#get a specific element [r,c]
print(e[1,3]) #indexing starts from 0 
print(e[1,-4])

#get a specific row
print(e[1,:])

#get a specific column
print(e[:,4])

#getting a little more fancy [startindex:endindex:stepsize]
print(e[0,1:6:2])

#to change specific element
e[1,3]=11
print(e)

e[:,2]=[11,12]
print(e)

#for 3d array
f=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,12,13]]])
print(f)
print(f.ndim)

#get a specific element (work outside in)
print(f[1,1,0])
print(f[:,1,:])

#replace
f[1,1,0]=12
f[:,1,:]=[[22,33,55],[55,44,22]]
print(f)

#INITIALIZING DIFFERENT TYPES OF ARRAYS
#all zeroes matrix
print(np.zeros(3))
print(np.zeros((3,4)))
print(np.zeros(((3,2,1))))

#all ones matrix
print(np.ones(5))
print(np.ones((8,9)))
print(np.ones(((6,7,4))))

#any another number np.full((shape),value)
print(np.full((2,3),4))
#print(np.full(((2,3,5))),4)

#any other number (full_like) (we mention the array whose size you want)
print(np.full_like(b,5))

#random decimal number
print(np.random.rand(4,2))
print(np.random.random_sample(b.shape))

#random integer values  (low,high(optional),size(optional),dtype="l"(optional))
print(np.random.randint(4,8,size=(6,4)))

#identity matrix (create only square matrix)
print(np.identity(6))

#eye matrix ( it also create identity matrix) (no.of rows,no.of columns(optional),index of diagonal to set 1(optional))
print("eye=" , np.eye(4,5))

#used to create arrays with evenly spaced values (start(optional),stop,step(optional),dtype(optional))
print(np.arange(5, 25, 5))

#takes the number of samples as an argument and numpy calculates the appropriate step size
print(np.linspace(0, 1, 6))

#repeat an array multiple times
print(np.repeat(a,4))

#for multi-dimensional arrays , you can specify axis
print(np.repeat(c,4,axis=0))

#QUESTION
q=np.ones((5,5))
print(q)
z=np.zeros((3,3))
z[1,1]=9
print(z)
q[1:4,1:4]=z
print(q)  

#be carefull when copying an array

a=b
b[0]=99
print(b)
print(a)
#here changes done in b will also reflect on a that means both a and b are pointing to the same array

#to avoid this error we use .copy()
a1=np.ones((3,4))
b1=a1.copy()
b1[0]=11
print("b1= ",b1)
print("a1= ",a1)

##MATHEMATICS
print(a1+2)
print(a1-2)
print(a1*2)
print(a1/2)
print(a1//2)
print(a1%2)
print(a1**2)
print(np.sin(a1))
print(np.tan(a1))
print(np.cos(a1))

##LINEAR ALGEBRA
n1=np.ones([2,3])
n2=np.full([3,2],3)
#print(n1*n2) will give an error as matrices sizes are different
print(np.matmul(n1,n2))

#TO FIND THE DETERMINANT
i=np.identity(4)
print(np.linalg.det(i))

# TO FIND THE TRACE(sum of diagonal elements)
print(np.trace(i))

#TO FIND INVERSE OF A MATRIX
print(np.linalg.inv(i))

#TO FIND EIGENVALUES AND EIGENVECTORS
print(np.linalg.eig(i))

#TO FIND SINGULAR VALUE DECOMPOSITION
print(np.linalg.svd(i))

#STATISTICS

stats=np.array([[6,7,8],[2,3,4]])
print("Mean:", np.mean(stats))
print("Std Dev:", np.std(stats))
print(np.min(stats)) # we can also write the axis
print(np.max(stats))
print(np.sum(stats))

#REORGANIZING ARRAY

before=np.array([[33,44,55,43],[100,66,77,88]])
print(before)
after=before.reshape(4,2)
print(after)

#VERTICALLY STACKING VECTORS
after1=np.ones([2,4])
print(np.vstack([before,after1]))

#HORIZONTALLY STACKING VECTORS
print(np.hstack([before,after1]))

#MISCELLANIOUS

#load data from file

filedata=np.genfromtxt('data.txt' , delimiter=',')
print("filedata=",filedata)
filedata=filedata.astype("int32")
print("astype=",filedata)

#BOOLEAN MASKING AND ADVANCED INDEXING

print(filedata>50)
print((filedata>50) & (filedata>30))

#Challenge Problems (Try These Yourself)

# A. Create a 3x3 identity matrix
print("identity matrix of 3x3= ",np.identity(3))

# B. Replace odd numbers in array with -1
A=np.arange(10)
A[A%2==1]=-1
print(A)

#C. Create a 5x5 matrix with values from 1 to 25, reverse rows
B=np.arange(1,26).reshape((5,5))
B[::-1]
print(B)

# D. Sort a random array of 10 integers
print(np.sort(np.random.randint(1,100,size=10)))


