info={
    "name":"Adel",
    "ID": 57,
    "CGPA": 3.31,
    "Marks":[75,82,85,80,70],
    "cours":["Maath","EEE","DSA","DLD","HUM"],
    "is_passed":True,
}

print(info)
print(info["CGPA"])
print(info["Marks"])

#assined new values

info["CGPA"]=3.55
print(info)

#nested dictionary

Student={
    "information":{
    "name":"Adel",
    "ID": 57,
    "CGPA": 3.31,
    "Marks":[75,82,85,80,70],
    "cours":["Maath","EEE","DSA","DLD","HUM"],
    "is_passed":True
},
    "address":"Kotbari-Cumilla",
    "age":22,
    
}

print(Student)
print(Student["information"]["Marks"])


#methods in dictionary
print(Student.keys())
print(Student.values())
print(list(Student.values()))
print(list(Student.keys()))
print(Student.items())
print(list(Student.items()))
pairs=list(Student.items())
print(pairs[0])
print(pairs[1])
print(Student.get("information"))
print(Student.get("address"))
Student.update({"address":"Rampura-Mohanogor"})
print(Student.get("address"))

#empty dictionary operation

results={
    
}

results.update({"chem":78})
results.update({"phy":98})
results.update({"math":88})
results.update({"ethics":68})
results.update({"english":81})
print(results)

#set 

collection={1,2,2,3,"hellow","world","hellow"}
print(collection)
print(len(collection))
collection.add("fuckyou")
print(collection)
collection.remove("world")
print(collection)
print(collection.pop())
print(collection)
collection.clear()
print(collection)

#functions of set

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))

#touples in set

values={
    ("float",9.0),
    ("int", 9)
}
print(values)

