from game import Game

white_winning_games = []
black_winning_games = []

for i in range(1000):
    game = Game()
    game_moves = game.start_random()

    if game_moves[-1] == 'b' and game_moves:
        black_winning_games.append(game_moves)
    if game_moves[-1] == 'b' and game_moves:
        white_winning_games.append(game_moves)

    white_file = open('games/white_winning_games', 'w')
    white_file.write(str(white_winning_games))
    white_file.close()

    black_file = open('games/black_winning_games', 'w')
    black_file.write(str(black_winning_games))
    black_file.close()