import sqlite3 as db

def connect():
    conn = db.connect('movies.db')
    cursor = conn.cursor()
    return [conn, cursor]

def create_table(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS movie(IMDB int, title varchar(255), status int)')
    
def get_movies(cursor):
    movies = cursor.execute(f'SELECT * FROM movie')
    movies = cursor.fetchall()
    return(movies)

def insert_movies(movies):
    pass
    
def insert_movies_into_database(movies, con, cursor):
    title, pos, status = 0, 0, 0
    for index, row in movies.iterrows():
        print(f'{row['Titulo']}, {row['Posicao IMDB']}, {row['Status']}')
        cursor.execute(f'INSERT INTO movie("IMDB", "title", "status") VALUES ({row['Posicao IMDB']}, "{row['Titulo']}", {row['Status']})')
        con.commit()
            
            
def get_unwatched(cursor):
    movies = cursor.execute(f'SELECT * FROM movie WHERE status = 0')
    movies = cursor.fetchall()
    return(movies)

def get_watched(cursor):
    movies = cursor.execute(f'SELECT * FROM movie WHERE status = 1')
    movies = cursor.fetchall()
    return(movies)

def set_watched(con, cursor, IMDB):
    cursor.execute(f'UPDATE movie SET Status = 1 WHERE IMDB = {IMDB}')
    con.commit()
    
def get_movie(cursor, IMDB):
    movie = cursor.execute(f'SELECT * FROM movie WHERE IMDB = {IMDB}')
    movie = cursor.fetchall()
    return movie 