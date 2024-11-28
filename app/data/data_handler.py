from app.data.database import create_connection



def get_films():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM bot_data')
    films = cursor.fetchall()
    cursor.close()
    connection.close()

    film_dicts = []
    for film in films:
        film_dict = {
            'id': film[0],
            'title': film[1],
            'fdescription': film[2],
            'url': film[3],
            'photo_url': film[4],
            'rating': film[5]
        }
        film_dicts.append(film_dict)
    return film_dicts


def get_film_by_title(title):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM bot_data WHERE title = %s"
    cursor.execute(query, (title,))
    film = cursor.fetchone()
    cursor.close()
    connection.close()

    if film is None:
        return {}
    else:
        film_dict = {
            'id': film[0],
            'title': film[1],
            'fdescription': film[2],
            'url': film[3],
            'photo_url': film[4],
            'rating': film[5]
        }
        return film_dict


def create_film(film: dict):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO bot_data (title, fdescription, url, photo_url, rating)
    VALUES (%s, %s, %s, %s, %s)
    """
    title = film.get('title')
    fdescription = film.get('fdescription')
    url = film.get('url')
    photo_url = film.get('photo_url')
    rating = film.get('rating')

    cursor.execute(query, (title, fdescription, url, photo_url, rating))
    connection.commit()
    cursor.close()
    connection.close()


def delete_film(title):
    if not find_film(title):
        return False

    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM bot_data WHERE title = %s"
    cursor.execute(query,(title,))
    connection.commit()
    cursor.close()
    connection.close()
    return True


def update_film(title, updated_film):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
        UPDATE bot_data 
        SET title = %s, fdescription = %s, url = %s, photo_url = %s, rating = %s 
        WHERE title = %s
        """
    cursor.execute(query, (
        updated_film.get('title'),
        updated_film.get('fdescription'),
        updated_film.get('url'),
        updated_film.get('photo_url'),
        updated_film.get('rating'),
        title
    ))
    connection.commit()
    cursor.close()
    connection.close()


def find_film(title):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM bot_data WHERE title = %s"
    cursor.execute(query, (title,))
    film = cursor.fetchone()
    cursor.close()
    connection.close()

    if film is None:
        return None
    else:
        film_dict = {
            'title': film[1],
            'fdescription': film[2],
            'url': film[3],
            'photo_url': film[4],
            'rating': film[5]
        }
        return film_dict


def find_films_by_partial_title(title):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM bot_data WHERE title LIKE %s"
    cursor.execute(query, ('%' + title + '%',))
    films = cursor.fetchall()
    cursor.close()
    connection.close()

    film_dicts = []
    for film in films:
        film_dict = {
            'id': film[0],
            'title': film[1],
            'fdescription': film[2],
            'url': film[3],
            'photo_url': film[4],
            'rating': film[5]
        }
        film_dicts.append(film_dict)
    return film_dicts