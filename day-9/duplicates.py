some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = {key: some_list.count(key) for key in some_list if some_list.count(key) > 1}
print(duplicates)