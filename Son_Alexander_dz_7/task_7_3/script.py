import os
import shutil

tree = os.walk(r'C:\Users\Александр\Desktop\Homework\Son_Alexander_dz_7\task_7_3\my_project')
data = []
print(tree)

# try:
#     os.mkdir('templates')
# except FileExistsError:
#     pass

for i in tree:
    if i[2] == ['base.html', 'index.html']:
        folder = i[0].split('\\')
        folder.pop()
        need_to_copy = '\\'.join(folder)
        shutil.copytree(need_to_copy, 'templates', dirs_exist_ok=True)
