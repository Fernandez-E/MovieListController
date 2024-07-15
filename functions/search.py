from functions import database as db

database = db.connect()
con = database[0]
cursor = database[1]


def search_movie(title):
    movies = db.get_unwatched(cursor)
    for movie in movies:
        #TODO: tratar exceção de uso de "-" | Ex: ValueError: invalid literal for int() with base 10: 'homem-aranha'
        if title.lower() in movie[1].lower():
            print(f'{movie[0]:>3} - {movie[1]}')
        #TODO: Retornar mensagem de filme nao encontrado
