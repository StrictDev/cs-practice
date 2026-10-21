def count_items(values: list) -> dict:
    dct = dict()

    for el in values:
        dct[el] = dct.get(el, 0) + 1

    return dct


def unique_sorted(values: list) -> list:
    return list(sorted(set(values)))


def common(first: list, second: list) -> list:
    return list(set(first) & set(second))


def only_in_first(first: list, second: list) -> list:
    return list(set(first) - set(second))
