from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['Peptipedia']
col = db['activities']
update_col = db['activities']

for documento in col.find({}):
    if (documento['length'] != ''):
        update_col.update_one({
            '_id': documento['_id']
        },{
        '$set': {
        'length': int(float(documento['length']))
        }
        }, upsert=False)

db = client['Peptipedia']
col = db['peptides']
update_col = db['peptides']

for documento in col.find({}):
    if (documento['length'] != ''):
        update_col.update_one({
            '_id': documento['_id']
        },{
        '$set': {
        'length': int(float(documento['length']))
        }
        }, upsert=False)
