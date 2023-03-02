# PGE_Practices_01

Part of BE5B33PGE course, FEL CTU, 2023
1D/2D   list/array problems  to upload


Each program you submit to the evaluation system will be capable
of solving more than one task. Each time your program is run,
it prints the solution of  only one task.  
The first line of input always specifies the task that is to be performed.


To solve any of the tasks 02 to 06 below do the following

   1. Define a function which takes the input list or lists as a parameter(s)
      and which solves the problem and prints the demanded output.
      
   2. Put that function in this file, the same way it is done for task01 below.
      Note, that each input data are preceded by a single line containing
      the number of the task these data are rleted to. Your program has to read
      the number of the task and apply the according function.
   
   3. Name the file main.py, zip it (any zip file name is ok)  
      and upload it to brute evaluation system.
      

 
------------------------------------------
Task 01
 
Lists A and B of integers are in the input, each on a separate line.
For each list, print the number of items in it which value is smaller than the
value of the first item in the list. Print the results on separate lines.

def task01( List1, List2 ):
    print( len( [x for x in List1 if x < List1[0]] ) )
    print( len( [x for x in List2 if x < List2[0]] ) )
 
'''
Example1:
Input
1
6 5 4 3 7 8 9
0 -1 -2 -3 -4 2 2 -1 -1 
Output
3
6
 
Example2:
Input
1
3 0 1 0 4 2
-2 0 2 4 6 8
Output
4 
0
 
 
Example solution:
def task01( List1, List2 ):
    print( len( [x for x in List1 if x < List1[0]] ) )
    print( len( [x for x in List2 if x < List2[0]] ) )
 
'''
 
 
------------------------------------------
 Task 02 
Lists A and B of integers are in the input, each on a separate line.
Check if in each of the lists the following holds:
The number of leading values 0 is equal to the number of trailing values 0.
Print True or False accordingly on a separate line.
 
'''
Example:
Input
2
0 0 0 2 3 0 0 4 5 6 0 0
0 10 11 12 22 0 
Output
False
True
'''
 
 
 
# ------------------------------------------
# Task 03
Lists A and B of integers are in the input, each on a separate line.
Task: Substitute all occurrences of maximum in B by minimum of value of A.
Print modified B. Print only values separated by single spaces.
 
'''
Example:
Input
3
2 3 4 5 2 3 4 5 2 3 4 5
55 20 33 11 55 33 11 33 44 44 55
Output
2 20 33 11 2 33 11 33 44 44 2
'''
 
 
 
# ------------------------------------------
# Task 04 
 
Lists A and B of integers are in the input, each on a separate line.
For each list, find minimum of all values which appear in list exactly twice.
Print the minimum on a separate line.
If no value appears twice in the list print string None.
'''
Example:
Input
4
11 20 33 11 20 33 11 33 44 44 55
2 3 4 5 2 3 4 5 2 3 4 5
Output
20
None
'''
 
 
# ------------------------------------------
# Task 05    
 
The input contains the size (dimension) S of a square matrix of integers,
each of the next S lines contains one row of the matrix.
The items on a line are separated by single spaces.
Shrink the size of the matrix by 2:
Remove the first and the next row of the matrix
and the first and the last column  of the matrix.
print the resulting matrix in the same format as in the input.
'''
Example:
Input
5
6
1 1 1 1 1 1 
1 2 3 2 3 1
1 3 2 3 2 1
1 2 3 2 3 1
1 3 2 3 2 1
1 1 1 1 1 1 
Output
2 3 2 3
3 2 3 2
2 3 2 3
3 2 3 2
'''
 
 
# ------------------------------------------
# Task 06    
 
The input contains the size (dimension) S of a square matrix of integers,
each of the next S lines contains one row of the matrix.
The items on a line are separated by single spaces.
Exchange the contents of the diagonals of the matrix.
The items on the diagonals will stay in the same row,
but in each row, the item X in the main diagonal will be exchanged with the
item Y in the secondary diagonal (antidiagonal) in the same row.
 
'''
Example:
Input
6
5
1 0 0 0 2
0 1 0 2 0
0 0 3 0 0
0 2 0 1 0
2 0 0 0 1
Output
2 0 0 0 1
0 2 0 1 0
0 0 3 0 0
0 1 0 2 0
1 0 0 0 2
'''
 
 
 
 
 
 
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#               I N P U T    R E A D I N G
taskNo = int( input() )
if taskNo in [1,2,3,4]:
    list1 = list( map( int, input().split() ) )
    list2 = list( map( int, input().split() ) )
if taskNo in [5,6]:
    matrixSize = int(input())
    matrix = []
    for i in range( matrixSize ):
        row = list(map(int, input().split()))
        matrix.append( row )
 
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             P R O C E S S I N G
 
if taskNo == 1:
    task01( list1, list2 )
 
if taskNo == 2:
    task02( list1 )
    task02( list2 )
 
if taskNo == 3:
    task03( list1, list2 )
 
if taskNo == 4:
    task04( list1 )
    task04( list2 )
 
if taskNo == 5:
    task05( matrix )
 
if taskNo == 6:
    task06( matrix )
