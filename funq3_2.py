# Write a function that takes an integer n and returns the n-th level of Pascal's triangle.
#code by Vedant Kale H3
def pascals_triangle(level):
    triangle = [[1]]
    for i in range(1, level):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))
level = 5
triangle = pascals_triangle(level)
print_pascals_triangle(triangle)