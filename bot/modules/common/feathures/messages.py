from telegram import Update
from telegram.ext import CallbackContext

from .keyboards import get_main_menu_keyboard


async def send_main_menu_main_page(update: Update, context: CallbackContext) -> None:
    context.user_data["old_keyboard_msg"] = (
        await update.effective_chat.send_message(
            text="Выберите действие",
            reply_markup=get_main_menu_keyboard(),
        )
    )
