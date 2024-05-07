from cube.cube_moves import CubeMoves
from cube.cube_formatter import CubeFormatter
from random import choice


class CubeSolver:
    def __init__(self, heuristic, deep=20):
        self.deep = deep
        self.threshold = deep
        self.min_threshold = None
        self.heuristic = heuristic
        self.moves = []

    def ida_star_path(self, state):
        while True:
            status = self.ida_star(state, 1)
            if status:
                return self.moves
            self.moves = []
            self.threshold = self.min_threshold
        return []

    def ida_star(self, state, g_value):
        format_cube = CubeFormatter(state=state)
        cube = CubeMoves(format_cube.get_cube())
        if cube.solved():
            return True
        elif len(self.moves) >= self.threshold:
            return False
        valor_minimo = float("inf")
        accion_elegida = None
        for a in [(r, n, d) for r in ["h", "v", "p"] for d in [0, 1] for n in range(3)]:
            format_cube = CubeFormatter(state=state)
            cube = CubeMoves(format_cube.get_cube())
            if a[0] == "h":
                cube.horizontal_twist(a[1], a[2])
            elif a[0] == "v":
                cube.vertical_twist(a[1], a[2])
            elif a[0] == "p":
                cube.deep_twist(a[1], a[2])
            if cube.solved():
                self.moves.append(a)
                return True
            cube_string = cube.to_string()
            h_value = (
                self.heuristic[cube_string]
                if cube_string in self.heuristic
                else self.deep
            )
            f_value = g_value + h_value
            if f_value < valor_minimo:
                valor_minimo = f_value
                accion_elegida = [(cube_string, a)]
            elif f_value == valor_minimo:
                if accion_elegida is None:
                    accion_elegida = [(cube_string, a)]
                else:
                    accion_elegida.append((cube_string, a))
        if accion_elegida is not None:
            if self.min_threshold is None or valor_minimo < self.min_threshold:
                self.min_threshold = valor_minimo
            siguiente_accion = choice(accion_elegida)
            self.moves.append(siguiente_accion[1])
            status = self.ida_star(siguiente_accion[0], g_value + valor_minimo)
            if status:
                return status
        return False
