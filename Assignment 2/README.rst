Assignment 2
=====

In this assignment you will implement a few Python programs related to searching, and answer a few questions related to them


Programming Part 1: Local search
=====

Task 1: The attack matrix
-------

* Consider the board (0, 3, 2, 1). We have 16 possible ways to move one queen, where only 12 of them are valid moves, producing 12 different boards.
* If we count the number of attacking pairs of these moves, we have:
1. Queen 0 to column 0: (not valid)
2. Queen 0 to column 1: (1, 3, 2, 1), count: 4
3. Queen 0 to column 2: (2, 3, 2, 1), count: 5
4. Queen 0 to column 3: (3, 3, 2, 1), count: 4
5. Queen 1 to column 0: (0, 0, 2, 1), count: 3
6. Queen 1 to column 1: (0, 1, 2, 1), count: 5
7. Queen 1 to column 2: (0, 2, 2, 1), count: 3
8. Queen 1 to column 3: (not valid)
9. Queen 2 to column 0: (0, 3, 0, 1), count: 3
10. Queen 2 to column 1: (0, 3, 1, 1), count: 2
11. Queen 2 to column 2: (not valid)
12. Queen 2 to column 3: (0, 3, 3, 1), count: 2
13. Queen 3 to column 0: (0, 3, 2, 0), count: 3
14. Queen 3 to column 1: (not valid)
15. Queen 3 to column 3: (0, 3, 2, 2), count: 3
16. Queen 3 to column 4: (0, 3, 2, 3), count: 5

* If we put these numbers on the board, at the position where the queen was moved to, the result will be ::

    -  4  5  4
    3  5  3  -
    3  2  -  2
    3  -  3  5

* We can see that by moving the queen at row 2 to position 1 or 3, we will get the smallest attacking count among the 12 possible moves. Let's call this the attack matrix.
* For any board, we can count the number of pairs of attacking queens using this function ::

    def countAttack(queen):
        count = 0
        for row1 in range( 0, len(queen) ):
            for row2 in range( row1 + 1, len( queen ) ):
                if queen[row1] == queen[row2]:
                    count += 1
                elif abs(queen[row1] - queen[row2]) == (row2 - row1):
                    count += 1
        return count

You can use the above function in this and the following tasks.

* For this task, define the function printMatrix(queen) in nqueen.py with one parameter, queen.
* Parameter queen is a tuple representing a n-queen problem as described above.
* The function should print the corresponding attack matrix, with each value occupying 2 spaces, left-aligned.
* For example, you can test your function in main.py using the following code ::

    from nqueen import *
    printMatrix( (0, 3, 2, 1) )

which produces the output ::

    -  4  5  4
    3  5  3  -
    3  2  -  2
    3  -  3  5
    
* Not that your function should be able to handle boards of different sizes, e.g., ::

    from nqueen import *
    printMatrix( (0, 3, 2, 1, 0, 3, 2, 1) )
    
which produces the output ::

    -  16 17 16 18 14 14 14
    14 16 14 -  12 12 12 15
    15 13 -  13 12 11 14 11
    13 -  13 15 11 15 11 11
    -  13 15 13 16 11 12 11
    14 16 14 -  12 14 12 13
    15 14 -  14 14 12 14 12
    15 -  15 17 13 15 13 15
    
* You can assume that the input queen is always a valid board, with all values less than the size of board.
* You can assume that the board will not exceed the size of 8.



