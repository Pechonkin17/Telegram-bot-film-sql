from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, REAL, Column, ForeignKey, Table
from typing import List

from .base import Base



class Film(Base):
    __tablename__ = 'films'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    fdescription: Mapped[str] = mapped_column(String(500), nullable=False, unique=False)
    url: Mapped[str] = mapped_column(String(300), nullable=False, unique=True)
    photo_url: Mapped[str] = mapped_column(String(1000), nullable=False, unique=True)
    rating: Mapped[int] = mapped_column(REAL, nullable=False, unique=False)
