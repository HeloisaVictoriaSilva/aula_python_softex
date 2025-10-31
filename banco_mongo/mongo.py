import pymongo

cliente = pymongo.MongoClient('')

banco= cliente["bancoloja"]
usuario= banco["mesa"]
doc = {'nome': 'alice'}
usuario.insert_many(doc)
#usuario.find_one{'nome':'alice'}