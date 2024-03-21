from pymongo.mongo_client import MongoClient

from pymongo.server_api import ServerApi

#uri = "mongodb+srv://renato191108:KZ1qwEKOwE5A54hX@clusters-std-ads.6xwi1sb.mongodb.net/" #Renato  

# mongodb+srv://renato191108:KZ1qwEKOwE5A54hX@clusters-std-ads.6xwi1sb.mongodb.net/test 

#Edivaldo de Jesus uri = "mongodb+srv://edics122:Rg0am7NSBmb9hNjr@edivaldo0.vribdwl.mongodb.net/test" 

#uri = "mongodb+srv://edics122:Rg0am7NSBmb9hNjr @edivaldo0.vribdwl.mongodb.net/test" # EDIVALDO
#uri = "mongodb+srv://flavioadm:A1b2C3@provaheleno.fthmkx4.mongodb.net/test"
#uri = "mongodb+srv://mishiyaeru:1@cluster0.duqjftm.mongodb.net/?retryWrites=true&w=majoritY" #Vinicius Luis Nunes; Michael  
#uri = "mongodb+srv://guigamoraesmaciel:020219Vg@guigamoraes.4gwqhml.mongodb.net/test" # Guilherme
#uri = "mongodb+srv://arseniomendes20:Ams0210021@googleclouduniruy.fbxtwzh.mongodb.net/test" # Arsenio ok

#uri = "mongodb+srv://renato191108:KZ1qwEKOwE5A54hX@clusters-std-ads.6xwi1sb.mongodb.net/test"

#Mercia uri = "mongodb+srv://dneym:levimercia1234@cluster0.3qwamqc.mongodb.net/test"

#uri = "mongodb+srv://guigamoraesmaciel:020219Vg@guigamoraes.4gwqhml.mongodb.net/test" # Guilherme Maciel

uri = "mongodb+srv://edics122:Rg0am7NSBmb9hNjr@edivaldo0.vribdwl.mongodb.net/"  # edivaldo Filho

server_api = ServerApi('1')

try:

    client = MongoClient(uri, server_api=server_api)

    client.admin.command('ping')

    print("Sucesso na conexão com o banco de dados")

    client.close()
except Exception as e:

    print("Falha na conexão com o MongoDB:", e)