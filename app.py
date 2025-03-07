import json

def stream_links(data):
  if isinstance(data, dict):
    for key, value in data.items():
      if key == 'stream_link':
        print(value)
      else:
        stream_links(value)

