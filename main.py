from functions import database as db
import pandas as pd
from random import randint

#recebe os filmes em formato excel
movies = pd.read_excel('excel/IMDB.xlsx')

#conecta ao banco de dados
database = db.connect()
con = database[0]
cursor = database[1]
db.create_table(cursor)

#inserir se banco estiver vazio
database_movies = db.get_movies(cursor)
if database_movies == []:
    db.insert_movies_into_database(movies, con, cursor)

option = 999
while option != 0:
    print('Controle e sorteio de filmes')
    print('O que deseja fazer?')
    print('1 - Listar todos os filmes')
    print('2 - Listar filmes nao assistidos')
    print('3 - Sortear novo filme para assistir')
    print('4 - Marcar filme assistido')
    print('5 - Editar registro')
    print('0 - Sair')
    option = int(input('>>> '))
    
#listar filmes
if option == 1:
    database_movies = db.get_movies(cursor)
    for movie in database_movies:
        print(f'{movie[0]:>3} - {movie[1]}')

#listar nao assistidos
elif option == 2:
    unwatched = db.get_unwatched(cursor)
    for movie in unwatched:
        print(f'{movie[0]:>3} - {movie[1]}')

#sortear um filme    
elif option == 3:
    unwatched = db.get_unwatched(cursor)
    unwatched_quantity = len(unwatched)
    selected = randint(1, unwatched_quantity)
    print(f'{unwatched[selected][0]} - {unwatched[selected][1]}')