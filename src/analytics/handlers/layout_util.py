from ..handlers.types.msg_data import MsgData
from ..constant.layout import layout

from src.util.log import logger


def get_msg_func(step: int, branch: str) -> callable:
    msg_funcs = layout.get(branch)
    if msg_funcs is None:
        raise RuntimeError(f"No such branch \"{branch}\" in layout")
    return msg_funcs[step]


async def enter_step(msg_data: MsgData, step: int, branch: str) -> None:
    logger.debug(f"STEP: user tgid={msg_data.tgid} entering: {branch=}, {step=}")
    state_data = await msg_data.state.get_data()
    
    messages_to_delete = state_data.get("report:messages_to_delete")
    if messages_to_delete is not None and messages_to_delete:
        await msg_data.msg.bot.delete_messages(chat_id=msg_data.tgid, message_ids=messages_to_delete)
    await msg_data.state.update_data({"report:messages_to_delete": []})
    
    await msg_data.state.update_data({"report:branch": branch, "report:step": step})
    msg_func = get_msg_func(step, branch)
    await msg_func(msg_data)


async def change_step(msg_data: MsgData, delta: int) -> None:
    state_data = await msg_data.state.get_data()
    step = state_data.get("report:step")
    if step is None:
        return
    next_step = step + delta
    await enter_step(msg_data, step=next_step, branch=state_data.get("report:branch"))


async def next_step(msg_data: MsgData) -> None:
    await change_step(msg_data, 1)
    
    
async def repeat_current_step(msg_data: MsgData) -> None:
    await change_step(msg_data, 0)
    
    
async def previous_step(msg_data: MsgData) -> None:
    await change_step(msg_data, -1)
    

    