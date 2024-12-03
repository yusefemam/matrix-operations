def input_matrix(rows, cols, label):
    return [[int(input(f"Enter {label} [{i + 1},{j + 1}]: ")) for j in range(cols)] for i in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def add_matrix(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def multiply_matrix(matrix1, matrix2):
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]


def main():
    if input("Operate on (one/multiple) matrices? ").strip().lower() == "one":
        rows, cols = int(input("Rows: ")), int(input("Columns: "))
        matrix = input_matrix(rows, cols, "matrix")
        if (op := input("Operation (add/multiply): ").strip().lower()) == "add":
            print("Result:")
            print_matrix(add_matrix(matrix, matrix))
        elif op == "multiply":
            print("Result:")
            print_matrix(multiply_matrix(matrix, matrix))
        else:
            print("Invalid operation.")
    else:
        matrices = [
            input_matrix(int(input(f"Rows for matrix {i + 1}: ")), int(input(f"Columns for matrix {i + 1}: ")), f"matrix {i + 1}")
            for i in range(int(input("Number of matrices: ")))
        ]
        if (op := input("Operation (add/multiply): ").strip().lower()) == "add":
            if all(len(m) == len(matrices[0]) and len(m[0]) == len(matrices[0][0]) for m in matrices):
                result = matrices[0]
                for m in matrices[1:]:
                    result = add_matrix(result, m)
                print("Result:")
                print_matrix(result)
            else:
                print("Matrices must have the same dimensions.")
        elif op == "multiply" and len(matrices) == 2 and len(matrices[0][0]) == len(matrices[1]):
            print("Result:")
            print_matrix(multiply_matrix(matrices[0], matrices[1]))
        else:
            print("Invalid operation or incompatible dimensions.")

main()
