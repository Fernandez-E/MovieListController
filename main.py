from functions import database as db
import pandas as pd
from random import randint
import os
from time import sleep

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
    os.system('cls')
    print('-' * 50)
    print('Controle e sorteio de filmes')
    print('-' * 50)
    
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
        os.system('cls')
        database_movies = db.get_movies(cursor)
        for movie in database_movies:
            print(f'{movie[0]:>3} - {movie[1]}')
            sleep(0.01)
        print('')
        input('Tecle ENTER para continuar...')  

    #listar nao assistidos
    elif option == 2:
        os.system('cls')
        unwatched = db.get_unwatched(cursor)
        for movie in unwatched:
            print(f'{movie[0]:>3} - {movie[1]}')
            sleep(0.01)

        print('')
        print(f'Existem {len(unwatched)} filmes ainda nao assistidos.')
        print('')
        input('Tecle ENTER para continuar...')
        
    #sortear um filme    
    elif option == 3:
        os.system('cls')
        unwatched = db.get_unwatched(cursor)
        unwatched_quantity = len(unwatched)
        selected = randint(1, unwatched_quantity)
        print('-' * 50)
        sleep(0.5)
        print('Sorteando...')
        sleep(1.5)
        print('-' * 50)
        sleep(0.5)
        print(f'{unwatched[selected][0]} - {unwatched[selected][1]}')
        sleep(0.5)
        print('-' * 50)
        sleep(0.5)
        print('')
        input('Tecle ENTER para continuar...')
    
    #marcar filme como marcado
    elif option == 4:
        os.system('cls')
        unwatched = db.get_unwatched(cursor)
        for movie in unwatched:
            print(f'{movie[0]:>3} - {movie[1]}')
            sleep(0.01)
        print('Qual a posicao IMDB do filme assistido?')
        imdb = int(input('>>> '))
        db.set_watched(con, cursor, imdb)

    # editar registro de filme assistido
    elif option == 5:
        os.system('cls')
        movies = db.get_movies(cursor)
        for movie in movies:
            print(f'{movie[0]:>3} - {movie[1]}')
            sleep(0.01)
        print('Qual a posicao IMDB do filme que deseja alterar?')
        imdb = int(input('>>> '))
        ### MENU DE ALTERACAO
        


os.system('cls')
