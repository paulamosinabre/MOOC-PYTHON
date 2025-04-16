num1 = int(input("Please type in a temperature (F): "))
cel = (num1-32) * 5/9
print(num1, "degrees Fahrenheit equals ", cel, "degrees Celsius")

if(cel < 0):
   print("Brr! It's cold in here!")
