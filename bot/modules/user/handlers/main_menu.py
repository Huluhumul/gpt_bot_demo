from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)

from modules.user import callbacks, states


main_menu_handler = ConversationHandler(
    entry_points=[CommandHandler("menu", callbacks.main_page)],
    states={
        states.main_page_action: [
            # CallbackQueryHandler(callbacks.gpt_page, pattern=r"Выбор GPT"),
            CallbackQueryHandler(callbacks.gpt_role_page, pattern=r"Выбор роли GPT"),
            CallbackQueryHandler(callbacks.subscription_page, pattern=r"Подписка"),
        ],
        states.subscription_action: [
            CallbackQueryHandler(callbacks.back_to_main_page, pattern=r"Назад"),
            CallbackQueryHandler(callbacks.add_subscription, pattern=r"Получить 5ч подписки"),
        ],
        states.gpt_action: [
            CallbackQueryHandler(callbacks.back_to_main_page, pattern=r"Назад"),
            CallbackQueryHandler(callbacks.gpt_selection_page),
        ],
        states.gpt_select_role: [
            CallbackQueryHandler(callbacks.back_to_main_page, pattern=r"Назад"),
            CallbackQueryHandler(callbacks.gpt_role_selection_page),
        ],
        states.gpt_message: [
            CallbackQueryHandler(callbacks.back_to_main_page, pattern=r"Назад"),
            MessageHandler(filters.TEXT, callbacks.gpt_answer_page),
        ]
    },
    fallbacks=[],
    allow_reentry=True,
)
