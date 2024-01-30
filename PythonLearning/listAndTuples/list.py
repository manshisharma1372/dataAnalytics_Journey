#list
marks=[100,99,55,60,70,80]
print(marks)
print(type(marks)) #class 'list'

#accessing the elements of list using index
print(marks[0]) #100

#we can store elm of diff type
student=["Manshi",155,"IT",92.2]
print(student) #['Manshi', 155, 'IT', 92.2]

#note string are immutable and list are mutable in python
str="hello"
print(str[0])
# str[0]="j" NOT allowed

student[0]="mannu"
print(student)
# print(student[4]) list index out of range

#slicing in list
print(student[0:2]) #['mannu', 155] ending index not included
print(student[0:])

#negative indexing
print(student[-3:-1]) #[155, 'IT']

#*********************************************************************************
# List methods

lst=[1,2,3]
#append: add one elm at end called mutating list
lst.append(4)
print(lst) #[1, 2, 3, 4]

#sort : sorts in ascending order
lst.sort()
print(lst.sort()) #None
lst.sort(reverse=True) #[4, 3, 2, 1]
print(lst)

lst2=["apple","mango","lichi"]
lst2.sort()
print(lst2) #['apple', 'lichi', 'mango']

lst.reverse()
print(lst) #1, 2, 3, 4]

#insert: to insert elm at index
lst2.insert(2,"banana")
print(lst2) #['apple', 'lichi', 'banana', 'mango']

#remove: removes first occ of elm
lst.remove(3)
print(lst) #[1, 2, 4]

#pop remove elem
lst.pop(2)
print(lst) #[1, 2]

