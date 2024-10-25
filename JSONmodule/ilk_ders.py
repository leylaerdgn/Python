import json
person_string='{"name":"Ali", "languages":["python","C#"]}'
#LOADS()
#result=json.loads(person_string)
#result=result["languages"]

#LOAD()
#with open("person.json") as f:
#    data=json.load(f)
#    print(data)

#DUMPS()
person_dict={
    "name":"Leyla",
    "languages":["python","java"]
}
#result=json.dumps(person_dict)

#DUMP()
with open("person.json","w") as f:
    json.dump(person_dict,f)
#print(result)