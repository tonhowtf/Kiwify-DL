import json

def stream_links(data):
  if isinstance(data, dict):
    for key, value in data.items():
      if key == 'stream_link':
        print(value)
      else:
        stream_links(value)
  elif isinstance(data, list):
    for item in data:
      stream_links(item)

def debug(file):
  with open(file, 'r', encoding='utf-8') as file:
    data = json.load(file)
    stream_links(data)

debug('data.json')

