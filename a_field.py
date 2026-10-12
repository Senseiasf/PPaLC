goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

def field(items, *args):
    assert len(args) > 0
    
    if len(args) == 1:
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value
    else:
        for item in items:
            filtered_item = {key: item.get(key) for key in args if item.get(key) is not None}
            if filtered_item:
                yield filtered_item
if __name__ == '__main__':             
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))
