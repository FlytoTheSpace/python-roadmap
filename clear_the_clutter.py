import os

files = os.listdir('./files/')

i = 1
for file in files:
    file_components = file.split('.')
    ext = file_components[len(file_components)-1]
    os.rename(f'./files/{file}', f'./files/{i}.{ext}')
    i += 1
    