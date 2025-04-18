from ..handlers.msg.messages import department_msg, branch_msg, type_msg, period_msg, menu_msg


layout = {
    "enter_department": [
        department_msg, 
        branch_msg
    ],
    "revenue": [
        lambda msg_data: period_msg(msg_data, [0, 1, 2, 3, 4, 5, 6]), 
        lambda msg_data: menu_msg(msg_data, [0, 1, 3, 4, 5])
    ],
    "writeoff": [
        lambda msg_data: type_msg(msg_data, [3, 4]), 
        lambda msg_data: period_msg(msg_data, [1, 2, 3, 4, 5, 6]), 
        lambda msg_data: menu_msg(msg_data, [0, 2, 4, 5])
    ],
    "losses": [
        lambda msg_data: type_msg(msg_data, [0, 1]), 
        lambda msg_data: period_msg(msg_data, [2, 5]),
        lambda msg_data: menu_msg(msg_data, [0, 2, 4, 5])
    ],
    "foodcost": [
        lambda msg_data: type_msg(msg_data, [2, 5]), 
        lambda msg_data: period_msg(msg_data, [1, 2, 3, 4, 5, 6]), 
        lambda msg_data: menu_msg(msg_data, [0, 1, 3, 4, 5])
    ],
    "turnover": [
        lambda msg_data: period_msg(msg_data, [1, 2, 3, 4, 5, 6]), 
        lambda msg_data: menu_msg(msg_data, [0, 1, 2, 4, 5])
    ],
}
