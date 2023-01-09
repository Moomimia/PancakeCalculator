# The recipe used for this program is as following
# 1 egg, 2.5dl milk , 1.25dl flour make 4 pancakes
# 0.25 egg, 0.625dl milk, 0.3125dl flour 
print("How much flour (dl) do you have?")
flour = float(input()) #take user input and store as decimal numb

print("How much milk (dl) do you have?")
milk = float(input())

print("How many eggs do you have?")
egg = float(input())


pancake_by_flour = flour/0.3125
pancake_by_milk = milk/0.625
pancake_by_egg = egg/0.25 

# print ("pancake limit " + str(pancake_by_flour))
# print ("pancake limit " + str(pancake_by_milk))
# print ("pancake limit " + str(pancake_by_egg))

smallest = 0

if pancake_by_flour < pancake_by_milk and pancake_by_flour < pancake_by_egg :
    smallest = pancake_by_flour
if pancake_by_milk < pancake_by_flour and pancake_by_milk < pancake_by_egg :
    smallest = pancake_by_milk
if pancake_by_egg < pancake_by_flour and pancake_by_egg < pancake_by_milk :
    smallest = pancake_by_egg
print("")
print(int(smallest), "is the amount of pancake you can make")
print("")
print ("Here's the recipe:")
print (str(0.3125 * smallest) + " dl of flour ")
print (str(0.625 * smallest) + " dl of milk ")
print (str(0.25 * smallest) + " egg ")
print ("Add a pinch of salt and sugar for better taste. Bon apetit :)")