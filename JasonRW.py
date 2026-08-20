

import json;

path=r"C:\Users\KIMAYA\Desktop";


class JASON_WRITTE():
    def WriteData(self):
        person={ 
            "Name": "Akshay",
            "Ph Number": "9766656993",
            "Adress" :"Pune",
            "Age":25,
            "blood Group": "O+",
        }
        #json_data=json.dumps(person)

      
  


class JASON_READ():
    def ReadData(self):
        with open(path+"\gameConfig.json","r")as file:
            data=json.load(file);
            #print(data);

        foramted_data=json.dumps(data,indent= 4)#indent=4 म्हणजे JSON ला व्यवस्थित spacing आणि new lines देऊन readable format मध्ये दाखवणे.
        print(foramted_data);


class CREATEJSON_FILE():
    def __init__(self):
        gameData={
            "GAMENAME" : "GOLDEN ARCHERY",
            "GAMECOLOR":{
                "R":0.8,
                "Y":0.2,
                "G":0.9,
                "B":1.0,
                },
            "PRIZENUMBER":[
                {
                    "CURRENTPRIZENUMBER":"1",
                    "TARGET":["00","10","20","30","40"],
                    "WINAMT":"200000"
                },
                {
                    "CURRENTPRIZENUMBER":"2",
                    "TARGET":["50","60","70","80","90"],
                    "WINAMT":"500000"
                },
                {
                    "CURRENTPRIZENUMBER":"3",
                    "TARGET":["100","110","120","130","140"],
                    "WINAMT":"500000"
                },
                {
                    "CURRENTPRIZENUMBER":"4",
                    "TARGET":["150","160","170","180","190"],
                    "WINAMT":"500000"
                }
            ]
        }
        with open(path+"\GameData.json","w")as file:
            json.dump(gameData,file,indent=4)

        print("Json File is created")

        


#json.dumps() → Python → JSON string
# json.loads() → JSON string → Python
# json.dump() → Python → JSON file
# json.load() → JSON file → Python
    
            

class my_class(JASON_WRITTE,CREATEJSON_FILE,JASON_READ):#JASON_READ,
      print("-----------")
      
      
      

cls=my_class()
#cls.WriteData()
cls.ReadData()






