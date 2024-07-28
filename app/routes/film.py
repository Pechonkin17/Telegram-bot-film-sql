import validators
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from ..data import get_films, get_film_by_title, create_film, delete_film, update_film, find_film, find_films_by_partial_title
from ..fsm import FilmCreateUpdateForm, FilmDeleteForm, FilmFindForm, FilmUpdateForm
from ..keyboards import build_films_keyboard, build_details_keyboard

film_router = Router()

@film_router.message(Command("films"))
@film_router.message(F.text.casefold().contains("films"))
async def show_films_command(message: Message, state: FSMContext):
    await check_commands(message, state)

    films = get_films()

    if not films:
        await message.answer(
            text="No films in database",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        keyboard = build_films_keyboard(films)
        await message.answer(
            text="Choose film",
            reply_markup=keyboard
        )

@film_router.callback_query(F.data.startswith("film_"))
async def show_film_details(callback: CallbackQuery, state: FSMContext) -> None:
    await check_commands(callback.message, state)

    film_id = int(callback.data.split("_")[-1])
    film = get_film_by_title(film_id)
    text = f"Name: {hbold(film.get('title'))}\nDescription: {hbold(film.get('fdescription'))}\nRating: {hbold(film.get('rating'))}"
    photo_id = film.get('photo_url')
    url = film.get('url')
    await callback.message.answer_photo(photo_id)
    await edit_or_answer(
        callback.message,
        text,
        build_details_keyboard(url)
    )

async def edit_or_answer(message: Message, text: str, keyboard, **kwards):
    if message.from_user.is_bot:
        await message.edit_text(text=text, reply_markup=keyboard, **kwards)
    else:
        await message.answer(text=text, reply_markup=keyboard, **kwards)

@film_router.message(Command("create_film"))
@film_router.message(F.text.casefold() == "create film")
async def create_film_command(message: Message, state: FSMContext) -> None:
    await check_commands(message, state)

    await state.clear()
    await state.update_data(action="create")
    await state.set_state(FilmCreateUpdateForm.title)
    await edit_or_answer(
        message,
        "Input title",
        ReplyKeyboardRemove()
    )


@film_router.message(Command("update_film"))
@film_router.message(F.text.casefold() == "update film")
async def update_film_command(message: Message, state: FSMContext) -> None:
    await check_commands(message, state)

    await state.clear()
    await state.update_data(action="update")

    await state.set_state(FilmUpdateForm.title)
    await message.answer(
        "Input title of film to update",
        reply_markup=ReplyKeyboardRemove()
    )


@film_router.message(FilmUpdateForm.title)
async def check_film_title(message: Message, state: FSMContext) -> None:
    title = message.text
    film = find_film(title)

    if film:
        await state.update_data(title=title)
        await state.set_state(FilmCreateUpdateForm.fdesciption)
        await message.answer(
            f"Film '{title}' found. Input new description:",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            "Film not found. Please check the title and try again."
        )
        await state.clear()

@film_router.message(Command("delete_film"))
@film_router.message(F.text.casefold() == "delete film")
async def delete_film_command(message: Message, state: FSMContext) -> None:
    await check_commands(message, state)

    await state.clear()
    await state.update_data(action="delete")

    await state.set_state(FilmDeleteForm.title)
    await edit_or_answer(
        message,
        "Enter title or type 'back' to cancel",
        ReplyKeyboardRemove()
    )

@film_router.message(FilmDeleteForm.title)
async def process_delete_film(message: Message, state: FSMContext) -> None:
    await state.update_data(title=message.text)
    title = (await state.get_data()).get('title')
    await state.clear()

    if title and delete_film(title):
        await edit_or_answer(
            message,
            "Deleted successfully",
            ReplyKeyboardRemove()
        )
    elif title == 'back':
        return await show_films_command(message, state)
    else:
        await edit_or_answer(
            message,
            "Film with this title was not found",
            ReplyKeyboardRemove()
        )
    return await show_films_command(message, state)

@film_router.message(FilmCreateUpdateForm.title)
async def process_title(message: Message, state: FSMContext) -> None:
    await state.update_data(title=message.text)
    await state.set_state(FilmCreateUpdateForm.fdescription)
    await edit_or_answer(
        message,
        "Input description",
        ReplyKeyboardRemove()
    )

@film_router.message(FilmCreateUpdateForm.fdescription)
async def process_fdescription(message: Message, state: FSMContext) -> None:
    data = await state.update_data(fdescription=message.text)
    await state.set_state(FilmCreateUpdateForm.url)
    await edit_or_answer(
        message,
        f"Enter url of {hbold(data.get('title'))}",
        ReplyKeyboardRemove()
    )

@film_router.message(FilmCreateUpdateForm.url)
@film_router.message(F.text.contains('http'))
async def process_url(message: Message, state: FSMContext) -> None:
    data = await state.update_data(url=message.text)
    url = message.text
    if validators.url(url):
        data = await state.update_data(url=url)
        await state.set_state(FilmCreateUpdateForm.photo_url)
        await edit_or_answer(
            message,
            f"Choose photo {hbold(data.get('title'))}",
            ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            "The URL provided is not valid. Please enter a valid URL."
        )

@film_router.message(FilmCreateUpdateForm.photo_url)
@film_router.message(F.photo)
async def process_photo_url(message: Message, state: FSMContext) -> None:
    photo = message.photo[-1]
    photo_id = photo.file_id

    data = await state.update_data(photo_url=photo_id)
    await state.set_state(FilmCreateUpdateForm.rating)
    await edit_or_answer(
        message,
        "Rating 1 to 10",
        ReplyKeyboardRemove()
    )

@film_router.message(FilmCreateUpdateForm.rating)
async def process_rating(message: Message, state: FSMContext) -> None:
    data = await state.update_data(rating=message.text)
    action = (await state.get_data()).get('action')

    filtered_data = {
        "title": data.get("title"),
        "fdescription": data.get("fdescription"),
        "url": data.get("url"),
        "photo_url": data.get("photo_url"),
        "rating": data.get("rating")
    }

    if action == "create":
        create_film(filtered_data)
        await message.answer("Saved successfully.")

    elif action == "update":
        title = data.get('title')
        update_film(title, filtered_data)
        await message.answer("Updated successfully.")

    await state.clear()

    film = find_film(data.get('title'))
    if film:
        text = f"Name: {hbold(film.get('title'))}\nDescription: {hbold(film.get('fdescription'))}\nRating: {hbold(film.get('rating'))}"
        photo_id = film.get('photo_url')
        url = film.get('url')
        await message.answer_photo(photo_id)
        await edit_or_answer(
            message,
            text,
            build_details_keyboard(url)
        )
    else:
        await message.answer("Film not found. Database ERROR")

@film_router.message(Command("find_film"))
@film_router.message(F.text.casefold() == "find film")
async def find_film_command(message: Message, state: FSMContext) -> None:
    await check_commands(message, state)

    await state.clear()
    await state.update_data(action="find")
    await state.set_state(FilmFindForm.title)
    await edit_or_answer(
        message,
        "Enter title or part of the title",
        ReplyKeyboardRemove()
    )

@film_router.message(FilmFindForm.title)
async def process_find_film(message: Message, state: FSMContext) -> None:
    partial_title = message.text
    matched_films = find_films_by_partial_title(partial_title)
    await state.clear()

    if not matched_films:
        await message.answer("No films found with that title.")
    elif len(matched_films) == 1:
        film = matched_films[0]
        text = f"Name: {hbold(film.get('title'))}\nDescription: {hbold(film.get('fdescription'))}\nRating: {hbold(film.get('rating'))}"
        photo_id = film.get('photo_url')
        url = film.get('url')
        await message.answer_photo(photo_id)
        await edit_or_answer(
            message,
            text,
            build_details_keyboard(url)
        )
    else:
        keyboard = build_films_keyboard(matched_films)
        await message.answer(
            text="Choose a film",
            reply_markup=keyboard
        )

@film_router.callback_query(F.data == 'back')
async def back_handler(callback: CallbackQuery, state) -> None:
    return await show_films_command(callback.message, state)

async def check_commands(message: Message, state: FSMContext):
    action = (await state.get_data()).get('action')
    if action:
        await state.clear()
        await message.answer(
            text=f"action {hbold(action)} canceled",
            reply_markup=ReplyKeyboardRemove()
        )