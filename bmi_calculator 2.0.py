# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
BMI=round(weight/height**2)

if(BMI<18.5):
  print(f"your bmi is {BMI},you are underweight")
elif(BMI<25) :
  print(f"your bmi is {BMI},you are normal weight") 
elif(BMI<30) :
  print(f"your bmi is {BMI},you are Slightly overweight") 
elif(BMI<=35) :
  print(f"your bmi is {BMI},you are obese") 
else:
  print(f"your bmi is {BMI},you are Clinically obese")  

    




