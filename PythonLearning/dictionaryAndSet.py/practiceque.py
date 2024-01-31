# wap to store follwong word in python dict

dic={"table":["a piece of furniture","list of facts &figures"],
     "cat":"a small animal"}
print(dic)

# you are given list of subjects for students assume one classroom is required for 1 subject how many classrooms are needed by all students

st={"python","java","C++","python","javascript","java","python","java","C++","c"}
print(len(st))  #5

 # wap to enter marks of 3 subj from the user and store them in dict start with an empty dict and add one by one use subj name as key and marks as value
m1=input("enter marks of subj 1")
m2=input("enter marks of subj 2")
m3=input("enter marks of subj 3")

dict={}
dict.update({"subj1": m1})
dict.update({"subj2": m2})
dict.update({"subj3": m3})
print(dict) #{'subj1': '20', 'subj2': '50', 'subj3': '80'} 

#figure out way to store 9 and 9.0 as seperated val in set
st={9}
st.add("9.0")
print(st) #{9, '9.0'}

#use built in data type

values={
    ("float",9.0),
    ("int",9)
}
print (values) #{('float', 9.0), ('int', 9)}