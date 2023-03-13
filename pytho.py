# Gauss Jordan Program
def reduce_echlon(func):
    def identity():
        func()
        r=len(matrix)
        while r>0:
            pr=int(input("Enter Pivot row"))
            pc=int(input("Enter Pivot Column"))
            pr-=1
            pc-=1
            pe=matrix[pr][pc]
            for i in range(0,NC):
                matrix[pr][i]=matrix[pr][i]/pe
            for m in range(0,NR):
                if m==pr:
                    continue
                makezero=matrix[m][pc]
                for n in range(0,NC):
                    matrix[m][n]=matrix[m][n]-(makezero*matrix[pr][n])
            func()        
                    
            r-=1    
    return identity        
# input matrix
def inp_matrix(m,n):
    global matrix
    matrix=[]
    for i in range(0,m):
        output=[]
        for j in range(0,n):
            num=int(input(f"Enter O[{i}][{j}]: "))
            output.append(num)
        matrix.append(output)
    return matrix                
NR=int(input("Enter number of rows: "))
NC=int(input("Enter number of columns: "))       
print(inp_matrix(NR,NC))    
@reduce_echlon
def disp_matrix():
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            print("%8.2f"%matrix[i][j],end="\t")
        print()
disp_matrix()
print("--------------------------------------------------")















    
