from subs import input_number
from matrix import Matrix

# --------------------------------------------------------------------------
# Game - Класс, создающий игровое поле и обеспечивающий смену раундов в игре
# --------------------------------------------------------------------------
class Game:
    matrix: Matrix

    # Конструктор
    def __init__(self):
        self.matrix = Matrix(3, 'Крестики - нолики')
        self.matrix.show(digit = True)
    
    # Прием данных от пользователя, - взаимодействие с пользователем в текущем раунде и в игре в целом
    def players_move(self)-> tuple:
        pos = input_number('Введите номер клетки [1, 9]: ', 1, 9)
        if  self.matrix.make_move(pos):
            in_game = bool(input_number('Желаете продолжить? [1-да, 0-нет]: ', 0, 1))
            if in_game:
                self.matrix.clear_data()
            return (in_game)
        else:
            return True
