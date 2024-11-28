from aiogram.utils.keyboard import InlineKeyboardBuilder



def build_films_keyboard(films: list):
    builder = InlineKeyboardBuilder()
    for index, film in enumerate(films):
        builder.button(text=film.get("title"), callback_data=f"film_{index}")
    builder.adjust(1)
    return builder.as_markup()


def build_details_keyboard(url):
    builder = InlineKeyboardBuilder()
    builder.button(text="Watch film", url=url)
    builder.button(text="Back", callback_data="back")
    builder.adjust(1)
    return builder.as_markup()