from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters

from modules.auth import callbacks, states


auth_handler = ConversationHandler(
    entry_points=[CommandHandler("start", callbacks.start)],
    states={
        states.auth: [
            MessageHandler(filters.CONTACT, callbacks.share_contact),
        ]
    },
    fallbacks=[],
    allow_reentry=True,
)
