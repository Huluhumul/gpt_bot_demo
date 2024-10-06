from telegram import Update
from telegram.ext import CallbackContext

from src.database import session_maker, User


def access_decorator(func):
    async def inner(update: Update, context: CallbackContext):
        with session_maker() as session:
            user = session.query(User).filter_by(tg_id=update.effective_user.id).first()
            if user:
                return await func(update, context)
            else:
                await update.effective_chat.send_message(
                    text="Сначала нужно зарегистрироваться в системе, используйте команду /start"
                )

    return inner
