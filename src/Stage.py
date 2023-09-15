from pymongo import MongoClient

class Stage:
    cnx = MongoClient("localhost",27017)
    db = cnx["db_stage"]
    stages_collection = db["stages"]

    def __init__(self,id:int,name:str,duration:int,price:float,domain:str) -> None:
        self.id = id
        self.name= name
        self.duration = duration
        self.price = price
        self.domain = domain
    
    def getAllData():
        res = list(Stage.stages_collection.find().sort("id"))
        return res

    def findById(id):
        return Stage.stages_collection.find_one({"id":id})
    

    def findByDomain(domain):
        res = Stage.stages_collection.aggregate([{"$match":{"domain":domain}},{"group":{"_id":domain,"countItems":{"$sum":1}}}])
    
    def AddToData(self):
        Stage.stages_collection.insert_one({"id":self.id,"name":self.name.capitalize(),"duration":self.duration,"price":self.price,"domain":(self.domain).upper()})
    
    def GetAllIds()->list:
        data = Stage.getAllData()
        ids = list(map(lambda item:item["id"],data))
        return ids

    def deleteById(id):
        Stage.stages_collection.delete_one({"id":id})

    def UpdateData(id,data:dict):
        Stage.stages_collection.update_one({"id":id},{'$set':data})
    def ListDomains ()->list:
        res = Stage.stages_collection.distinct("domain")
        return res

