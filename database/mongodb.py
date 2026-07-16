from pymongo import MongoClient 

try:
    MONGO_URI =  "mongodb+srv://gulshansarath001_db_user:Gulshan%401234@cluster0.94iwbyi.mongodb.net/?appName=Cluster0"

    client = MongoClient(MONGO_URI)
    
    client.admin.command("ping")

    db=client["ssus123"]

    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection=db["attendance"]
    bmi_collection=db["bmi_reports"]

    print ("Mongodb Connection Successfully")
except Exception as e:
    print ("MongoDB Error",e)
