BMI calculator, based on height, weight and gender of a person. 

user_name=input("Enter your name: ")
user_gender=input("For female, enter F: otherwise enter M: ")

height=float(input("Enter your Hight in meters: "))
weight=float(input("Enter your weight in kilos: "))
  
bmi = weight / height **2 

if user_gender == "F":
  if bmi < 19.5:
    print (f"{user_name}. Your body mas is {bmi}. You are underweight")
  elif bmi >= 19.5 and bmi <= 26: 
    print(f"{user_name}. Your body mas is {bmi}. You are healthy")   
  elif bmi > 26: 
    print(f" {user_name}. Your body mas is {bmi}. You are overweight")

if user_gender == "M":
  if bmi < 18.5:
    print (f"{user_name}. Your body mas is {bmi}. You are underweight")
  elif bmi >= 18.5 and bmi <= 25: 
    print(f"{user_name}. Your body mas is {bmi}. You are healthy")   
  elif bmi > 25:
    print(f"{user_name}. Your body mas is {bmi}. You are over-weight.")
print("\n\n\t\t! programe is finished !")
