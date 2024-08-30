# #create a print function that prints "Hello World"
# # print("Hello, World")
# # #ask user for day of the week
# # day_week = input("What day of the week is it? ")
# # print("Today is " + day_week)
# # #concatenation is when you add two strings together
# # # #using a + sign
# # movies_this_week = input ("What movies are you watching this week? ")
# # print("I am watching " + movies_this_week + " this week.")
# # mood = input("How are you feeling today? ")
# # print("I am feeling " + mood)

# #data types for variables in python
# #strings - text
# name = "John" #this is a string data type
# #whenever it is wrapped in quotes, it is a string
# year = "2024"
# #integers - whole numbers
# year = 2024 #this is an integer data type
# #do NOT wrap it in quotes
# yearFourfromNow = 2028
# subtract = yearFourfromNow - year
# print(subtract)
# #floats - decimal numbers
# priceBigMac = 3.99
# priceDoublePounder = 4.99
# totalPrice = priceBigMac + priceDoublePounder
# print(totalPrice)
# #booleans - True or False
# isRaining = False
# print(isRaining)
# #lists - a collection of items\
# groceries = ["apples", "bananas", "carrots"]
# print(groceries)
#challenge #1
#list of movies
moviesList = ["Deadpool 2","Inside Out 2","Despicable Me 4"]
print(moviesList)
#the name of the movie
movieName = "Deadpool 2"
#time of the movie
movieTime = "3:15pm"
#price of the movie
moviePrice = 29.35
#address of the dinner
restAddress = "6273 71st Street"
#time of dinner
restTime = "7:45pm"
#price of dinner
dinnerPrice = 195.78
#check to see if the movie is playing in evening
inEvening = False
#amount of people going
peopleGoing = (input("How many people are going? "))
#type conversion converting from one data type to another
#print the entire output
print("We are going to see " + movieName + " at " + movieTime + " and eat dinner at " + restAddress + " at " + restTime + " with " + peopleGoing + "people")
