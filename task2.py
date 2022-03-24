
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]

def flat_generator(target_list):
    for item in target_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item

for item in flat_generator(nested_list):
    print(item)

flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)