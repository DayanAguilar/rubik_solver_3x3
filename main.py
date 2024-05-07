from heuristic.heuristic import Heuristic
from cube.cube_loader import CubeLoader
from cube.cube_formatter import CubeFormatter
from cube.cube_moves import CubeMoves
from cube.cube_solver import CubeSolver

initial_cube = CubeLoader().initial_state()
format_cube = CubeFormatter(initial_cube).get_cube()
cube = CubeMoves(format_cube)
# We move the cube 8 times
cube.horizontal_twist(1, 0)
cube.horizontal_twist(2, 0)
cube.horizontal_twist(0, 1)
cube.vertical_twist(0, 1)
cube.vertical_twist(1, 1)
cube.vertical_twist(2, 1)
cube.deep_twist(2, 1)
cube.deep_twist(2, 0)

# Create a heuristic
heuristic_generator = Heuristic(initial_cube)
heuristic = heuristic_generator.get_heuristic()
solver = CubeSolver(heuristic=heuristic)
solver.ida_star_path(cube.to_string())
print(solver.moves)
