from telegram import Update
from telegram.ext import CallbackContext

from .keyboards import get_auth_keyboard


async def send_auth_message(update: Update, context: CallbackContext) -> None:
    context.user_data["old_keyboard_msg"] = (
        await update.effective_chat.send_message(
            text="Поделитесь контанктом что бы зарегистрироваться в системе",
            reply_markup=get_auth_keyboard(),
        )
    )


async def send_main_menu(update: Update, context: CallbackContext) -> None:
    context.user_data["old_keyboard_msg"] = (
        await update.effective_chat.send_message(
            text="Для вызова меню используйте команду /menu. Для общения с GPT просто напишите мне сообщение."
        )
    )
