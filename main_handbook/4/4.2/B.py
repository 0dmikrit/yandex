def make_matrix(size, value=0):
    if isinstance(size, int):
        width = height = size
    else:
        width, height = size
    matrix = []
    for i in range(height):
        row = [value] * width
        matrix.append(row)
    return matrix
