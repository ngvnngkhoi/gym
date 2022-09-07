'''
Author: Nguyen Van Nguyen Khoi
SID: 520526392
Unikey: vngu9798
'''
import math as mth                                              #import math library as math


valid_genders = ['male', 'female']                              #list of valid gender inputs    
val_chars = '~`!@#£€$¢¥§%°^&*()-_+={}[]|\/:;\"\'<>,.?'                #valid characters for input
i = 0  
name = (input('Please enter your name: '))                      #prompt user's name and save under name
while i <= len(name):                                           #initialize count control loop
    if len(name) <= 0:                                          #check for length of i 
        print('Error: Only accept alphabetical characters and spaces for name\n')
        name = (input('Please enter your name: '))
        continue
    if name[i].isalpha() or name[i].isspace():                  #check if string[i] is space or alphabet, if true--> continue
        i = i+1
    if i == len(name):                                          #if i reaches length of input with no disruption --> move next 
        break
    if any(x in val_chars for x in name):                       #check for invalid characters by looping through val_chars
        print('Error: Only accept alphabetical characters and spaces for name\n')
        name = (input('Please enter your name: '))
        continue
    if name[i].isdigit():                                       #check if string[i] is a digit, if true go back
        print('Error: Only accept alphabetical characters and spaces for name\n')
        name = (input('Please enter your name: '))
        i = 0
        continue

while True:                                                     #initalize event-controlled loop
    try:
        age = int(input('\nPlease enter your age: '))           #save age under age
    except ValueError:                                          #check for value error
        print('Error: Please enter valid input')
        continue
    if age < 0 or age > 110:                                    #check for range
        print('Error: The age is a number between 0 to 110')
        continue
    else: 
        break

while True:                                                     #same as age
    try: 
        gender = str(input('\nPlease enter your biological sex (female/male): '))
    except ValueError:
        break
    if gender not in valid_genders:
        print('Error: Please enter valid input')
        continue
    else:
        test = gender.upper()
        break

while True:                                                     #same as age
    try:
        print('''
What do you want to get out of your training? 
    1. Your goal is losing weight
    2. Your goal is to staying calm and relax
    3. Your goal is increasing your heart rate
    4. Your goal is having stronger legs
    5. Your goal is having stronger ABS
    6. Your goal is having stronger shoulders and arms''')
        selection = int(input('Choose a number between 1 to 6: '))      #selection variable is used to store the index # 
    except ValueError:
        print('Error: Please enter valid input\n')
        continue
    if selection < 1 or selection > 6:
        print('Error - It can only be a number between 1 to 6')
        continue
    else: 
        break
while True:                                                         #same as age
    try:
        days = int(input('\nHow many days per week you can train: '))
    except NameError:
        print('Error: It can only be a number between 1 to 7')
    if days > 7 or days <1:
        print('Error: It can only be a number between 1 to 7')
    else:
        break

percent = 1                                     #percent is set default to 1
if age == 60:                                   
    percent = 0.99
if age > 60 and age < 65:
    decrease = ((age - 60)/100)                 #decrease variable is used to control how percentage is decreased
    percent = percent - decrease
if age >= 65:
    percent = 0.95
if age > 65 and age < 75:
    decrease =((age-65) * 0.02) 
    percent = percent - decrease
if age >= 75:
    percent = 0.75
if age > 75 and age < 80:
    decrease = (age - 75)*0.03
    percent = percent - decrease
if age >= 80:
    percent = 0.6
if age > 80:
    decrease = (age - 80) * 0.04
    percent = percent - decrease
if percent < 0.2:
    percent = 0.2

numbers = [2,3,4,5,10,12,15,18,20,18]               #list of numbers for the excercises

