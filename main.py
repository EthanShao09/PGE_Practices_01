# ( Part of BE5B33PGE course, FEL CTU, 2023 )


# --------------------------------------------------------------------
#     1D/2D   list/array problems  to upload
# --------------------------------------------------------------------



# Task 01
# Lists A and B of integers are in the input, each on a separate line.
# For each list, print the number of items in it which value is smaller than the
# value of the first item in the list. Print the results on separate lines.

def task01(List1, List2):
    print(len([x for x in List1 if x < List1[0]]))
    print(len([x for x in List2 if x < List2[0]]))




# Task 02

# Lists A and B of integers are in the input, each on a separate line.
# Check if in each of the lists the following holds:
# The number of leading values 0 is equal to the number of trailing values 0.
# Print True or False accordingly on a separate line.

def task02(list):
    flag1 = 0
    flag2 = 0
    for i in list:
        if i == 0:
            flag1 += 1
        else:
            break
    for j in list[::-1]:
        if j == 0:
            flag2 += 1
        else:
            break
    print(flag1 == flag2)




# ------------------------------------------
# Task 03

# Lists A and B of integers are in the input, each on a separate line.
# Task: Substitute all occurrences of maximum in B by minimum of value of A.
# Print modified B. Print only values separated by single spaces.
def task03(list1, list2):
    a = min(list1)
    b = max(list2)
    for i in range(len(list2)):
         if list2[i] == b:
            list2[i] = a
    print(list2)







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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if taskNo == 1:
        task01(list1, list2)

    if taskNo == 2:
        task02(list1)
        task02(list2)

    if taskNo == 3:
        task03(list1, list2)

    if taskNo == 4:
        task04(list1)
        task04(list2)

    if taskNo == 5:
        task05(matrix)

    if taskNo == 6:
        task06(matrix)