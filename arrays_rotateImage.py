"""
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
"""
def rotateImage(a):
    a_mat = zip(*a)
    return_mat = list()
    for row in a_mat:
        return_mat.append(row[::-1])
    return return_mat
