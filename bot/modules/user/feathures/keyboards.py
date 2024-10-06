from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


def get_main_menu_keyboard():
    return InlineKeyboardMarkup(
        [
            # [InlineKeyboardButton("Выбор GPT", callback_data="Выбор GPT")],
            [InlineKeyboardButton("Выбор роли GPT", callback_data="Выбор роли GPT")],
            [InlineKeyboardButton("Подписка", callback_data="Подписка")],
        ]
    )


def get_subscriptions_keyboard():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Получить 5ч подписки", callback_data="Получить 5ч подписки")],
            [InlineKeyboardButton("Назад", callback_data="Назад")],
        ]
    )


def get_gpts_keyboard(context: CallbackContext):
    if not context.user_data.get("gpt_version"):
        context.user_data["gpt_version"] = "GPT 4o"
    keyboard = []
    for i in ["GPT o1", "GPT o1 (mini)", "GPT 4o", "GPT 4o (mini)"]:
        if i == context.user_data["gpt_version"]:
            keyboard.append([InlineKeyboardButton("✅" + i, callback_data=i)])
        else:
            keyboard.append([InlineKeyboardButton(i, callback_data=i)])
    keyboard.append([InlineKeyboardButton("Назад", callback_data="Назад")])
    return InlineKeyboardMarkup(keyboard)


def get_gpt_role_keyboard(context: CallbackContext):
    if not context.user_data.get("gpt_role"):
        context.user_data["gpt_role"] = "HR помощник по вакансии"
    keyboard = []
    for i in ["HR помощник по вакансии", "Кинокритик", "Спортсмен", "Поэт"]:
        keyboard.append([InlineKeyboardButton(i, callback_data=i)])
    keyboard.append([InlineKeyboardButton("Назад", callback_data="Назад")])
    return InlineKeyboardMarkup(keyboard)


def get_back_keyboard():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("Назад", callback_data="Назад")]]
    )
