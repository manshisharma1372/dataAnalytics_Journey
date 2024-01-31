
#key value pairs
#unordered, mutable, no duplicate keys

dict={"name":"manshi", "age":18, "female":True}
print(dict)

dict1={"name":"mannu",
       "subjects":["hindi","english"],
       "num":(1,2,3)}
print(dict1)
print(type(dict1)) #<class 'dict'>

#no indexing

print(dict["name"])  #manshi
print(dict["age"])
#we get key error if key  is not present in the dictionary.

dict["name"]="mona" #overwrite
print(dict) #{'name': 'mona', 'age': 18, 'female': True}

#NESTING

student={
    "name":"manshi",
    "subjects":{
        "english":50,
        "phy":45,
        "math":50
    }
}
print(student)
print(student["subjects"]["phy"]) #45

#********************METHODS****************************************************************************888888

dic={
    "name":"manshi",
    "age":20,
    "branch":"IT"
}

# keys():return all keys
print(dic.keys()) #dict_keys(['name', 'age', 'branch']) list form

print(list(dic.keys())) #['name', 'age', 'branch']

print(len(dic)) #3

#values(): return all val in dict
print(dic.values()) #dict_values(['manshi', 20, 'IT'])
print(list(dic.values())) #['manshi', 20, 'IT']


#items() : returns key val pairs as tuple

print(dic.items()) #dict_items([('name', 'manshi'), ('age', 20), ('branch', 'IT')])
print(tuple(dic.items())) #(('name', 'manshi'), ('age', 20), ('branch', 'IT'))
pairs= list(dic.items())#[('name', 'manshi'), ('age', 20), ('branch', 'IT')]
print(pairs[0]) #('name', 'manshi')



#get() : return key according to value
print(dic["name"]) #manshi
print(dic.get("name")) #manshi
print(dic.get("surnname")) #None
# print(dic["surname"]) #error KeyError: 'surname'



#update insert item in dict
dic.update({"city":"delhi"})
print(dic) #{'name': 'manshi', 'age': 20, 'branch': 'IT', 'city': 'delhi'}

dic1 = {"id":1,"branch":"CS"}
dic.update(dic1)
print(dic) #{'name': 'manshi', 'age': 20, 'branch': 'CS', 'city': 'delhi', 'id': 1}  branch upadated 


