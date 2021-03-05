password = "hello"
user_input = input("Please enter your password: ")

attempt = 1

while(password !=user_input):
  atempt = attempt + 1
  user_input = input("WRONG! Attempt no " + str(attempt) + "Try Again: ")
  if(attempt > 3):
    print("LONG DELAY")
  if (attempt > 10):
    print("TERMINATE")  


print("wellcome")  
