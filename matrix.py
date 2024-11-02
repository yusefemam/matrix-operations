def input_matrix(rows, cols, matrix_num):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(
                input(f"Enter value for element at {matrix_num} row {i + 1}, column {j + 1}: "))
            row.append(value)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()


def add_matrix(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def subtract_matrix(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def multiply_matrix(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def main():
    operation_choice = input(
        "Do you want to perform operations on one matrix or multiple matrices? (one/multiple): ").strip().lower()

    if operation_choice == "one":
        rows = int(input("Enter the number of rows for the matrix: "))
        cols = int(input("Enter the number of columns for the matrix: "))
        matrix = input_matrix(rows, cols, "matrix")

        operation = input(
            "Which operation would you like to perform? (add, subtract, multiply): ").strip().lower()

        if operation == "add":
            result = add_matrix(matrix, matrix)
            print("Result of addition (adding the matrix to itself):")
            print_matrix(result)

        elif operation == "subtract":
            result = subtract_matrix(matrix, matrix)
            print("Result of subtraction (subtracting the matrix from itself):")
            print_matrix(result)

        elif operation == "multiply":
            result = multiply_matrix(matrix, matrix)
            print("Result of multiplication (multiplying the matrix by itself):")
            print_matrix(result)

        else:
            print("Invalid operation. Please choose add, subtract, or multiply.")

    elif operation_choice == "multiple":
        num_matrices = int(input("How many matrices do you want to input? "))
        matrices = []

        for i in range(num_matrices):
            rows = int(input(f"Enter the number of rows for matrix {i + 1}: "))
            cols = int(
                input(f"Enter the number of columns for matrix {i + 1}: "))
            matrix = input_matrix(rows, cols, f"matrix {i + 1}")
            matrices.append(matrix)

        operation = input(
            "Which operation would you like to perform? (add, subtract, multiply): ").strip().lower()

        if operation == "add":
            if all(len(matrix) == len(matrices[0]) and len(matrix[0]) == len(matrices[0][0]) for matrix in matrices):
                result = matrices[0]
                for matrix in matrices[1:]:
                    result = add_matrix(result, matrix)
                print("Result of addition:")
                print_matrix(result)
            else:
                print("All matrices must have the same dimensions for addition.")

        elif operation == "subtract":
            if all(len(matrix) == len(matrices[0]) and len(matrix[0]) == len(matrices[0][0]) for matrix in matrices):
                result = matrices[0]
                for matrix in matrices[1:]:
                    result = subtract_matrix(result, matrix)
                print("Result of subtraction:")
                print_matrix(result)
            else:
                print("All matrices must have the same dimensions for subtraction.")

        elif operation == "multiply":
            if len(matrices) == 2 and len(matrices[0][0]) == len(matrices[1]):
                result = multiply_matrix(matrices[0], matrices[1])
                print("Result of multiplication:")
                print_matrix(result)
            else:
                print(
                    "To multiply matrices, the number of columns in the first must equal the number of rows in the second.")

        else:
            print("Invalid operation. Please choose add, subtract, or multiply.")

    else:
        print("Invalid choice. Please choose one or multiple.")


main()
