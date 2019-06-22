#Mark A
#11-14-2013

#4_10 Pg 155 Body Mass Index

#Collect Height and Weight of person.
def Input():
    Weight = int(input('Enter your weight in pounds: '))
    Height = int(input('Enter your heigth in inches: '))

    Calculation(Weight, Height)

#Calculate BMI.
def Calculation(Weight, Height):
    BMI = Weight * 703 / (Height * Height)

    Display(BMI)

#Display wether the BMI is to low, to high, or on target goal.
def Display(BMI):

    if BMI < 18.5:
        print('Your BMI is',format (BMI, '.2f'),' and is considered to be under weight.')

    elif BMI > 25:
        print('Your BMI is',format (BMI, '.2f'),' and is considerd to be over weight.')

    elif BMI >= 18.5 and BMI <= 25:
        print('Your BMI is',format (BMI, '.2f'),' and is considerd to be optimal weight.')

Input()

#--------------------------
#Test 1

##Enter your weight in pounds: 146
##Enter your heigth in inches: 50
##Your BMI is 41.06  and is considerd to be over weight.

#-------------------------
#Test 2

##Enter your weight in pounds: 123
##Enter your heigth in inches: 70
##Your BMI is 17.65  and is considered to be under weight.

#-------------------------
#Test 3

##Enter your weight in pounds: 150
##Enter your heigth in inches: 65
##Your BMI is 24.96  and is considerd to be optimal weight.
