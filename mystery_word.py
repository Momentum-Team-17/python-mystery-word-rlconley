def play_game():
    word = 'apple'
    wrong_guesses = ['b', 'd']
    right_guesses = []

    game_board = ''
    for letter in word:
        if letter in right_guesses:
            game_board += letter + ' '
        else:
            game_board += "_ "
    print(game_board)


if __name__ == "__main__":
    play_game()
