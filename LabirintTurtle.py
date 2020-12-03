from termcolor import colored


class LabirintTurtle:
    def __init__(self):
        self.map = []
        self.ma = []
        self.map_vad = None
        self.s = [0, 0]
        self.x = 0
        self.y = 0
        self.d = True

    def load_map(self, name):
        file = open(name, "r", encoding='utf-8')
        line = file.readline()
        while line.find(" ") != -1 or line.find("*") != -1:
            self.map.append(list(line[:-1]))
            self.ma.append(list(line[:-1]))
            line = file.readline()
        try:
            self.x = int(line)
            line = file.readline()
            self.y = int(line)
            self.map[self.x][self.y] = "🦖"
        except ValueError:
            print("Ошибочка")

    def show_map(self, turtle=None):
        if turtle == True:
            for i in range(0, len(self.map)):
                for j in range(0, len(self.map[i])):
                    print(colored(self.map[i][j], "red"), end="\t")
                print("\t")
        else:
            for i in range(0, len(self.ma)):
                for j in range(0, len(self.ma[i])):
                    print(colored(self.ma[i][j], "blue"), end="\t")
                print("\t")

    def check_map(self, name=None):
        c = None
        for i in range(0, len(self.ma)):
            for j in range(0, len(self.ma[i])):
                if c == False:
                    break
                if self.ma[i][j] == "*" or self.ma[i][j] == " ":
                    c = True
                else:
                    c = False
        if c:
            self.map_vad = True
        else:
            self.map_vad = False

        if self.map_vad:
            for i in range(0, len(self.map)):
                for j in range(0, len(self.map[i])):
                    if i == 0 or j == 0 or \
                            i == self.map or j == self.map[i]:
                        if self.map[i][j] == " ":
                            self.map_vad = True
                            self.s = [i, j]

        if self.map_vad:
            if self.ma[self.x][self.y] == "*":
                self.map_vad = False
            else:
                self.map_vad = True

        if self.map_vad:
            if self.d:
                self.map_vad = True
            else:
                self.map_vad = False

        if self.map_vad:
            print("Yes")
            print(self.s)
        else:
            print("No")

    def exit_count_step(self):
        c = 0
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if self.map[i][j] == ".":
                    c += 1
        print(str(c) + " колво шагов")

    def exit_show_step(self):
        x, y = self.x, self.y
        while x != self.s[0] and y != self.s[1]:

            if self.map[x - 1][y] != "*":
                self.map[x - 1][y] = "."
                x, y = x - 1, y
                break

            if self.map[x][y + 1] != "*":
                self.map[x][y + 1] = "."
                x, y = x, y + 1
                break

            if self.map[x + 1][y] != "*":
                self.map[x + 1][y] = "."
                x, y = x, y + 1
                break

            if self.map[x][y - 1] != "*":
                self.map[x][y - 1] = "."
                x, y = x, y - 1
                break
        self.map[self.s[0]][self.s[1]] = "."

        if self.map[self.s[0]][self.s[1]] == ".":
            self.d = True
        else:
            self.d = False


map = LabirintTurtle()
map.load_map("123.txt")
map.check_map()
map.exit_show_step()
map.show_map(turtle=True)
map.exit_count_step()
