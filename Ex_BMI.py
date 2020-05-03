height=float(input('Enter your height in meter:'))
weight=float(input('Enter your weight in kilogram:'))

bmi=weight/(height * height)

print('BMI is:',round(bmi,2))

if(bmi <= 18.5):
    print('underweight')
elif(bmi >= 18.5 and bmi <= 24.5):
    print('Normal weight')
elif(bmi >= 24.5 and bmi <= 29.9):
    print('Overweight')
else:
    print('Obsey')
