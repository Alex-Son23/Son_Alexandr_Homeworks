import os

folder = 'some_data'
size_data = {}
draft_dictionary = {}

file_max_size = 0

for i in os.listdir(folder):
    statinfo = os.stat(os.path.join(folder, i))
    file_size = statinfo.st_size
    key_size = int('1' + len(str(file_size)) * '0')
    if draft_dictionary.setdefault(key_size) is None:
        draft_dictionary[key_size] = 0
        draft_dictionary[key_size] += 1
    else:
        draft_dictionary[key_size] += 1

for i in sorted(draft_dictionary):
    size_data[i] = draft_dictionary[i]


print(size_data)

