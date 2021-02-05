some_list = ['a', 'b', 't', 'e', 'u', 'o', 'p', 'b', 'e', 'm']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)