import yaml

with open('../data/data.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f)
    print(data)
