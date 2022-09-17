n = 6
arr = []
for i in range(n):
    arr.append(list(map(int, input().split()[:n])))
    
def sum_glass(m, i, j):
    """Assumes hour-glass is in bounds of m!"""
    return sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])

pattern = float("-inf")
for i in range(4):
    for j in range(4):
        s = sum_glass(arr, i, j)
        if s > pattern:
            pattern = s
            
print (pattern)