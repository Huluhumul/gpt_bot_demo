from telegram import Update
from telegram.ext import CallbackContext

from modules.user import states, feathures
from modules.common import feathures as common_feathures


@feathures.access_decorator
async def main_page(update: Update, context: CallbackContext) -> None:
    await common_feathures.delete_old_keyboard(context, update.effective_chat.id)
    await common_feathures.send_main_menu_main_page(update, context)
    return states.main_page_action


async def gpt_page(update: Update, context: CallbackContext) -> None:
    await common_feathures.delete_old_keyboard(context, update.effective_chat.id)
    await feathures.send_gpt_page(update, context)
    return states.gpt_action


async def gpt_role_page(update: Update, context: CallbackContext) -> None:
    await common_feathures.delete_old_keyboard(context, update.effective_chat.id)
    await feathures.send_gpt_role_page(update, context)
    return states.gpt_select_role


async def subscription_page(update: Update, context: CallbackContext) -> None:
    await common_feathures.delete_old_keyboard(context, update.effective_chat.id)
    await feathures.send_main_menu_subscription_page(update, context)
    return states.subscription_action


@feathures.access_decorator
async def gpt_conversation(update: Update, context: CallbackContext) -> None:
    await feathures.gpt_answer(update, context)


async def back_to_main_page(update: Update, context: CallbackContext) -> None:
    await common_feathures.delete_old_keyboard(context, update.effective_chat.id)
    return await main_page(update, context)


async def gpt_selection_page(update: Update, context: CallbackContext) -> None:
    context.user_data["gpt_version"] = update.callback_query.data
    await feathures.edit_gpt_page(update, context)


async def gpt_role_selection_page(update: Update, context: CallbackContext) -> None:
    context.user_data["gpt_role"] = update.callback_query.data
    await feathures.edit_gpt_role_page(update, context)
