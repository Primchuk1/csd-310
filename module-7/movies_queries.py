import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try: 
    db = mysql.connector.connect(**config)


    cursor = db.cursor()

    #Query 1
    cursor.execute("Select * FROM studio")
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    #Query 2
    cursor.execute("Select * FROM genre")
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    #Query 3
    cursor.execute("Select film_id, film_runtime FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for film in films:
        print("Film Name: {}\nFilm Runtime: {}\n".format(film[0], film[1]))

    #Query 4
    cursor.execute("Select film_name, film_director FROM film ORDER BY film_director")
    films = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for film in films:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))
    


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("     The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("     The specified database does not exist")
    
    else:
        print(err)

finally:
    db.close()

