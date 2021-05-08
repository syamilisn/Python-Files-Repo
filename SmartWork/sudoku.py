#Solving Sudoku
"""Method: Only recursion
Should have tried to implement backtracking"""
#Check if number is present in 3X3 cube
def compare(n,p,q):
    for i in range(p):
        for j in range(q):
            if sud[i][j] == n:
                return False
            else:
                return True
#Check if number is present in the same number's corresponding row & column           
def RowColChk(n,p,q):
    for i in range(9):
        if sud[p][i]==n:
            return False
    for j in range(9):
        if sud[j][q]==n:
            return False
    return True

def fun(n,i,j,p,q):
    val1=compare(n,p,q)
    if val1 == False:
        return False
    else:
        val2=RowColChk(n,i,j)
        if val2 == False:
            return False
        else:#place logic here
            return True    
#Passing the Sudoku puzzle question
sudque=[[2,0,0,0,0,3,0,0,0],
     [0,1,9,0,0,2,0,6,8],
     [0,0,0,0,0,7,0,0,5],
     [4,0,0,0,7,0,0,2,0],
     [0,7,0,1,0,9,0,3,0],
     [0,3,0,0,8,0,0,0,7],
     [8,0,0,2,0,0,0,0,0],
     [5,4,0,7,0,0,1,9,0],
     [0,0,0,5,0,0,0,0,3]]

#To print just the numbers
for i in range(9):
    for j in range(9):
        print(sudque[i][j],end=" \t")
    print("\n")
#or to print separating each row + commas inbw
for item in sudque:
    print(item,"\n")
sud=[[2,0,0,0,0,3,0,0,0],
     [0,1,9,0,0,2,0,6,8],
     [0,0,0,0,0,7,0,0,5],
     [4,0,0,0,7,0,0,2,0],
     [0,7,0,1,0,9,0,3,0],
     [0,3,0,0,8,0,0,0,7],
     [8,0,0,2,0,0,0,0,0],
     [5,4,0,7,0,0,1,9,0],
     [0,0,0,5,0,0,0,0,3]]
list=[1,2,3,4,5,6,7,8,9]
def playsudoku(sud):
    for i in range(9):
        for j in range(9):
            if sud[i][j] != 0:
                continue
            else:
                for n in list:
                    if i<3:
                        if j<3:
                            val3=fun(n,i,j,3,3)
                            if val3:
                                sud[i][j]=n
                        elif j<6:
                            val3=fun(n,i,j,3,6)
                            if val3:
                                sud[i][j]=n
                        elif j<9: 
                            val3=fun(n,i,j,3,9)
                            if val3:
                                sud[i][j]=n
                    elif i<6:
                        if j<3:
                            val3=fun(n,i,j,6,3)
                            if val3:
                                sud[i][j]=n
                        elif j<6:
                            val3=fun(n,i,j,6,6)
                            if val3:
                                sud[i][j]=n
                        elif j<9: 
                            val3=fun(n,i,j,6,9)
                            if val3:
                                sud[i][j]=n
                    elif i<9:
                        if j<3:
                            val3=fun(n,i,j,9,3)
                            if val3:
                                sud[i][j]=n
                        elif j<6:
                            val3=fun(n,i,j,9,6)
                            if val3:
                                sud[i][j]=n
                        elif j<9: 
                            val3=fun(n,i,j,9,9) 
                            if val3:
                                sud[i][j]=n

    for i in range(9):
        for j in range(9):
            print(sud[i][j],end="\t ")
        print("\n")
    print("____xxxx____")
    
    for i in range(9):
        for j in range(9):
            if sud[i][j]==0:
                sud=playsudoku(sud)
            elif sud[i][j]!=0:
                return sud

solved=playsudoku(sud) 
for item in sudque:
    print(item,"\n")
print("\n")
for item in sud:
    print(item,"\n")      