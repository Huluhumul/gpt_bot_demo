import requests
from loguru import logger

import config


def refresh_token() -> None:
    api_url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    headers = {
        "Content-Type": "Application/json",
    }
    data = {
        "yandexPassportOauthToken": config.gpt_refresh_token,
    }
    try:
        response = requests.post(api_url, headers=headers, data=data)
    except Exception as e:
        logger.exception(f"Ошибка при обновлении токена: {e}")

    if response.status_code == 200:
        data = response.json()
        logger.info(f"Обновлен токен доступа к yandex gpt: {data}")
        config.gpt_token = data["iamToken"]
    else:
        logger.error(f"Не удалось обновить токен: {response.text}")
