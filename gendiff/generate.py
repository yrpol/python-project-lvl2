import json


def read_path(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def normalize(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    else:
        return value


def generate_diff(filename1, filename2, output):
    '''Generate diff'''
    difference = '{\n'

    json_first = read_path(filename1)
    json_second = read_path(filename2)

    all_keys = set(list(json_first.keys()) + list(json_second.keys()))

    for key in sorted(all_keys):
        result_string = ''
        first = normalize(json_first.get(key, None))
        second = normalize(json_second.get(key, None))

        if first == second:
            result_string = '    {}: {}\n'.format(key, first)
        elif first is None:
            result_string = '  + {}: {}\n'.format(key, second)
        elif second is None:
            result_string = '  - {}: {}\n'.format(key, first)
        elif first != second:
            result_string = '  - {}: {}\n'.format(key, first)
            result_string += '  + {}: {}\n'.format(key, second)

        difference += result_string

    return difference[:-1] + '\n}'
