import pymongo
from pymongo import MongoClient

password = "<your MongoDB password goes here>"
dbname = "<your MongoDB cluster name goes here>"
#Paste the MongoDB connection link below. Format it in the same way i did
myclient = pymongo.MongoClient('<Your mongoDB atlas link goes here>'.format(password,dbname))
mydb = myclient["DataBase_Credentials"] #DatabaseName
mycol = mydb["Credentials"] #Cluster name

#Store Credentials
def storeCredentials(website,username,password):
  insert_credential = { "Website": website, "UserName": username, "Password":password }
  mycol.insert_one(insert_credential)
  print("All information fed!")

#Get Credentials
def getCredentials(website):
  myQuery = {"Website": website}
  my_information = mycol.find(myQuery)
  for cred in my_information:
    return ('Website: '+ cred["Website"]+ '\n' + 'Username: '+ cred["UserName"]+ '\n' + 'Password: '+ cred["Password"])




