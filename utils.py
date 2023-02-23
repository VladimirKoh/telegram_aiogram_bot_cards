def convert_type(type: int) -> str:
    dict_type = {1: 'Basic',
                 2: 'Civil',
                 3: 'Rare',
                 4: 'Extra',
                 5: 'Exclusive'
                 }
    return dict_type.get(type, 'None')