wk1 =[                                              #list of workouts based on goals
f'''Gym workout for fat loss

Plate thrusters ({mth.ceil(numbers[6] *percent)} reps x {numbers[1]} sets)
Mountain climbers ({mth.ceil(numbers[8]* percent)} reps x {numbers[1]} sets)
Box jumps ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Lunges ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Renegade rows ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Press ups ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Treadmill ({mth.ceil(numbers[4]* percent)} mins x {numbers[1]} sets)
Supermans ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Crunches ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
'''
,f'''Gym workout for stretch and relax

Quad stretchs ({mth.ceil(numbers[0]* percent)} mins x {numbers[1]} sets)
Hamstring stretchs ({mth.ceil(numbers[0]* percent)} mins x {numbers[1]} sets)
Chest and shoulder stretchs ({mth.ceil(numbers[0]* percent)} mins x {numbers[0]} sets)
Upper back stretchs ({mth.ceil(numbers[1]* percent)} mins x {numbers[0]} sets)
Biceps stretchs ({mth.ceil(numbers[0]* percent)} mins x {numbers[0]} sets)
Triceps stretchs ({mth.ceil(numbers[0]* percent)} mins x {numbers[1]} sets)
Hip flexors ({mth.ceil(numbers[0]* percent)} mins x {numbers[1]} sets)
Calf stretchs ({mth.ceil(numbers[0]* percent)} mins x {numbers[1]} sets)
Lower back stretchs ({mth.ceil(numbers[0]* percent)} mins x {numbers[1]} sets)
'''
,
f'''Gym workout for high-intensity exercises

Jumping jacks ({mth.ceil(numbers[8]* percent)} reps x {numbers[2]} sets)
Sprints ({mth.ceil(numbers[8]* percent)} reps x {numbers[1]} sets)
Mountain climbers ({mth.ceil(numbers[8]* percent)} reps x {numbers[2]} sets)
Squat jumps ({mth.ceil(numbers[8]* percent)} reps x {numbers[2]} sets)
Lunges ({mth.ceil(numbers[8]* percent)} reps x {numbers[1]} sets)
Crunches ({mth.ceil(numbers[8]* percent)} reps x {numbers[1]} sets)
Treadmill ({mth.ceil(numbers[6]* percent)} mins x {numbers[0]} sets)
Side planks ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Burpees ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
'''
,
f'''Gym workout for strong legs

Back squats ({mth.ceil(numbers[4]* percent)} reps x {numbers[3]* percent} sets)
Hip thrusts ({mth.ceil(numbers[5]* percent)} reps x {numbers[1]* percent} sets)
Overhead presses ({mth.ceil(numbers[4]* percent)} reps x {numbers[3]* percent} sets)
Rack pulls ({mth.ceil(numbers[4]* percent)} reps x {numbers[3]* percent} sets)
Squats ({mth.ceil(numbers[4]* percent)} reps x {numbers[2]* percent} sets)
Dumbbell lunges ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]* percent} sets)
Leg curls ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]* percent} sets)
Standing calf raises ({mth.ceil(numbers[8]* percent)} reps x {numbers[0]* percent} sets)
'''
,
f'''Gym workout for strong ABS

Cross crunchs({mth.ceil(numbers[5]* percent)} reps x {numbers[1]} sets)
Knee ups ({mth.ceil(numbers[6]* percent)} reps x {numbers[3]} sets)
Hip thrusts ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Mountain climbers ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Vertical hip thrusts ({mth.ceil(numbers[5]* percent)} reps x {numbers[1]} sets)
Bicycles ({mth.ceil(numbers[6]* percent)} mins x {numbers[0]} sets)
Front planks ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Dragon flags ({mth.ceil(numbers[5]* percent)} reps x  {numbers[2]} sets)
Reverse crunches ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
'''
, 
f'''Gym workout for strong shoulder and arms

Bench presses ({mth.ceil(numbers[4]* percent)} reps x {numbers[3]} sets)
Triceps dips ({mth.ceil(numbers[4]* percent)} reps x {numbers[3]} sets)
Incline dumbbell presses ({mth.ceil(numbers[5]* percent)} reps x {numbers[1]} sets)
dumbbell flyes ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Triceps extensions ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Pull ups ({mth.ceil(numbers[4]* percent)} reps x {numbers[3]} sets)
Treadmill ({mth.ceil(numbers[6]* percent)} mins x {numbers[0]} sets)
Bent over rows ({mth.ceil(numbers[4]* percent)} reps x {numbers[3]} sets)
Chin ups ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
'''
]


wk2 = [                                                             #workout based on body type                                               
f'''Gym workout for a male younger than 18 years old

High knees ({mth.ceil(numbers[8]* percent)} reps x {numbers[1]} sets)
Squats ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Calf raises ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Scissor jumps({mth.ceil(numbers[5]* percent)} reps x {numbers[1]} sets)
Burpees ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Treadmill ({mth.ceil(numbers[4]* percent)} mins x {numbers[0]} sets)
'''
,
f'''Gym workout for a female younger than 18 years old

Squats ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Crunches ({mth.ceil(numbers[4]* percent)} mins x {numbers[0]} sets)
Jumping jacks ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Push ups ({mth.ceil(numbers[4]* percent)} mins x {numbers[0]} sets)
Burpees ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Treadmill ({mth.ceil(numbers[4]* percent)} mins x {numbers[0]} sets)
'''
,
f'''Gym workout for a male at least 18 years old

Standing biceps curls ({mth.ceil(numbers[8]* percent)} reps x {numbers[1]} sets)
Seated incline curls ({mth.ceil(numbers[7]* percent)} reps x {numbers[1]} sets)
Seated dumbbell presses ({mth.ceil(numbers[5]* percent)} reps x {numbers[1]} sets)
Leg presses ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Bench presses ({mth.ceil(numbers[4]* percent)} reps x {numbers[2]} sets)
Tricep kickbacks ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Hip thrusts ({mth.ceil(numbers[5]* percent)} reps x {numbers[1]} sets)
Seated rows ({mth.ceil(numbers[4]* percent)} reps x {numbers[2]} sets)
'''
,
f'''Gym workout for a female at least 18 years old

Lateral raises ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Reverse flyes ({mth.ceil(numbers[5]* percent)} reps x {numbers[1]} sets)
Hip thrusts ({mth.ceil(numbers[5]* percent)} reps x {numbers[1]} sets)
Incline dumbbell presses ({mth.ceil(numbers[6]* percent)} reps x {numbers[1]} sets)
Squats ({mth.ceil(numbers[4]* percent)} reps x {numbers[2]} sets)
Dumbbell lunges ({mth.ceil(numbers[4]* percent)} reps x {numbers[1]} sets)
Leg presses ({mth.ceil(numbers[5]* percent)} reps x {numbers[1]} sets)
Dumbbell presses ({mth.ceil(numbers[4]* percent)} reps x {numbers[2]} sets)
''' 
]

def excercises():                                       #output first workout by going through the list via selection variable
    ex1 = wk1[selection - 1]
    print(ex1 + '-'*85)
    

def extra():
    if age < 18 and test == "MALE":
        ex2 = wk2[0]
    if age >= 18 and test == "MALE":
        ex2 = wk2[2]
    if age < 18 and test == "FEMALE":
        ex2 = wk2[1]
    if age >= 18 and test == "FEMALE":
        ex2 = wk2[3]
    print(ex2 + '-'*85)

def output():
    print(f'\nHello {name}! Here is your training:'+'\n' + '-'*85)
    counter = 0
    while counter < days:
        counter = counter + 1
        if counter % 2 != 0:
            print(f'Day {counter}')
            excercises()
        if counter % 2 == 0:
            print(f'Day {counter}')
            extra()
    print(f'\nBye {name}.')


output()    





