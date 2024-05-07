import os
from cube.cube_formatter import CubeFormatter
from cube.cube_moves import CubeMoves

MOVES = 5
ACTIONS = [(r, n, d) for r in ["h", "v", "p"] for d in [0, 1] for n in range(3)]


class Heuristic:
    def __init__(self, state):
        if os.path.exists("heuristic/heuristic.txt"):
            self.heuristic = self.read_heuristic()
        else:
            self.heuristic = {state: 0}
            frontier = [(state, 0)]
            print("Wait.....")
            processed_nodes = 0
            while True:
                if not frontier:
                    break
                s, d = frontier.pop()
                if d > MOVES:
                    continue
                for a in ACTIONS:
                    cube_format = CubeFormatter(state=s)
                    cube = CubeMoves(cube_format.get_cube())
                    if a[0] == "h":
                        cube.horizontal_twist(a[1], a[2])
                    elif a[0] == "v":
                        cube.vertical_twist(a[1], a[2])
                    elif a[0] == "p":
                        cube.deep_twist(a[1], a[2])
                    a_str = cube.to_string()
                    if a_str not in self.heuristic or self.heuristic[a_str] > d + 1:
                        self.heuristic[a_str] = d + 1
                        frontier.append((a_str, d + 1))
                    processed_nodes += 1
                    with open("heuristic/heuristic.txt", "w") as f:
                        for key, value in self.heuristic.items():
                            f.write(f"{key}: {value}\n")
                print("Finished")
                    
    def read_heuristic(self):
        with open("heuristic/heuristic.txt", "r") as f:
            heuristic = {}
            for line in f:
                items = line.strip().split(": ")
                if len(items) == 2:
                    key, value = items
                    heuristic[key] = int(value)
        return heuristic

    def get_heuristic(self):
        return self.heuristic
