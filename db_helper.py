from replit.database.database import ObservedList, ObservedDict
from replit import db
import json
class db_raw(object):
  def dict(self):
    findata = {}
    for key in db.keys():
      findata[key] = json.loads(db.get_raw(key)) if type(db[key]) == ObservedList or type(db[key]) == ObservedDict else db[key]
    return findata
  def __getitem__(self, key):
    return json.loads(db.get_raw(key)) if type(db[key]) == ObservedList or type(db[key]) == ObservedDict else db[key]
db_raw = db_raw()
