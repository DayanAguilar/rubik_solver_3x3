class CubeMoves:
    def __init__(self, cube):
        self.cube = cube

    def horizontal_twist(self, row, direction):
        if row < len(self.cube[0]):
            if direction == 0:
                (
                    self.cube[1][row],
                    self.cube[2][row],
                    self.cube[3][row],
                    self.cube[4][row],
                ) = (
                    self.cube[2][row],
                    self.cube[3][row],
                    self.cube[4][row],
                    self.cube[1][row],
                )

            elif direction == 1:
                (
                    self.cube[1][row],
                    self.cube[2][row],
                    self.cube[3][row],
                    self.cube[4][row],
                ) = (
                    self.cube[4][row],
                    self.cube[1][row],
                    self.cube[2][row],
                    self.cube[3][row],
                )
            else:
                print(f"ERROR - direction must be 0(left) or 1(right)")
                return

            if direction == 0:
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(*reversed(self.cube[0]))]
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(*reversed(self.cube[5]))]
            elif direction == 1:
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(*self.cube[0])][::-1]
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(*self.cube[5])][::-1]
        else:
            print(f"ERROR - row must be between 0-{len(self.cube[0]) - 1}")
            return

    def vertical_twist(self, column, direction):
        if column < len(self.cube[0]):
            for i in range(len(self.cube[0])):
                if direction == 0:
                    (
                        self.cube[0][i][column],
                        self.cube[2][i][column],
                        self.cube[4][-i - 1][-column - 1],
                        self.cube[5][i][column],
                    ) = (
                        self.cube[4][-i - 1][-column - 1],
                        self.cube[0][i][column],
                        self.cube[5][i][column],
                        self.cube[2][i][column],
                    )
                elif direction == 1:
                    (
                        self.cube[0][i][column],
                        self.cube[2][i][column],
                        self.cube[4][-i - 1][-column - 1],
                        self.cube[5][i][column],
                    ) = (
                        self.cube[2][i][column],
                        self.cube[5][i][column],
                        self.cube[0][i][column],
                        self.cube[4][-i - 1][-column - 1],
                    )
                else:
                    print(f"ERROR - direction must be 0 (down) or 1 (up)")
                    return
            if direction == 0:
                if column == 0:
                    self.cube[1] = [list(x) for x in zip(*self.cube[1])][::-1]
                elif column == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(*self.cube[3])][::-1]
            elif direction == 1:
                if column == 0:
                    self.cube[1] = [list(x) for x in zip(*reversed(self.cube[1]))]
                elif column == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(*reversed(self.cube[3]))]
        else:
            print(f"ERROR - column must be between 0-{len(self.cube[0]) - 1}")
            return

    def to_string(self):
        return "".join([i for r in self.cube for s in r for i in s])
    
    def solved(self):
        for side in self.cube:
            visitados = []
            solved = True
            for fila in side:
                if len(set(fila)) == 1:
                    visitados.append(fila[0])
                else:
                    solved = False
                    break
            if solved == False:
                break
            if len(set(visitados)) > 1:
                solved = False
                break
        return solved

    def deep_twist(self, column, direction):
        if column < len(self.cube[0]):
            for i in range(len(self.cube[0])):
                if direction == 0:
                    (
                        self.cube[0][column][i],
                        self.cube[1][-i - 1][column],
                        self.cube[3][i][-column - 1],
                        self.cube[5][-column - 1][-1 - i],
                    ) = (
                        self.cube[3][i][-column - 1],
                        self.cube[0][column][i],
                        self.cube[5][-column - 1][-1 - i],
                        self.cube[1][-i - 1][column],
                    )
                elif direction == 1:
                    (
                        self.cube[0][column][i],
                        self.cube[1][-i - 1][column],
                        self.cube[3][i][-column - 1],
                        self.cube[5][-column - 1][-1 - i],
                    ) = (
                        self.cube[1][-i - 1][column],
                        self.cube[5][-column - 1][-1 - i],
                        self.cube[0][column][i],
                        self.cube[3][i][-column - 1],
                    )
                else:
                    print(f"ERROR - direction must be 0 (down) or 1 (up)")
                    return
            if direction == 0:
                if column == 0:
                    self.cube[4] = [list(x) for x in zip(*reversed(self.cube[4]))]
                elif column == len(self.cube[0]) - 1:
                    self.cube[2] = [list(x) for x in zip(*reversed(self.cube[2]))]
            elif direction == 1:
                if column == 0:
                    self.cube[4] = [list(x) for x in zip(*self.cube[4])][::-1]
                elif column == len(self.cube[0]) - 1:
                    self.cube[2] = [list(x) for x in zip(*self.cube[2])][::-1]
        else:
            print(f"ERROR - column must be between 0-{len(self.cube[0]) - 1}")
            return
