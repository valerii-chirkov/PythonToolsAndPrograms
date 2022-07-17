import random


class Cell:
    def __init__(self) -> None:
        self.value = 0

    def __bool__(self):
        return True if self.value == 0 else False


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self) -> None:
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def __check_index(self, *args):
        for idx in args[0]:
            if not 0 <= idx <= 2 or not isinstance(idx, int):
                raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_index(item)
        i, j = item
        return self.pole[i][j].value
    
    def __setitem__(self, key, value):
        self.__check_index(key)
        i, j = key
        self.pole[i][j].value = value

    def __bool__(self):
        return any(cell.value==0 for row in self.pole for cell in row) and not self.is_computer_win and not self.is_human_win

    def win_by_rows(self, value):
        return any(list(all(self[row,col]==value for col in range(3)) for row in range(3)))

    def win_by_cols(self, value):
        return any(list(all(self[row,col]==value for row in range(3)) for col in range(3)))

    def win_by_cross(self, value):
        return all(self[i,i]==value for i in range(3)) or all([self[0,2]==value, self[1,1]==value, self[2,0]==value])

    def decide_win(self, value):
        return any([self.win_by_cols(value), self.win_by_rows(value), self.win_by_cross(value)])

    @property
    def is_human_win(self):
        return self.decide_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.decide_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        if all(cell.value==0 for row in self.pole for cell in row):
            return False
        return not self.is_human_win and not self.is_computer_win

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0

    def show(self):
        for row in self.pole:
            for cell in row:
                print(cell.value, end='')
            print('\n', end='')
        print()

    def go(self, obj):
        free_cells_list = []
        for row_pos, row in enumerate(self.pole):
            for cell_pos, cell in enumerate(row):
                if cell.value == 0:
                    free_cells_list.append([row_pos, cell_pos])
        self[random.choice(free_cells_list)] = obj

    def human_go(self):
        self.go(self.HUMAN_X)

    def computer_go(self):
        self.go(self.COMPUTER_O)



game = TicTacToe()
game.init()
step_game = 0

while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
