height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
msg = f"Your BMI is: {bmi}"

def bmi_2(bmi): 

    if bmi < 18.5:
        return msg + " you are underweight"
    elif bmi < 25:
        return msg + " you are normal weight"
    elif bmi < 30:
        return msg + " you are slightly overweight"
    elif bmi < 35:
        return msg + " you are obese"
    elif bmi > 35:
        return msg + " you are clinically obese"
    else: 
        return 'incorrect input'

print(bmi_2(bmi))




