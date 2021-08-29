import os
import sys

folder = sys.argv[1]

# folder = os.getcwd()
names = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']
# files = [item for item in os.listdir(folder)]

os.mkdir(os.path.join(folder, names[0]))
os.mkdir(os.path.join(folder, names[0], names[1]))
os.mkdir(os.path.join(folder, names[0], names[2]))
os.mkdir(os.path.join(folder, names[0], names[3]))
os.mkdir(os.path.join(folder, names[0], names[4]))
