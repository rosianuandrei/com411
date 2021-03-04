print("What is your name human?")
name = input()
print("How old are you?")
age = int(input())
print("How tall are you?")
height = float(input())
print("How much do you weigh?")
weight = float(input())
# Calculate bmi
bmi = weight / (height ** 2)

# Display result
print(name, "your bmi is", bmi)
