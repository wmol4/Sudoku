assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    dual_values = [box for box in values.keys() if len(values[box]) == 2]
    for box in dual_values:
        #check rows for equivalent boxes
        for row_boxes in row_dict[box]:
            if values[row_boxes] == values[box]:

                try:
                    digit_1 = values[box][0]
                    digit_2 = values[box][1]
                except:
                    pass
                
                modified_row = list(row_dict[box])
                modified_row.remove(row_boxes) #we do not want to remove the values from naked twins
                for modified in modified_row:
                    if len(values[modified]) == 1:
                        modified_row.remove(modified)
                
                for row_boxes_2 in modified_row:
                    #modify row_boxes_2 but do not modify row_boxes
                    try:
                        values[row_boxes_2] = values[row_boxes_2].replace(digit_1,'')
                    except:
                        pass
                    try:
                        values[row_boxes_2] = values[row_boxes_2].replace(digit_2,'')
                    except:
                        pass


        #now check columns
        for column_boxes in column_dict[box]:
            if values[column_boxes] == values[box]:

                try:
                    digit_1 = values[box][0]
                    digit_2 = values[box][1]
                except:
                    pass
                
                modified_column = list(column_dict[box])
                modified_column.remove(column_boxes) #we do not want to remove the values from naked twins
                for modified in modified_column:
                    if len(values[modified]) == 1:
                        modified_column.remove(modified)                
                
                for column_boxes_2 in modified_column:
                    #modify row_boxes_2 but do not modify column_boxes
                    try:
                        values[column_boxes_2] = values[column_boxes_2].replace(digit_1,'')
                    except:
                        pass
                    try:
                        values[column_boxes_2] = values[column_boxes_2].replace(digit_2,'')
                    except:
                        pass

       
        #now check 3x3 squares
        for square_boxes in square_dict[box]:
            if values[square_boxes] == values[box]:

                try:
                    digit_1 = values[box][0]
                    digit_2 = values[box][1]
                except:
                    pass
                
                modified_square = list(square_dict[box])
                modified_square.remove(square_boxes) #we do not want to remove the values from naked twins
                for modified in modified_square:
                    if len(values[modified]) == 1:
                        modified_square.remove(modified)                
                
                for square_boxes_2 in modified_square:
                    #modify row_boxes_2 but do not modify square_boxes
                    try:
                        values[square_boxes_2] = values[square_boxes_2].replace(digit_1,'')
                    except:
                        pass
                    try:
                        values[square_boxes_2] = values[square_boxes_2].replace(digit_2,'')
                    except:
                        pass

                    
        #finally check diagonals
        try:
            for diagonal_boxes in diagonal_dict[box]:
                if values[diagonal_boxes] == values[box]:
    
                    try:
                        digit_1 = values[box][0]
                        digit_2 = values[box][1]
                    except:
                        pass
                    
                    modified_diagonal = list(diagonal_dict[box])
                    modified_diagonal.remove(diagonal_boxes) #we do not want to remove the values from naked twins
                    for modified in modified_diagonal:
                        if len(values[modified]) == 1:
                            modified_diagonal.remove(modified)                 
                    
                    for diagonal_boxes_2 in modified_diagonal:
                        #modify row_boxes_2 but do not modify diagonal_boxes
                        try:
                            values[diagonal_boxes_2] = values[diagonal_boxes_2].replace(digit_1,'')
                        except:
                            pass
                        try:
                            values[diagonal_boxes_2] = values[diagonal_boxes_2].replace(digit_2,'')
                        except:
                            pass
        except:
            pass

    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    boxes = []
    for s in A:
        for t in B:
            boxes.append(s+t)
    return boxes

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
row_dict = dict()
for s in boxes:
    for row in row_units:
        if s in row:
            row_modified = list(row)
            row_modified.remove(s)
            row_dict[s] = row_modified

column_units = [cross(rows, c) for c in cols]
column_dict = dict()
for s in boxes:
    for column in column_units:
        if s in column:
            column_modified = list(column)
            column_modified.remove(s)
            column_dict[s] = column_modified

square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
square_dict = dict()
for s in boxes:
    for square in square_units:
        if s in square:
            square_modified = list(square)
            square_modified.remove(s)
            square_dict[s] = square_modified

diagonal_units = [['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'], ['I1', 'H2', 'G3', 
                  'F4', 'E5', 'D6', 'C7', 'B8', 'A9']]
diagonal_dict = dict()
for s in boxes:
    for diagonal in diagonal_units:
        if s in diagonal:
            diagonal_modified = list(diagonal)
            diagonal_modified.remove(s)
            diagonal_dict[s] = diagonal_modified

#unitlist = row_units + column_units + square_units
unitlist_diag = row_units + column_units + square_units + diagonal_units

#for non-diagonal versions of sudoku
#units = dict()
#for s in boxes:
#    units[s] = []
#    for u in unitlist:
#        if s in u:
#            units[s].append(u)
            
units_diag = dict()
for s in boxes:
    units_diag[s] = []
    for u in unitlist_diag:
        if s in u:
            units_diag[s].append(u)

#for non-diagonal versions of sudoku
#peers = dict()
#for s in boxes:
#    peer_list = []
#    for i in units[s]:
#        for j in i:
#            if j not in peer_list and j != s:
#                peer_list.append(j)
#    peers[s] = peer_list
    
peers_diag = dict()
for s in boxes:
    peer_list = []
    for i in units_diag[s]:
        for j in i:
            if j not in peer_list and j != s:
                peer_list.append(j)
    peers_diag[s] = peer_list

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = []
    all_values = '123456789'
    
    for c in grid:
        if c == '.':
            values.append(all_values)
            
        elif c in all_values:
            values.append(c)
            
    return dict(zip(boxes, values))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': 
            print(line)
    return

def eliminate(values):
    """
    Look through the peers and adjust the values i the 'values' dictionary
    """    
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers_diag[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values):
    
    for unit in unitlist_diag:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Naked Twins Strategy
        values = naked_twins(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    puzzle = grid_values(grid)
    puzzle_searched = search(puzzle)
    return search(puzzle)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
