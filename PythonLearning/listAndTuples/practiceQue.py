#wap to ask user to enter their names of their 3 fav movies and store them in a list

movie1=input("enter movie 1")
movie2=input("enter movie 1")
movie3=input("enter movie 1")
movie=[]
movie.append(movie1)
movie.append(movie2)
movie.append(movie3)
print(movie)

movies=[]
movies.append(input("enter movies"))
print(movies)

#wap to check if a list contains a palindrome of elm 
lst=[1,2,1]
lstCopy=lst.copy()
lstCopy.reverse()

if(lst==lstCopy):
    print("palindrome")
else:
    print("not palindrome")    #palindrome
    

#WAP to count number of students with a A grade in following tup
tup=("a","b","c","a","a","a")
print(tup.count("a")) #4

#store tup in list and sort from a to d
newList=["a","b","c","a","a","a"]
newList.sort()
print(newList) #['a', 'a', 'a', 'a', 'b', 'c']