from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, REAL, Column, ForeignKey, Table
from typing import List

from .base import Base



# film_genre_table = Table(
#     'film_genre',
#     Base.metadata,
#     Column('film_id', ForeignKey('films.id'), primary_key=True),
#     Column('genre_id', ForeignKey('genres.id'), primary_key=True)
# )



class Film(Base):
    __tablename__ = 'films'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    fdescription: Mapped[str] = mapped_column(String(500), nullable=False, unique=False)
    url: Mapped[str] = mapped_column(String(300), nullable=False, unique=True)
    photo_url: Mapped[str] = mapped_column(String(1000), nullable=False, unique=True)
    rating: Mapped[int] = mapped_column(REAL, nullable=False, unique=False)
    #genres: Mapped[List['Genre']] = relationship('Genre', secondary=film_genre_table, back_populates='films')



# class Genre(Base):
#     __tablename__ = 'films'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
#     films: Mapped[List['Film']] = relationship('Film', back_populates='genre')
