BMI (Body Mass Index), based on height and weight of a person. 
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

height = float(input("Enter your Hight in meters: "))
weight = float(input("Enter your weight in kilos: "))
  
bmi = weight / height **2 

if bmi < 19.5:
  print (f " {user_name} you are {user_age} years old. Your body mas is {bmi}. you are underweight. ")
    
elif bmi >= 19.5 and bmi <= 26: 
  print(f " {user_name} you are {user_age} years old. Your body mas is {bmi}.you are healthy. ")
    
elif bmi > 26: 
  print(f " {user_name} you are {user_age} years old. Your body mas is {bmi}. you are overweight. ")

