#Make a choice bases program where you can add and subtract two matrices by taking matrices and operation as a user input 
import numpy as np 

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter the elements of matrix A row by row:")
matrix_a = []
for i in range(rows): 
    row = list(map(int, input(f"Row {i + 1} (space-separated): ").split()))  #used help online --> dont understand at all
    matrix_a.append(row)

print("Enter the elements of matrix B row by row:")
matrix_b = []
for i in range(rows):
    row = list(map(int, input(f"Row {i + 1} (space-separated): ").split()))
    matrix_b.append(row)

print("Choose an operation:")
print("\n 1. Add matrices \n 2.Subtract \n 3.Multiply \n 4.Divide \n")
choice = input("Enter your choice (1,2,3 or 4): ")

result = []
if choice == "1":
    for i in range(rows):
        result_row = []
        for j in range(cols):
            result_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(result_row)
elif choice == "2":
    for i in range(rows):
        result_row = []
        for j in range(cols):
            result_row.append(matrix_a[i][j] - matrix_b[i][j])
        result.append(result_row)
elif choice == "3":
    for i in range(rows):
        result_row = []
        for j in range(cols):
            result_row.append(matrix_a[i][j] * matrix_b[i][j])
        result.append(result_row)
elif choice =="4":
    for i in range(rows):
        result_row = []
        for j in range(cols):
            result_row.append(matrix_a[i][j] // matrix_b[i][j])
        result.append(result_row)

else:
    print("Invalid choice!")
    exit() 

print("Result:")
for row in result:
    print(" ".join(map(str, row)))