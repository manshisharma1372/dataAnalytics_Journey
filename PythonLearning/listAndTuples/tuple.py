tup1=(100,90,50,40,30,20) #class 'tuple'
print(type(tup1))

#immutable tuple
print(tup1[0]) #accessing elements using index
# tup[0]=1 tuple' object does not support item assignment

tup=() #empty tuple
print(tup) #()
#single val tuple
tip=(1,) #otherwise it will be considered int
print(tip)

#slcing
print(tup1[0:3]) #(100, 90, 50)

#****************METHODS********************************************************

#index : retunr index of first occ
print(tup1.index(90)) #1

#count:  count total occ
print(tup1.count(100)) #1
