def multiply(x,y):
    #This function multiplies 2 numbers
    return x*y

#take input from user
print("Select Room")
print("1. Main Bedroom")
print("2. Kitchen")
print("3. Guest Bedroom")
print("4. Main Living Room")
choice=input("1/2/3/4: ")
num1=int(input("Width: '"))
num2=int(input("Length: '"))


if choice == '1,2,3,4':
    print(multiply(num1,num2))
    
else: 
    print("Invalid Entry")

multiply(x,y)