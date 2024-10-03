from os import getenv


logs_path = getenv("LOGS_PATH")

db_connect_data = {
    "drivername": "postgresql",
    "host": getenv("POSTGRES_HOST"),
    "port": getenv("POSTGRES_PORT"),
    "username": getenv("POSTGRES_USER"),
    "password": getenv("POSTGRES_PASSWORD"),
    "database": getenv("POSTGRES_DB"),
}

token = getenv("TELEGRAM_TOKEN")
