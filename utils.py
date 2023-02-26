import random


def convert_type(type: int) -> str:
    dict_type = {1: 'Basic',
                 2: 'Civil',
                 3: 'Rare',
                 4: 'Extra',
                 5: 'Exclusive'
                 }
    return dict_type.get(type, 'None')


def random_card(spot_pass: bool):
    if spot_pass:
        type_card = random.choices([1, 2, 3, 4, 5], weights=[50, 25, 15, 7, 3])
    else:
        type_card = random.choices([1, 2, 3, 4, 5], weights=[50, 25, 17, 9, 4])

    return type_card[0]