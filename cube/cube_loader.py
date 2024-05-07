COLOURS = ["W","O","G","R","B","Y"]

class CubeLoader:
    def __init__(filename):
        try:
            with open(filename,"r") as file:
                print(file)
        except:
            FileNotFoundError("The file doesn't exist")
    
    def initial_state(self):
        data=""
        for color in COLOURS:
            for i in range(0,9):
                data+=color
        return data
