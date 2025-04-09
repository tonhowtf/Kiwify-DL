import json
import os
import requests


def json(data):
  with open(data, 'r', encoding='utf-8') as f:
    return json.load(f)

def dir_creation(module_order, module_name, lesson_order, lesson_title):
  module_dir = f"{module_order:03d}_{module_name}"
  lesson_dir = f"{lesson_order:03d}_{lesson_title}"
  full_path = os.path.join(module_dir, lesson_dir)
  os.makedirs(full_path, exist_ok=True)
  return full_path

def download_file(url, path):
  r = requests.get(url, stream=True)
  if r.status_code == 200:
    with open(path, 'wb') as f:
      for chunk in r.iter_content(chunk_size=8192):
        if chunk:
          f.write(chunk)
      else:
        print(f"Não foi possivel baixar: {url}")
        .


  



