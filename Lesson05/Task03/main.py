# Создайте программу для игры в ""Крестики-нолики""

from game import Game
from matrix import Matrix

# Главный метод программы - создание игры и выход из нее по условию
def main():
    game: Game = Game()
    in_game = True
    while in_game:
        in_game = game.players_move()
    print('\nК О Н Е Ц    И Г Р Ы')
    print(f'------ 02.2023 ------\n')

# Здесь началось и здесь все закончится(с)
if __name__=='__main__':
    main()
    
