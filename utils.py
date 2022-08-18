import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def get_data(file_name):
    try:
        with open(os.path.join(DATA_DIR, file_name), 'r') as file:
            return [i.rstrip('\n') for i in file.readlines()]
    except FileNotFoundError:
        return 'Файл не найден'


def limit(list_obj, num):
    return list_obj[:num]


def do_cmd(cmd: str, value:str, data: list) -> list:
    dict_cmd = {
        'map': map(lambda x: x.split(' ')[int(value)], data),
        'filter': filter(lambda line: value in line, data),
        'unique': set(data),
        'sort': sorted(data, reverse=True if value == 'desc' else True),
        'limit': limit(data, num=int(value) if value.isdigit() else 0)
    }

    return list(dict_cmd.get(cmd))


def do_query(data, query):
    result = data
    if 'cmd1' in query:
        result = do_cmd(query['cmd1'], query['value1'], data=result)
    if 'cmd2' in query:
        result = do_cmd(query['cmd2'], query['value2'], data=result)
    return result
