import os
import json

folder = 'some_data'
size_data = {}
draft_dictionary = {}

file_max_size = 0

for i in os.listdir(folder):
    statinfo = os.stat(os.path.join(folder, i))
    file_size = statinfo.st_size
    key_size = int('1' + len(str(file_size)) * '0')
    if draft_dictionary.setdefault(key_size) is None:
        draft_dictionary[key_size] = []
        draft_dictionary[key_size].append(1)
        try:
            extension = i.split('.')[1]
            draft_dictionary[key_size].append([extension])
        except Exception:
            None
    else:
        draft_dictionary[key_size][0] += 1
        try:
            extension = i.split('.')[1]
            for i in draft_dictionary[key_size][1]:
                if i == extension:
                    break
            draft_dictionary[key_size][2].append(extension)
        except Exception:
            None

for i in sorted(draft_dictionary):
    size_data[i] = draft_dictionary[i]
    size_data[i] = tuple(size_data[i])

with open('some_data_summary.json', 'w', encoding='UTF-8') as f:
    size_data_json = json.dumps(size_data)
    f.write(size_data_json)


print(size_data)