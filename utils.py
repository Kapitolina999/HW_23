from typing import Iterable


def slice_limit(data, limit):
    i = 0
    for item in data:
        if i < limit:
            yield item
        else:
            break
        i += 1


def query_builder(cmd, value, data: Iterable) -> Iterable:
    mapped_data = map(lambda v: v.strip(), data)

    if cmd == "unique":
        return set(mapped_data)

    if value:
        if cmd == "filter":
            return filter(lambda x: value in x, mapped_data)
        elif cmd == "map":
            return map(lambda x: x.split(' ')[int(value)], mapped_data)
        elif cmd == "limit":
            return slice_limit(mapped_data, int(value))
        elif cmd == "sort":
            return sorted(mapped_data, reverse=True if value == "desc" else False)

    return mapped_data


def get_cmd(query):
    del query["file_name"]
    buf = []
    for item in query.values():
        buf.append(item)
        if len(buf) == 2:
            yield buf
            buf = []


def do_query(data, items):
    result = list(data)
    for i in items:
        result = query_builder(*i, data=result)
    return result
