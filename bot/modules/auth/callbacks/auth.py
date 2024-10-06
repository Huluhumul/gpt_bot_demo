from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from src.database import session_maker, User
from modules.auth import feathures, states
from modules.common import feathures as common_feathures


async def start(update: Update, context: CallbackContext) -> int:
    with session_maker() as session:
        user = session.query(User).filter_by(tg_id=update.effective_user.id).first()
        if user:
            await feathures.send_main_menu(update, context)
            return ConversationHandler.END
        else:
            await feathures.send_auth_message(update, context)
            return states.auth


async def share_contact(update: Update, context: CallbackContext) -> int:
    await common_feathures.delete_old_keyboard(context, update.effective_chat.id)

    contact = update.message.contact
    if contact.user_id != update.effective_chat.id:
        await update.effective_chat.send_message(
            text="Вы поделились чужим контактом, отправьте свой!"
        )
        return states.auth

    with session_maker() as session:
        user = User(
            tg_id=update.effective_user.id,
            username=update.effective_user.username,
            phone=contact.phone_number,
        )
        session.add(user)
        session.commit()

    await update.effective_chat.send_message(
        text="Вы успешно авторизовались в системе! Используйте команду /menu для вызова главного меню"
    )
    return ConversationHandler.END
