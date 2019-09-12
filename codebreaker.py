import bottle
import codebreaker_model

bottle.TEMPLATE_PATH.insert(0,'U:\\uvp\\repozitorij\\codebreaker\\views')

SECRET_CODE = 'my_code'
FILE_WITH_CODES = 'list_of_codes.txt'
FILE_WITH_STATUS = 'status.json'
codebreaker = codebreaker_model.Codebreaker(FILE_WITH_STATUS, FILE_WITH_CODES)

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/new_game/')
def new_game():
    game_id = codebreaker.new_game()
    bottle.response.set_cookie('game_id', game_id, secret=SECRET_CODE, path='/')
    bottle.redirect('/game/')

@bottle.get('/game/')
def show_game():
    game_id = bottle.request.get_cookie('game_id', secret=SECRET_CODE)
    return bottle.template('game.tpl',
    game = codebreaker.games[game_id][0],
    game_id = game_id,
    guess = codebreaker.games[game_id][1])

@bottle.post('/game/')
def make_guess():
    game_id = bottle.request.get_cookie('game_id', secret=SECRET_CODE)
    guess_to_make = bottle.request.forms.getunicode("guess")
    codebreaker.make_guess(game_id,guess_to_make)
    bottle.redirect('/game/')

bottle.run(reloader=True, debug=True)