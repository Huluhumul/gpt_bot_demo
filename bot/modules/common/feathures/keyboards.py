from telegram import InlineKeyboardButton, InlineKeyboardMarkup


async def delete_old_keyboard(context, chat_id):
    if context.user_data.get("old_keyboard_msg"):
        try:
            await context.bot.edit_message_text(
                text=context.user_data["old_keyboard_msg"].text,
                chat_id=chat_id,
                message_id=context.user_data["old_keyboard_msg"].message_id
            )
        except Exception:
            pass
        del context.user_data["old_keyboard_msg"]


def get_main_menu_keyboard():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Выбор GPT", callback_data="Выбор GPT")],
            [InlineKeyboardButton("Выбор роли GPT", callback_data="Выбор роли GPT")],
            [InlineKeyboardButton("Подписка", callback_data="Подписка")],
        ]
    )
