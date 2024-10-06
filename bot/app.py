

from loguru import logger

from modules import auth
from modules import user
from src.telegram_api import app


if __name__ == "__main__":
    logger.info("Inializing complete, bot starting")
    app.add_handler(auth.auth_handler)
    app.add_handler(user.main_menu_handler)
    app.run_polling()
