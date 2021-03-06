import numpy as np
import sys

# Reading number of unknowns
n = int(input('Enter number of unknowns: '))

# Making array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = np.zeros((n,n+1))

# Making array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)
pivots=np.zeros(n)     #to store pivot choosen for each column 

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))


# Applying Gauss Elimination which is no longer gauss elination as we are 
# not interested in row echlon form
# I have not done any exchanges,saving computation,but its still too much.
for j in range(n):    #Going through columns
    max_quality=-1
    pivot_i=0
# Pivot selection and Scaling before operation in each column    
#I have defined a quality function for a candidate pivot,
#element with max quality will be our pivot          
    for i in range(n):  #Pre-scanning entire column for selecting pivot
                        #But here in each column we are scanning corresponding entire row,i.e entire matrix:)
        if((np.abs(a[i][j])/max(np.abs(a[i])))>=max_quality): #Checking Quality of (i,j)
           max_quality=np.abs(a[i][j])/max(np.abs(a[i]))
           if(i not in pivots):  #previously chosen pivot should not be affected,that's why
               pivot_i=i
    pivots[j]=pivot_i       #pivot[j] is equal to pivot chosen in jth_column
#The above part for numerical stability(n^2) 

#Now row operations to make zeros by using pivot in the current column
    for i in range(n):
       if(i!=pivots[j]):  #Dont perform operation on the pivot row itself
           ratio = a[i][j]/a[pivot_i][j]      #element/pivot
        
           for k in range(n+1):  
                a[i][k] = a[i][k] - ratio * a[pivot_i][k]
#All eliminations Cost(n^2)
#Total time complexity=(n^2+n^2)*n=n^3
#Now after finishing previous step, every pivot choosen will be non-zero and rest 0
#Storing answers,kind of  back_substitution with only one variable left 
for j in range(n):      #Every column has an answer ready for us
    x[j]=a[int(pivots[j])][n]/a[int(pivots[j])][j]    #bi/aij


# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.12g' %((i+1),x[i]), end = '\t')
#Note:
#Scaling and good pivoting are two seperate options,but the quality function relates two.


