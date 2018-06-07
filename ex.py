import random

table = []
arr = []
i_main = 0
j_main = 0

#initialising the sudoku with zeroes
for j in range(9):
    column = []
    for i in range(9):
        column.append(0)
    table.append(column)
	
#printing the sudoku
def printTable():
    for i in table:
        print (i)
    
def rowCheck(row, col):
    for i in range(row):
        j=col
        if (table[i][j] in arr):
            arr.remove(table[i][j]) 
    
def colCheck(row, col): 
    for t in range(col):
        p=row
        if (table[p][t] in arr):
            arr.remove(table[p][t])
                    
def blockCheck(row, col):
    num = 3*(row%3) + col%3
    print "num " + str(num)
    for i in range(row-row%3,row-row%3 + 3):
        for j in range(col-col%3,col-col%3 + 3):
            if (num == 0):
                return
            if (table[i][j] in arr):
                arr.remove(table[i][j])
            num = num - 1

		
def check(row,col):

    globals()['arr'] = [1,2,3,4,5,6,7,8,9]
    rowCheck(row, col)
    colCheck(row, col)
    blockCheck(row, col)	
	


while (i_main < 9):
    j_main = 0
    while(j_main < 9):

        print ("i_main " + str(i_main) + " j_main " + str(j_main))
        check(i_main,j_main)
        print arr

        if (len(arr) == 0):
            table[i_main][j_main] = 0
            table[i_main][j_main-1] = 0
            table[i_main][j_main-2] = 0
            j_main -= 3

        else:
            table[i_main][j_main] = random.choice(arr)
        
        printTable()
        print('\n')

        j_main += 1

    i_main += 1
                 
printTable()
