print("Welcome to band name Generator")
city = input("what city are you from?\n")
food = input("Name of your favorite Food?\n")
#print("Name of your Band is " + city + " " + food)
bandname = "Name of you band can be {0} {1} or {1} {0}".format(city,food)
print(bandname)
