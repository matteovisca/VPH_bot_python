
import json

def callback_for_action(action, params=None):
    # """
    # Generates an uglified JSON representation to use in ``callback_data`` of ``InlineKeyboardButton``.
    # :param action: The identifier for your action.
    # :param params: A dict of additional parameters.
    # :return:
    # """

    if params is None:
        params = dict()

    callback_data = {'a': action}
    if params:
        for key, value in params.items():
            callback_data[key] = value
    return callback_str_from_dict(callback_data)

def callback_str_from_dict(d):
    dumped = json.dumps(d, separators=(',', ':'))
    assert len(dumped) <= 64
    return dumped