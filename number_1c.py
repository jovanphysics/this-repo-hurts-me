def factorial(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        a = 1
        for i in range(1, n+1):
            a *= i
        return a
def combination(n, r):
    if (n - r) < 0:
        return 0
    else:
        x = factorial(n)/(factorial(n - r) * factorial(r))
        return x
def stack(old, new):
    new_arr = old + new
    return new_arr
def create_zero_vector(N):
    return [0]*N
def create_zero_matrix(N):
    matrix = create_zero_vector(N)
    for i in range(N):
        matrix[i] = create_zero_vector(N)
    return matrix
def count_zeros(array, N):
    n_zeros = 0
    for i in range(N):
        if array[i] == 0:
            n_zeros += 1
    return n_zeros

N = int(input('Number: '))
arr = create_zero_matrix(N)
for i in range(N):
    for j in range(N):
        arr[i][j] = combination(i,j)
n_spaces = 0
for i in range(N):
    n_spaces = count_zeros(arr[i], N)/2
    if n_spaces % 2 != 0:
        n_spaces = n_spaces + 0.5
    for k in range(int(n_spaces)):
        print(" ", end=' ')
    for j in range(N):
        value = arr[i][j]
        if value == 0:
            continue
        else:
            print(int(value), end=' ')
        
            
    print()