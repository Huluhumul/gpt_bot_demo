from telegram import KeyboardButton, ReplyKeyboardMarkup


def get_auth_keyboard():
    return ReplyKeyboardMarkup(
        [[KeyboardButton("Отправить контакт", request_contact=True)]]
    )
