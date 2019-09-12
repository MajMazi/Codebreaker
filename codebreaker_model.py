import random
import json

NUMBER_OF_GUESSES = 10
START = 'S'
WIN = 'W'
LOSS = 'L'


class Game:
    def __init__(self, code, current_guesses = None):
        self.code = code
        if current_guesses is None:
            self.current_guesses = []
            self.guesses_used = 0
        else:
            self.current_guesses = current_guesses
            self.guesses_used = len(self.current_guesses)


    def guesses_used(self):
        return len(self.current_guesses)
    
    def victory(self):
        if self.code in self.current_guesses:
            return True
        else:
            return False

    def defeat(self):
        return self.guesses_used == NUMBER_OF_GUESSES and self.code not in self.current_guesses

    def make_guess(self, guess):
        code = self.code
        self.guess_correct_placements = 0
        self.guess_correct_values = 0    
        self.guesses_used += 1
        self.current_guesses.append(guess)    
        for x in guess:
            if x in self.code:
                   self.guess_correct_values += 1
            else:
                pass
        for x in guess:
            if guess.find(x) == code.find(x):
                self.guess_correct_placements +=1
            else:
                pass
        self.guess_result = [self.guess_correct_values, self.guess_correct_placements]
        return self.guess_result
        



    
with open("list_of_codes.txt", "r", encoding = "utf-8") as f:
                code_pool = [line.strip() for line in f]
def new_game():
    return Game(random.choice(code_pool))
    

class Codebreaker:

    def __init__(self, file_with_status, file_with_codes):
        self.games = {}
        self.file_with_status = file_with_status
        self.file_with_codes = file_with_codes
    
    def load_game_from_file(self):
        with open(self.file_with_status, 'r', encoding='utf-8') as f:
            games = json.load(f)
            self.games = { int(game_id) : (Game(games[game_id]['code'], games[game_id]['current_guesses']),
            games[game_id]['guess']
            )
                for game_id in games
            }
        return

    def save_games_to_file(self):
        with open(self.file_with_status, 'w', encoding = 'utf-8') as f:
                games = {game_id : {'code':game.code, 'current_guesses': game.current_guesses, 'guess':guess}
                for game_id, (game, guess) in self.games.items()}
                json.dump(games, f)

    def free_game_id(self):
        if len(self.games) == 0:
            return 0
        else:
            return max(self.games.keys()) + 1
        
    def new_game(self):
        self.load_game_from_file()
        game_id = self.free_game_id()
        with open("list_of_codes.txt", "r", encoding = "utf-8") as f:
            code_pool = [line.strip() for line in f]
        game = Game(random.choice(code_pool))
        self.games[game_id] = (game, START)
        self.save_games_to_file()
        return game_id

    def make_guess(self, game_id, guess):
        self.load_game_from_file()
        game = self.games[game_id][0]
        new_state = game.make_guess(guess)
        self.games[game_id] = (game, new_state)
        self.save_games_to_file()
        return