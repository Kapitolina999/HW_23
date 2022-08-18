import os


def get_data(path, file_name):
    try:
        with open(os.path.join(path, file_name), 'r') as file:
            return [i.rstrip('\n') for i in file.readlines()]
    except FileNotFoundError:
        return 'Файл не найден'


def limit(list_obj, num: int) -> list:
    return list_obj[:num]


def do_cmd(cmd: str, value: str, data: list) -> list:
    dict_cmd = {
        'map': map(lambda x: x.split(' ')[int(value)], data),
        'filter': filter(lambda line: value in line, data),
        'unique': set(data),
        'sort': sorted(data, reverse=True if value == 'desc' else True),
        'limit': limit(data, num=int(value) if value.isdigit() else 0)
    }

    return list(dict_cmd.get(cmd))


def get_cmd(query):
    del query['file_name']
    buf = []
    for item in query.values():
        buf.append(item)
        if len(buf) == 2:
            yield buf
            buf = []


def do_query(data: list, chunk) -> list:
    result = data
    for i in chunk:
        result = do_cmd(*i, data=result)
    return result