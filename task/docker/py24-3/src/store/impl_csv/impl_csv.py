import csv
import time
from store.store import image_store

"""
structure of csv file

id,title

"""

# Errors
ErrImageNotFound = Exception("image not found")
ErrImageAlreadyExists = Exception("image already exists")

# Implementation of image_store
class ImageStore(image_store):
  def __init__(self, path:str):
    self.path = path
  def get_all(self) -> [list,Exception]:
    try:
      with open(self.path) as file:
        render = csv.reader(file)
        return [row for row in render], None
    except Exception as err:
      return None, err
  def get_by_id(self, id:str) -> [str,Exception]:
    try:
      with open(self.path) as file:
        render = csv.reader(file)
        for row in render:
          if row[0] == id:
            return row, None
        return None, ErrImageNotFound
    except Exception as err:
      return None, err
  def create(self, id:str ,title:str) -> Exception:
    _ ,err = self.get_by_id(id)
    if err == ErrImageNotFound:
      try:
        with open(self.path, "a") as file:
          writer = csv.writer(file)
          writer.writerow([id, title, time.time()])
        return None
      except Exception as err:
        return err
    else:
      return ErrImageAlreadyExists
  # def update(self) -> Exception:
  #   return self.csv.update()
  def delete_all(self) -> Exception:
    try:
      with open(self.path, "w") as file:
        file.write("")
      return None
    except Exception as err:
      return err
  
  def delete_by_id(self, id:str) -> Exception:
    try:
      with open(self.path, "w") as file:
        render = csv.reader(file)
        for row in render:
          if row[0] != id:
            writer = csv.writer(file)
            writer.writerow(row)
      return None
    except Exception as err:
      return err