"""Start calculations route."""


from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from pricecalcbot.bot.callbacks.calcs import StartCalcsCallback
from pricecalcbot.bot.filters.extract_message import ExtractMessage
from pricecalcbot.bot.handler_result import HandlerResult, Ok
from pricecalcbot.bot.views.calcs.start import send_start_menu

router = Router(name='calcs/start')


@router.callback_query(
    StartCalcsCallback.filter(),
    ExtractMessage,
)
async def start_calcs(
    callback_query: CallbackQuery,
    message: Message,
    state: FSMContext,
) -> HandlerResult:
    """Send start message.

    Args:
        callback_query: Open menu query.
        message: Message where query from.
        state: Current FSM state.

    Returns:
        Always success.
    """
    await send_start_menu(message)
    await state.clear()
    return Ok()
