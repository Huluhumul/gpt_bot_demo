import json

import requests
from loguru import logger

import config


def refresh_token() -> None:
    url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"

    # Подготовка тела запроса в формате JSON
    body = json.dumps({"yandexPassportOauthToken": config.gpt_refresh_token})

    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, data=body, headers=headers)
    except Exception as e:
        logger.exception(f"Ошибка при обновлении токена: {e}")

    if response.status_code == 200:
        data = response.json()
        logger.info(f"Обновлен токен доступа к yandex gpt: {data}")
        config.gpt_token = data["iamToken"]
    else:
        logger.error(f"Не удалось обновить токен: {response.text}")
