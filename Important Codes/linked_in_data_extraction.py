import json
import requests

# making request to get data 
url = "https://linkedin-profiles-and-company-data.p.rapidapi.com/profile-details"

username = "akshay-singh-elite"

payload = {
	"profile_id": username,
	"profile_type": "personal",
	"contact_info": False,
	"recommendations": False,
	"related_profiles": False
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "4057d2be1dmshf1fdeb188359618p151c1djsnae9faca23c70",
	"X-RapidAPI-Host": "linkedin-profiles-and-company-data.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

# convert json to python dict 
json_obj = json.loads(response.content)
# print(type(json_obj))
# print(json.dumps(json_obj, indent = 3))

# Creating new dict to save data in more understandable form 
data_dic = {}

data_dic["Name"] = json_obj["first_name"] + " " + json_obj["last_name"]
data_dic["Summary"] = json_obj["summary"]

# divide skills into language, frameworks, other 
lang = ["c","c++","java","python","javascript","kotlin","html","css","html5","css3","php","r"]
liby_and_fram = ['bootstrap','django']
other = ["microsoft powerPoint","microsoft office","adobe photoshop"]
temp = {'language' : [], 'library_and_framework' : [] , 'other' : []}
for i in json_obj["skills"]:
    if i.lower() in lang:
        temp["language"].append(i)
    elif i.lower() in liby_and_fram:
        temp["library_and_framework"].append(i)
    elif i.lower() in other:
        temp["other"].append(i)
temp["language"].sort()
temp["library_and_framework"].sort()
temp["other"].sort()
data_dic['skills'] = temp

# Extract Education 
edu_dic = []
for i in json_obj["education"]:
    temp_edu = {}
    temp_edu["Degree"] = i["degree_name"] + ", " + i["field_of_study"]
    temp_edu["College"] = str(i["school"]["name"]) + " (" + str(i["date"]["start"]["year"]) + " - " + str(i["date"]["end"]["year"]) + ")"
    edu_dic.append(temp_edu)

data_dic["Education"] = edu_dic




# print data_dic for testing
print(json.dumps(data_dic, indent = 3))