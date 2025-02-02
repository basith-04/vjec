def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} values separated by space: ").split()))
        matrix.append(row)
    
    return matrix

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

matrix = input_matrix()
print("\nOriginal Matrix:")
print_matrix(matrix)

transposed = transpose_matrix(matrix)
print("\nTranspose of the Matrix:")
print_matrix(transposed)
