
#Review 1

x= int(input('First Number: '))
y= int(input('Second Number: '))

for add in x,y:
    add= x+y
for multiply in x,y:
    multiply=x*y    
print('Your first value is:', add ) 
print ('Your second value is:',multiply)

#Review 2: If, elif and else statements!!
#Challenge! For every multiple of 2 print "Buzz", every multiple of 4
# print "Fizz", and for multiples of 2 and 4 print "FizzBuzz!".

for x in range(1, 20):
    if x%2==0 and x%4==0:
        print('Fizzbuzz!!')
    elif x%2==0:
        print('Buzz')
    elif x%4==0:
        print('Fizz')
    else:
        print(x)


#Review 3
Shoelist= ["Vans", "Nike", "Reebok", "Sketchers", "Adidas", "Puma!"]
Shoelist.append("New Balance")
Shoelist.sort()
print(Shoelist)
x= Shoelist[3]
print(x)
howmany = len(Shoelist)
print(howmany)
for brand in Shoelist:
   if brand == "Nike":
      Shoelist.remove(brand)
print(Shoelist)
entry = ""
Shoelist = ["Vans", "Nike", "Reebok", "Sneakers", "Sketchers", "Adidas", "Puma!"]
while entry != "Exit":
    entry = input('Add to list, or use the "exit" command: ')
    if entry != "Exit":
        Shoelist.append(entry)
        print(Shoelist)
Shoelist = ["Vans", "Nike", "Reebok", "Sneakers", "Sketchers", "Adidas", "Puma!"]
for each in Shoelist:
    if each == "vans":
        print("Vans")
    else:
        print(Shoelist)


#Review 4, try and except statements:
# Type in how much $$$ was spent at In N Out:
try:
  cost= float(input('How much money did you spend at In n Out?: '))
except:
   print('Your a dummy. Try again.')
else: 
    txt = "You paid ${:.2f} dollars at In N Out."
    print(txt.format(cost))
finally:
   print('Have a good day!')
  
# Review 5

import json
tiredict= {
             "brand": "Michelin",
             "composition": "Silica Rubber",
             "weight": "600 grams",
             "Wheel size": "26 inches",
             "Min Pressure": "29 PSI",
             "Max Pressure": "58 PSI",
             "Made In": "Thailand",
             "Tire Width": " 52mm"}

tiredict["Made In"] = "China"
tiredict["Threads per inch"]= "33"
del tiredict["Max Pressure"]

print(tiredict)
tiredictJson = json.dumps(tiredict)



# Review 6: Functions 
def unit_converter():
    print("1. Convert liters to gallons.")
    print("2. Convert gallons to liters. ")

def liters_gallons():
    liters= float(input("What is your volume in liters?")) 
    gallons= liters*0.264
    print("Your volume in gallons: {0}".format(gallons))

def gallons_liters():
    gallons= float(input("What is your volume in gallons?"))
    liters= gallons*3.785
    print(" Your volume in liters: {0}".format(liters))

unit_converter()
liters_gallons() 
gallons_liters()



