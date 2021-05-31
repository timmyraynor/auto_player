from unittest.mock import Mock
mock_player_action = Mock()


mock_player_action.find_touch_any.return_value = "friend_receive"

import sys
sys.modules['player'] = mock_player_action

from modules.utils import _act_with_clicks


def test_counter():
    counter={'value': 0}
    action_pool = []
    constructed_touch_seq = ['friend_receive', 'friend_receive2', 'friend_send']
    count_limits = 3
    seq = [
        {
            "name": [
                "friend_receive",
                "friend_receive2"
            ],
            "id": 1,
            "sleep": 1,
            "response": "接受友情点",
            "tick": False,
            "next": []
        },
        {
            "name": [
                "friend_send"
            ],
            "id": 2,
            "sleep": 1,
            "response": "发出友情点",
            "tick": True,
            "next": []
        }
    ]

    for x in range(1,3):
        _act_with_clicks(constructed_touch_seq, seq, counter, None, count_limits, seq, action_pool)

    assert counter['value'] == 3
    




if __name__ == "__main__":
    test_counter()