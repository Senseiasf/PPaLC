from gen_random import gen_random  

class Unique(object):
    def __init__(self, items, **kwargs):
        self.iterator = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.iterator)
            if self.ignore_case and isinstance(item, str):
                check_value = item.lower()
            else:
                check_value = item
            if check_value not in self.seen:
                self.seen.add(check_value)
                return item

    def __iter__(self):
        return self

if __name__ == '__main__':    
    data = gen_random(10,1,3)
    print(list(Unique(data)))
    data1 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data1)))
    print(list(Unique(data1, ignore_case=True)))