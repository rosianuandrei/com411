print("Program Started")
user_input = input("Please enter a letter:")
print("you entered", user_input)

if (len(user_input) != 1):
    print("You were supossed to enter a single character only, you clever human")

else:
   print("Thank you, we will now process your input")
   print("ASCII code of", user_input, "is", ord(user_input))
   cod = ord(user_input) + 1
   print("The next character is", chr(cod))