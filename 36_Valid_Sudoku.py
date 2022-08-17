from typing import List

class Solution:
    def isValidSudoku(self,board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.
        Only the filled cells need to be validated according
        to the following rules:
            1. Each row must contain the digits 1-9 w/o repetition
            2. Each col must contain the digits 1-9 w/o repetition
            3. Each of the nine 3x3 sub-boxes of the grid must
                contain the digits 1-9 w/o repetition
        """
        def checkRows(b):
            #iterates through rows and runs checkVals
            for row in b:
                if not checkVals(row):
                    return False
            return True
        
        def checkCols(b):
            #iterates through cols and runs checkVals
            for col in list(zip(*b)):
                if not checkVals(col):
                    return False
            return True
        
        def checkBoxes(b):
            #loops over 0,3,6
            for i in (0,3,6):
                #loops over 0,3,6
                for j in (0,3,6):
                    #gets list of values of board squares
                    square = [b[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                    #run checkVals over squares
                    if not checkVals(square):
                        return False
            return True
        
        def checkVals(arr):
            #creates set
            valsSet = set()
            for val in arr:
                #if val isn't blank space on board
                if val != '.':
                    #if val is already in set, return false
                    if val in valsSet:
                        return False
                    #else, add val to set
                    else:
                        valsSet.add(val)
            return True
        #check rows, cols and boxes
        if checkRows(board) and checkCols(board) and checkBoxes(board):
            return True
        else:
            return False