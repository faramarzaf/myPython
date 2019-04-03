def bmi_calc():
        height = input('Insert your height [Centimeter]: ')
        height = float(height)

        weight = input('Insert your weight [Kilogram]: ')
        weight = float(weight)

        H_2 = height*height
        W_2 = weight

        bmi = W_2/H_2

        if bmi < 18.5:
                print('You are underweight')

        elif bmi > 18.5 and bmi < 24.9:
                print('You are normal')

        elif bmi > 25 and bmi < 29.9:
                print('You are overweight')

        else:
                print('You are obese')

print('Welcome to the BMI system')
bmi_calc()
soal = input('Do you want to continue?[y/n]: ')
while soal != 'n':
        bmi_calc()
        soal = input('Do you want to continue?[y/n]: ')