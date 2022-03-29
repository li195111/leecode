

def removeIslands(matrix):
    '''
    1 -> black pixels
    0 -> white pixels
    Remove All the black pixels
    that are not connected to the border of the image
    
    connected -> two pixels or two or more pixels 
    that are either horizontally or vertically adjacent
    兩個像素或兩個或多個水平或垂直相鄰的像素
    
    and if they are not connected to the border then
    you have to remove them
    we're going to call these blocks of black pixels
    that are not connected to the border we're going to call
    them islands
    '''
    print ("Input")
    for m in matrix:
        print (m)
    nrows = len(matrix)
    ncols = len(matrix[0])

    # border(mainland) =    row 0 and row (nrows-1)
    #                       col 0 and col (ncols-1)
    
    # for row(i) col(j)
    # pixels[i][j] need to consider 
    # connected to mainland = i==0 or i==(nrow-1), j==0 or j==(ncols-1)
    # connected mean pixels[i][j] => pixels[i+1][j], pixels[i-1][j], pixels[i][j+1], pixels[i][j-1] in mainland
    # so
    
    return []

if __name__ == "__main__":
    matrix = [
        [1,0,0,0,0,0],
        [0,1,0,1,1,1],
        [0,0,1,0,1,0],
        [1,1,0,0,1,0],
        [1,0,1,1,0,0],
        [1,0,0,0,0,1],
    ]
    '''
    # sample_output
    [
        [1,0,0,0,0,0],
        [0,0,0,1,1,1],
        [0,0,0,0,1,0],
        [1,1,0,0,1,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,1]
    ]
    # island_removed
    [
        [ , , , , , ],
        [ ,1, , , , ],
        [ , ,1, , , ],
        [ , , , , , ],
        [ , ,1,1, , ],
        [ , , , , , ],
    ]
    '''
    removeIslands(matrix)
    pass