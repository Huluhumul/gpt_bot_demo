import requests
from telegram import Update
from telegram.ext import CallbackContext

import config
from . import keyboards
from src.database import session_maker, User


async def send_main_menu_subscription_page(
    update: Update, context: CallbackContext
) -> None:
    with session_maker() as session:
        user = session.query(User).filter_by(tg_id=update.effective_user.id).first()

        context.user_data["old_keyboard_msg"] = (
            await update.effective_chat.send_message(
                text=f"Дата и время окончания подписки: {user.subscription.strftime('%d.%m.%Y %H:%M')}",
                reply_markup=keyboards.get_subscriptions_keyboard(),
            )
        )


async def send_gpt_page(update: Update, context: CallbackContext) -> None:
    context.user_data["old_keyboard_msg"] = await update.effective_chat.send_message(
        text="Выберите модель для взаимодействия",
        reply_markup=keyboards.get_gpts_keyboard(context),
    )


async def send_gpt_role_page(update: Update, context: CallbackContext) -> None:
    context.user_data["old_keyboard_msg"] = await update.effective_chat.send_message(
        text="Выберите роль для GPT",
        reply_markup=keyboards.get_gpt_role_keyboard(context),
    )


async def ask_gpt_prompt(update: Update, context: CallbackContext) -> None:
    await update.effective_message.edit_text(
        text="Задайте интересующий вас вопрос к gpt",
        reply_markup=keyboards.get_back_keyboard(),
    )


async def edit_gpt_role_page(update: Update, context: CallbackContext) -> None:
    await update.effective_message.edit_text(
        text="Выберите модель для взаимодействия",
        reply_markup=keyboards.get_gpt_role_keyboard(context),
    )


async def gpt_answer(update: Update, context: CallbackContext) -> None:
    if not context.user_data.get("gpt_role"):
        context.user_data["gpt_role"] = "HR помощник по вакансии"
    api_url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Authorization": f"Bearer {config.gpt_token}",
        "x-folder-id": config.gpt_folder_id,
        "Content-Type": "application/json",
    }
    data = {
        "modelUri": f"gpt://{config.gpt_folder_id}/yandexgpt-lite",
        "completionOptions": {"stream": False, "temperature": 0.6, "maxTokens": "200"},
        "messages": [
            {
                "role": "system",
                "text": f"Ты: {context.user_data['gpt_role']}, в диалоге веди себя как {context.user_data['gpt_role']}",
            },
            {
                "role": "user",
                "text": update.message.text,
            },
        ],
    }
    try:
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            data = response.json()
            await update.effective_chat.send_message(
                data["result"]["alternatives"][0]["message"]["text"],
                parse_mode="MarkdownV2",
            )
            return
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Возникла ошибка: {e}")
    await update.effective_chat.send_message(
        "Не удалось сгенерировать ответ, попробуйте позже"
    )
