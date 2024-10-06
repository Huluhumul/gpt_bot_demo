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

token = getenv("TOKEN")
gpt_token = getenv("GPT_API_KEY")
gpt_folder_id = "b1gum0tmqptetta039k2"
