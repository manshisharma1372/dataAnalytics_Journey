#sets

#collection of unordered items
#unique and set elm are immutatable but set are mutable
#cannot store list and dict in set

st={1,2,3}
print(st) #{1, 2, 3}

st1={1,1,1,2,3,5,5,5}
print(st1) #{1, 2, 3, 5} removed dup

print(len(st)) #3
print(len(st1)) #4 ignored dup

#empty set
st2={} # not this is dic not set
st2=set()
print(type(st2)) #<class 'set'>

#**********METHODS***************************************************8

#add() to add an elm
#remove() to remove an elm

st={1,2,3,4,5,6}
st.add(1)
st.add(8)
print(st) #{1, 2, 3, 4, 5, 6, 8}
st.remove(2)
print(st) #{1, 3, 4, 5, 6, 8}

st.add("manshi")
print(st) #{1, 3, 4, 5, 6, 8, 'manshi'}
ls=[1,2]
# st.add(ls) #TypeError: unhashable type: 'list'


#clear : empties set

st.clear()
print(st) #set()
print(len(st)) #0


#pop remove random val

st3={1,2,5,8,9,6}
st3.pop()
print(st3) #{2, 5, 6, 8, 9} randomly

#union : combines both set val and return new
#intersection :combines common val and return new set

st1={1,2,3,4,5,6}
st2={1,2,3,7,8,9,10,11,12}

fst=st1.union(st2)
print(fst) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

ust=st1.intersection(st2)
print(ust) #{1, 2, 3}


