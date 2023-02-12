from subs import print_header, get_symbol

#------------------------------
# Matrix - Класс игрового поля                     
#------------------------------
class Matrix:
    size: int           # Размер матрицы
    title: str          # Заголовок
    matrix: list = []   # Само поле
    pattern: list = []  # Схематическое представление(чтобы каждый раз не вычислять)
    gamer: int = 0      # Игрок 
    round: int = 1      # Раунд
    step: int = 1       # Номер хода

    # Констрцктор
    def __init__(self, size: int, title: str) -> None:
        self.size = size
        self.title = title
        self.matrix = [[0 for i in range(self.size)] for j in range(self.size)]
        self.pattern = [[(i + j*self.size + 1) for i in range(self.size)] for j in range(self.size)]

    # Отображение игрового поля и схемы
    def show(self, digit: bool = False) -> None:
        if digit:
            print()
            print_header(self.size*3, f'ИГРА "{self.title.upper()}"')
        print()
        print_header(self.size*2, f'Раунд {self.round}. Ход {self.step}. Очередь {self.gamer+1} игрока.')
        self.show_substr()

    # Построчный вывод игрового поля и схемы    
    def show_substr(self):
        for i in range(self.size):
            space = ' '*self.size*8
            sep = ' | '
            print((sep.join(map(str, self.pattern[i]))
                    + space +sep.join(get_symbol(self.matrix[i]))))
            if i < self.size-1:
                foot = '-'*(self.size*3) 
                print(foot + space + foot)
        print()

    # Метод очистки матрицы перед новым раундом
    def clear_data(self):
        self.step = 1
        self.round += 1
        self.gamer = 0
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = 0
        self.show(True)

    # Метод выполнения хода игроком при выполнении ряда условий
    def make_move(self, num: int): 
        i = (num-1) // 3
        j = num - i*3 -1

        if self.matrix[i][j] == 0:
            self.step += 1
            self.gamer = not self.gamer

            if self.gamer == 0:
                self.matrix[i][j] = 1
            else:
                self.matrix[i][j] = -1
            self.show()
            return self.is_finish(i, j)
        else:
            print('Ход недоступен!')
            return False

    # Метод, проверяющий соблюдение условий окончания игры
    def is_finish(self, row: int, col: int):
        sz = self.size
        is_victory = (abs(sum([self.matrix[row][j] for j in range(sz)]))==3 or 
            abs(sum([self.matrix[i][col] for i in range(sz)]))==3 or
            abs(sum([self.matrix[i][i] for i in range(sz)]))==3 or
            abs(sum([self.matrix[i][sz - i - 1] for i in range(sz)]))==3)
        
        if (self.step == sz**2+1 or is_victory):
            if is_victory:
                print(f'Партия окончена. Выиграл {1 + (not self.gamer)} игрок.\n')
                print_header(self.size*3,'ПОЗДРАВЛЯЮ ПОБЕДИТЕЛЯ!!!')
            else:
                print(f'Партия окончена. Нет доступных ходов.')
            print()
            return True
        return False