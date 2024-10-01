#!/usr/bin/python3
""" prints the pascal's triangle """


def pascal_triangle(n):
    """ prints pascal's triangle """
    if n <= 0:
        return []
    
    triangle = [[1]]

    for row in range(1, n):
        prev_row = triangle[row - 1]
        current_row = [1]

        for col in range(1, row):
            current_row.append(prev_row[col - 1] + prev_row[col])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
