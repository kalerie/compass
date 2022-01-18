facing = input("Type your current facing: ")
turn = input("Type turn: ")


direction_list = [('N', 0), ('NE', 45), ('E', 90), ('SE', 135), ('S', 180),
             ('SW', 225), ('W', 270), ('NW', 315)]


def direction(facing, turn_str):
    input_validation(facing, turn_str)
    idx = current_direction(facing)
    turn = int(turn_str)
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
    print(direction_list[idx][0])
    return direction_list[idx][0]


def current_direction(facing):
    for index, key in enumerate(direction_list):
        if key[0] == facing:
            return index


def input_validation(facing, turn):
    valid_facing = [k[0] for k in direction_list]
    if facing not in valid_facing:
        raise TypeError('Only ' + str(valid_facing) + ' are allowed for "facing" argument')

    try:
        int(turn)
    except:
        raise TypeError('Only integer are allowed for "turn" argument')

    if int(turn) % 45 != 0 or int(turn) == 1 or int(turn) == -1:
        raise ValueError('Only integer that multiple of 45 are allowed for "turn" argument')

direction(facing, turn)
