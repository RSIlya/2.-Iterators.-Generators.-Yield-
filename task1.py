
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

class FlatIterator:
    list_for_iterable = []

    def __init__(self, list_of_lists: list):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.extraction_from_list(self.list_of_lists)
        return self

    def __next__(self):
        if not self.list_for_iterable:
            raise StopIteration
        return self.list_for_iterable.pop(0)

    def extraction_from_list(self, origin_list):
        for item in origin_list:
            if isinstance(item, list):
                self.extraction_from_list(item)
                continue
            else:
                self.list_for_iterable.append(item)


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)