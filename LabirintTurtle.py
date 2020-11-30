class LabirintTurtle:
    def __init__(self):
        self.map = []
    def load_map(self, name):
        file = open(name, "r")
        line = file.readline()
        while line.find(" ") != -1 or line.find("*") != -1:
            self.map.append(list(line[:-1]))
            line = file.readline()
        try:
            x = int(line)
            line = file.readline()
            y = int(line)
            self.map[x][y] = "A"
            self.check_map()
        except ValueError:
            print("Ошибочка")
    def show_map(self):
        pass
    def check_map(self):
        pass
    def exit_count_step(self):
        pass
    def exit_show_step(self):
        pass