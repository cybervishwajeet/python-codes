#code by vishwa

def generate_pascals_triangle(level):
    triangle = []
    for i in range(level):
        row = [None] * (i + 1)
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1])*6))
level = 5
triangle = generate_pascals_triangle(level)
print_pascals_triangle(triangle)
