from datetime import timedelta, datetime

from telegram import Update
from telegram.ext import CallbackContext

from src.database import session_maker, User


async def add_time_to_subscription(
    update: Update, context: CallbackContext, time: int
) -> None:
    with session_maker() as session:
        user = session.query(User).filter_by(tg_id=update.effective_user.id).first()
        if user.subscription > datetime.now():
            user.subscription = user.subscription + timedelta(hours=time)
        else:
            user.subscription = datetime.now() + timedelta(hours=time)
        session.commit()
    await update.effective_chat.send_message("Подписка успешно продлена!")
