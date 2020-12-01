class LabirintTurtle:
    def __init__(self):
        self.map = []
        self.ma = []

    def load_map(self, name):
        file = open(name, "r")
        line = file.readline()
        while line.find(" ") != -1 or line.find("*") != -1:
            self.map.append(list(line[:-1]))
            self.ma.append(list(line[:-1]))
            line = file.readline()
        try:
            x = int(line)
            line = file.readline()
            y = int(line)
            self.map[x][y] = "A"
        except ValueError:
            print("Ошибочка")

    def show_map(self, turtle=None):
        if turtle == True:
            for i in range(0, len(self.map)):
                for j in range(0, len(self.map[i])):
                    print(self.map[i][j], end="")
                print(sep="\n")
        else:
            for i in range(0, len(self.ma)):
                for j in range(0, len(self.ma[i])):
                    print(self.ma[i][j], end="")
                print(sep="\n")

    def check_map(self):
        pass

    def exit_count_step(self):
        pass

    def exit_show_step(self):
        pass


map = LabirintTurtle()
map.load_map("123.txt")
map.show_map(turtle=True)
