import requests
import csv
import json
from bs4 import BeautifulSoup

schoolCodes = []
schoolDataDict = []

def getSchoolData():
    link = "https://directory.ntschools.net/api/System/GetAllSchools"
    data = requests.get(link)
    parseData = json.loads(data.content)

    for i in parseData:
        schoolCodes.append(i["itSchoolCode"])

    link = "https://directory.ntschools.net/api/System/GetSchool?itSchoolCode="
    
    for i in range(51):
        schoolData = requests.get(link + schoolCodes[i])
        parseSchoolData = json.loads(schoolData.content)
        name = parseSchoolData["name"]
        try:
            physicalAddress = parseSchoolData["physicalAddress"]["description"] + parseSchoolData["physicalAddress"]["postCode"] + parseSchoolData["physicalAddress"]["state"]
            adminName = parseSchoolData["schoolManagement"][1]["firstName"] + " " + parseSchoolData["schoolManagement"][1]["lastName"]
            position = parseSchoolData["schoolManagement"][1]["position"]
            email = parseSchoolData["schoolManagement"][1]["email"]
            phone = parseSchoolData["schoolManagement"][1]["phone"]
            schoolDataDict.append({"Name":name, "Address":physicalAddress, "AdminName":adminName, "AdminPosition":position, "AdminEmail":email, "Phone":phone})
            print(f"Writing {schoolCodes[i]} to CSV")
        except Exception:
            print(f"{schoolCodes[i]} data not avalaible")

    with open('Q3.csv', mode='w') as school_writer:
        writer = csv.DictWriter(school_writer ,fieldnames=["Name", "Address", "AdminName", "AdminPosition", "AdminEmail", "Phone"])
        writer.writeheader()
        writer.writerows(schoolDataDict)
        print("\nData has been writed successfully in CSV File")

getSchoolData()