def diagonal_sum(matrix):
    total = 0
    for row_index, row in enumerate(matrix):
        col_index = row_index
        print(col_index, row_index)
        total += row[col_index]
    return total



    # return sum(matrix[0,2], matrix[1,1], matrix[2,0])



myList2D= [[1,2,3],[4,5,6],[7,8,9]]

print(diagonal_sum(myList2D)) # 15