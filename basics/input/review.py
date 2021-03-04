# Ask user to enter their name
print("What is your name human?")
name = input()
print("It is nice to meet you human", name)
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
# Ask user for eye character 
print("Please enter eye character")
eye = input() 

# Display an ascii art robot
print("##########")
print("#  " + eye + "  " + eye + "  #")
print("#  ----  #")
print("##########")
print("Please enter the number of lives.")
lives = int(input())
print("Please enter the energy level.")
energy = int(input())
print("Please enter the shield level. ")
shield = int(input())
# Display bot data
print("Lives:", "♥" * lives)
print("Energy:", "♦" * energy)
print("Shield:", "♦" * shield)