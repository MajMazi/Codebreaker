import codebreaker_model

def victory_text(game):
    text = "You cracked the code {0}!\n".format(game.code)
    return text

def loss_text(game):
    text = "The code was {0}! Better luck next time!\n".format(game.code)
    return text

def game_state(game):
    text = "There is a code consisting of four letters representing the colours of the rainbow - r, o, y, g, b, p. \n The first number in the result checks how many colours are correct, while the second states how many are in the correct order."
    return text

def request_input():
    return input("Guess a code: ")

def run_interface():
    game = codebreaker_model.new_game()
    while True:
        print(game_state(game))
        guess = request_input()
        game.make_guess(guess)
        print(game.guess_result)
        if game.defeat():
            print(loss_text(game))
            break
        elif game.victory():
            print(victory_text(game))
            break
        else:
            pass
    
    return None

run_interface()
print(game.guess_result)