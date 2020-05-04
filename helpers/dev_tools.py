
def list_dump(_l, _filter=None):
    for item in _l:
        if (_filter is None) or _filter(item):
            print(item)
    print()
