import json

def json(data):
  with open(data, 'r', encoding='utf-8') as f:
    return json.load(f)



