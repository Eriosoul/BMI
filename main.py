weigh = float(input('Please insert your weight in KG'))
heigh = float(input('Please insert your heih in cm'))


total = weigh / (heigh**2)
if total <= 16:
    print('Severe Thinness')
    print('Your BMI is : {}'.format(total))
elif total > 17 and total <= 17.9:
    print('Moderate Thinness')
    print('Your BMI is : {}'.format(total))
elif total > 18 and total <= 18.4:
    print('Mild Thinness')
    print('Your BMI is : {}'.format(total))
elif total > 18.5 and total <= 25:
    print('Normal')
    print('Your BMI is : {}'.format(total))
elif total > 26 and total <= 30:
    print('Overweight')
    print('Your BMI is : {}'.format(total))
elif total > 31 and total <= 35:
    print('Obese Class I')
    print('Your BMI is : {}'.format(total))
elif total > 36 and total <= 40:
    print('Obese Class II')
    print('Your BMI is : {}'.format(total))
else:
    print('Obese Class III')
    print('Your BMI is : {}'.format(total))


# Overweight	25 - 30
# Obese Class I	30 - 35
# Obese Class II	35 - 40
# Obese Class III	> 40