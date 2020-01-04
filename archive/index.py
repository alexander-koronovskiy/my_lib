import json

data = {11028522: 2, 46042277: 17, 398612226: 1033}

# Сохраняем словарь в файл
with open('data.json', 'w') as f:
    f.write(json.dumps(data))

# Читаем словарь из файла
with open('data.json', 'r') as f:
    data_new = json.loads(str(f.read()))

print(data_new.keys())
