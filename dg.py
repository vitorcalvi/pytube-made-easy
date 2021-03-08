from tinydb import TinyDB, Query
db = TinyDB('./db/db.json')

db.insert({'int': 1, 'char': 'a'})


