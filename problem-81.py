def printAllPathsUtil(mat, i, j, m, n, path, pi, dic): 
  
    # Reached the bottom of the matrix  
    # so we are left with only option to move right 
    if (i == m - 1): 
        for k in range(j, n): 
            path[pi + k - j] = mat[i][k] 
        
        dic[sum(path[:-1])] = path[:-1]
        return
  
    # Reached the right corner of the matrix  
    # we are left with only the downward movement. 
    if (j == n - 1): 
  
        for k in range(i, m): 
            path[pi + k - i] = mat[k][j] 
  
        dic[sum(path[:-1])] = path[:-1]
        return
  
    path[pi] = mat[i][j] 
  
    printAllPathsUtil(mat, i + 1, j, m, n, path, pi + 1, dic) 
  
    printAllPathsUtil(mat, i, j + 1, m, n, path, pi + 1, dic) 

  
def printAllPaths(mat, m, n): 
    
    dic = {}
    path = [0 for i in range(m + n)] 
    printAllPathsUtil(mat, 0, 0, m, n, path, 0, dic) 

    return dic
  
  
#printAllPaths(mat, 2, 3)     

with open('p081_matrix.txt', 'r') as txt:
    matrix = txt.readlines()
    
mat = matrix
new_list = []

for i in mat:
    i = i.split('\n')[0]
    m = [int(j) for j in i.split(',')]
    new_list.append(m)
    
# dic = printAllPaths(new_list, len(new_list), len(new_list[0]))
# arr = [
#     [1,2,3,4],
#     [2,3,4,5],
#     [4,5,7,8],
#     [5,6,8,9]
# ]

dic = printAllPaths(arr, len(arr), len(arr[0]))
print(dic)
print('Here', min(dic.keys()))
