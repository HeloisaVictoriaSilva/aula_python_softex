import pymongo

#localhost
conn = pymongo.MongoClient("mongodb://localhost:27017/")

#print(conn.list_database_names())

banco = conn["loja"]
cliente = banco["users"]
cliente.insert_one({"nome":"heloisa", "idade":20, "endereço":{"cep": 51230490, "logadouro":"Rua jet jackson", "numero": 380, "referencia": None}})
print(conn.list_database_names())
