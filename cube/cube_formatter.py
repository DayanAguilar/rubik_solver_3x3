COLOURS = ["W","O","G","R","B","Y"]

class CubeFormatter:
    def __init__(self, state):
        self.n = 3
        self.colores = []
        self.cube = [[[]]]
        for i, s in enumerate(state):
                if s not in self.colores:
                    self.colores.append(s)
                self.cube[-1][-1].append(s)
                if len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) < self.n:
                    self.cube[-1].append([])
                elif (
                    len(self.cube[-1][-1]) == self.n
                    and len(self.cube[-1]) == self.n
                    and i < len(state) - 1
                ):
                    self.cube.append([[]])
    
    def get_cube(self):
        return self.cube
