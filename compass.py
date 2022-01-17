facing = input()
turn_text = input()
turn = int(turn_text)

direction_list = [('N', 0), ('NE', 45), ('E', 90), ('SE', 135), ('S', 180),
             ('SW', 225), ('W', 270), ('NW', 315)]


def direction(facing, turn):
    idx = current_direction(facing)
    is_positive_turn = turn > 0
    if is_positive_turn is True:
        for i in range(int(turn/45)):
            idx += 1
            if idx == 8:
                idx = 0
    else:
        for i in range(int(abs(turn)/45)):
            idx -= 1
            if idx == -1:
                idx = 7
    return direction_list[idx][0]


def current_direction(facing):
    for index, key in enumerate(direction_list):
        if key[0] == facing:
            return index


direction(facing, turn)
