
def countBoats():
    n,m = map(int, input().split())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))



    count = 0

    #counts for rows 
    for r in mat:
        i = 0
        while i < m-1:
            j = i+1
            if r[i] == 1 and r[j] == 1:
                while j < m and r[j] == 1:
                    j += 1
                count += 1
            i = j

    #count for columns
    for col in range(len(mat[0])):
        i = 0
        while i < n-1:
            j = i + 1
            if mat[i][col] == 1 and mat[j][col] == 1:
                while j < n and mat[j][col] == 1:
                    j +=1
                count += 1
            i = j
    
    print(count)


    

countBoats()         



    






    

