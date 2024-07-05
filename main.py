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
    print('3 - Listar filmes assistidos')
    print('4 - Sortear novo filme para assistir')
    print('5 - Marcar filme assistido')
    print('6 - Editar registro')
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
        
    #listar filmes assistidos
    elif option == 3:
        os.system('cls')
        watched = db.get_watched(cursor)
        for movie in watched:
            print(f'{movie[0]:>3} - {movie[1]}')
            sleep(0.01)

        print('')
        print(f'Voce assistiu {len(watched)} filmes da lista.')
        print('')
        input('Tecle ENTER para continuar...')
        
        
    #sortear um filme    
    elif option == 4:
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
    
    #marcar filme como assistido
    elif option == 5:
        confirm = 0
        os.system('cls')
        unwatched = db.get_unwatched(cursor)
        for movie in unwatched:
            print(f'{movie[0]:>3} - {movie[1]}')
            sleep(0.01)
    
        #TODO: Tratar erro de selecao (filme que esta na lista geral pode ser selecionado)
        while confirm != 1:
            print('')
            print('Qual a posicao IMDB do filme assistido?')
            imdb = int(input('>>> '))
            selected_movie = db.get_movie(cursor, imdb)
            print('')
            print(f'{selected_movie[0][0]:>3} - {selected_movie[0][1]}')
            print('')
            print(f'Confirma o filme assistido? ')
            print('1 - Sim / 2 - Nao / 3 - Voltar')
            confirm = int(input('>>> '))
            if confirm == 1:
                db.set_watched(con, cursor, imdb)
            elif confirm == 3:
                break

    # editar registro de filme assistido
    elif option == 6:
        os.system('cls')
        movies = db.get_movies(cursor)
        for movie in movies:
            print(f'{movie[0]:>3} - {movie[1]}')
            sleep(0.01)
        print('Qual a posicao IMDB do filme que deseja alterar?')
        imdb = int(input('>>> '))
        ### MENU DE ALTERACAO
        


os.system('cls')
