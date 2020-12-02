class LabirintTurtle:
    def __init__(self):
        self.map = []
        self.ma = []
        self.map_vad = None
        self.size = [0, 0]

    def load_map(self, name):
        file = open(name, "r")
        line = file.readline()
        while line.find(" ") != -1 or line.find("*") != -1:
            self.map.append(list(line[:-1]))
            self.ma.append(list(line[:-1]))
            line = file.readline()
        self.size[0] = len(self.ma)
        self.size[1] = len(self.ma[0])
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
            co1 = 0
            co2 = 0
            co3 = 0
            co4 = 0
            u = False
            b = False
            l = False
            r = False
            up = self.ma[0]
            for i in up:
                if i == "*":
                    co1 += 1
            bottom = self.ma[-1]
            for i in bottom:
                if i == "*":
                    co2 += 1
            left = [i[0] for i in self.ma]
            for i in left:
                if i == "*":
                    co3 += 1
            right = [i[-1] for i in self.ma]
            for i in right:
                if i == "*":
                    co4 += 1

            if len(up) // 2 == co1:
                u = True
            if len(bottom) // 2 == co2:
                b = True
            if len(left) != co3:
                l = True
            if len(right) != co4:
                r = True
            if u == False and b == False and l == False and r == False:
                self.map_vad = False

        if self.map_vad:
            tur = ''
            up = self.map[0]
            bottom = self.map[-1]
            left = [i[0] for i in self.map]
            right = [i[-1] for i in self.map]
            for i in up:
                if i == 'A':
                    tur = "turtle"
                    break
                else:
                    u = True
            for i in bottom:
                if i == 'A':
                    tur = "turtle"
            for i in left:
                if i == 'A':
                    tur = "turtle"
            for i in right:
                if i == 'A':
                    tur = "turtle"

            if tur == "turtle":
                self.map_vad = False
            else:
                self.map_vad = True

        if self.map_vad:
            print("Yes")
        else:
            print("No")

    def exit_count_step(self):
        pass

    def exit_show_step(self):
        pass


map = LabirintTurtle()
map.load_map("123.txt")
map.show_map(turtle=True)
map.check_map()
