from .base import Session
from .model import Film # , Genre



def get_films():
    with Session() as session:
        films = session.query(Film).all()
        return [
            {
                'id': film.id,
                'title': film.title,
                'fdescription': film.fdescription,
                'url': film.url,
                'photo_url': film.photo_url,
                'rating': film.rating
            } for film in films
        ]


def get_film_by_id(id):
    with Session() as session:
        film = session.query(Film).filter(Film.id == title).first()
        if not film:
            return {}
        return {
            'id': film.id,
            'title': film.title,
            'fdescription': film.fdescription,
            'url': film.url,
            'photo_url': film.photo_url,
            'rating': film.rating
        }


def create_film(film: dict):
    with Session() as session:
        new_film = Film(
            title=film['title'],
            fdescription=film['fdescription'],
            url=film['url'],
            photo_url=film['photo_url'],
            rating=film['rating']
        )
        session.add(new_film)
        session.commit()


def delete_film(title):
    with Session() as session:
        film = session.query(Film).filter(Film.title == title).first()
        if not film:
            return False
        session.delete(film)
        session.commit()
        return True


def update_film(title, updated_film):
    with Session() as session:
        film = session.query(Film).filter(Film.title == title).first()
        if not film:
            return False

        film.title = updated_film.get('title', film.title)
        film.fdescription = updated_film.get('fdescription', film.fdescription)
        film.url = updated_film.get('url', film.url)
        film.photo_url = updated_film.get('photo_url', film.photo_url)
        film.rating = updated_film.get('rating', film.rating)

        session.commit()
        return True


def find_film(title):
    with Session() as session:
        film = session.query(Film).filter(Film.title == title).first()
        if not film:
            return None
        return {
            'id': film.id,
            'title': film.title,
            'fdescription': film.fdescription,
            'url': film.url,
            'photo_url': film.photo_url,
            'rating': film.rating
        }


def find_films_by_partial_title(partial_title):
    with Session() as session:
        films = session.query(Film).filter(Film.title.like(f'%{partial_title}%')).all()
        return [
            {
                'id': film.id,
                'title': film.title,
                'fdescription': film.fdescription,
                'url': film.url,
                'photo_url': film.photo_url,
                'rating': film.rating
            } for film in films
        ]
