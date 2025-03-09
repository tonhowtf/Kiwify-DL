import json
import os


def json(data):
  with open(data, 'r', encoding='utf-8') as f:
    return json.load(f)

def dir_creation(module_order, module_name, lesson_order, lesson_title):
  module_dir = f"{module_order:03d}_{module_name}"
  lesson_dir = f"{lesson_order:03d}_{lesson_title}"
  full_path = os.path.join(module_dir, lesson_dir)
  os.makedirs(full_path, exist_ok=True)
  return full_path





