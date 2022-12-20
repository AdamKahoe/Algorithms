class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        def check(grid):
            for x in range(3):
                row = set([grid[x][0],grid[x][1],grid[x][2]])
                if len(row) == 1 and grid[x][0] != 0:
                    return grid[x][0]

            for x in range(3):
                column = set([grid[0][x],grid[1][x],grid[2][x]])
                if len(column) == 1 and grid[0][x] != 0:
                    return grid[0][x]

            diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
            diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
            if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
                return grid[1][1]

            return 0

        if not moves:
            return ""
        grid = [[0, 0, 0], [0, 0, 0], [0,0,0]]
        user = 1
        for move in moves:
            grid[move[0]][move[1]] = user
            if user == 1:
                user = 2
            else:
                user = 1

        result = check(grid)
        if result == 1:
            return "A"
        elif result == 2:
            return "B"
        else:
            if len(moves) == 9:
                return "Draw"
            else:
                return "Pending"