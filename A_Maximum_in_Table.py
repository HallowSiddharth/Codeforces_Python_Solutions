n=int(input())
tab=[[0 for i in range(n)] for i in range(n)]
tab[0]=[1 for i in range(n)]
for i in tab:
    i[0]=1
for i in range(1,n):
    for j in range(1,n):
        tab[i][j]=tab[i-1][j]+tab[i][j-1]
print(tab[n-1][n-1])