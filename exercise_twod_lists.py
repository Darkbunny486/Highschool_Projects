#1
'''
def row (table, r):
    row = (table[r])
 '''  
#2
'''
def column (table, c):
    column = (table[c])
 '''   
#3
'''
def print_table (table):
    for a in range (len(table)):
        print (table[a])
 '''       
#4
'''
def five_eight ():
    my_list = []
    for a in range(8):
        my_list.append (1)
    table = [my_list]*5
print (table)
'''
#5
'''
def twoDList ():
    my_list = []
    table = []
    start = 1
    finsh = 3
    for b in range (3):
        for a in range (start, finsh+1):
            my_list.append (a)
        table.append (my_list)
        start += 3
        finsh += 3
        my_list = []
    
print (table)
'''
#6
''''
def flatten (Alist):
    my_list = []
    for a in range (len(Alist)):
        for b in range (len(Alist[a])):
            my_list.append (Alist[a][b])
    return my_list
print (flatten([["a", "b"], ["c", "d", "e"], ["f"]]))
'''
#7
'''
def swap_rows (table, r1, r2):
    Alist = table[r1]
    table[r1] = table[r2]
    table[r2] = Alist
    return table
print (swap_rows ([["a", "b"], ["c", "d", "e"], ["f"]], 2, 1))
'''
#8
'''
def swap_columns (table, c1, c2):
    for a in range (len(table)):
        n = table[a][c1]
        table[a][c1] = table[a][c2]
        table[a][c2] = n
    return table
print (swap_columns ([["a", "b"], ["c", "d", "e"], ["f","x"]], 0, 1))
'''
#9
'''
def matrix_dimensions (matrix):
    length = len(matrix)
    width = len(matrix[0])
    return length, width

def matrix_average (matrix):
    sume = 0
    count = 0
    for lists in martrix:
        for num in martrix[lists]:
            sume += num
            count += 1
    average = sume/count
    return average

def matrix_sum(matrix1, matrix2):
    matrix = []
    matrixsum = []
    len1, wid1 = matrix_dimensions (matrix1)
    len2, wid2 = matrix_dimensions (matrix2)
    half = wid1/2
    if (len1 == len2) and (wid1 == wid2):
        for a in range (len1):
            for b in range (wid1):
                matrix.append (matrix1[a][b] + matrix2[a][b])
                if (b >= half):
                    matrixsum.append (matrix)
                    matrix= []
    print (matrixsum)
   
matrix_sum([[1, 2, 3,], [4, 5, 6]], [[1, 2, 3,], [4, 5, 6]])

def matrix_transposed (matrix):
    for a in range (len(matrix)):
        for b in range (len(matrix[0])):
            something = matrix[b][a]
            matrix[a][b] = matrix[b][a]
            matrix[b][a] = something
            print (something)
    return matrix

print(matrix_transposed ([[1, -3, -1], [2, 9, -2], [4, 7, -4]]))
'''












 
