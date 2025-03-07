import json

links = []

def stream_links(data):
  if isinstance(data, dict):
    for key, value in data.items():
      if key == 'stream_link':
        links.append(value)
      else:
        links.extend(stream_links(value))
  elif isinstance(data, list):
    for item in data:
      links.extend(stream_links(item))
  return links




