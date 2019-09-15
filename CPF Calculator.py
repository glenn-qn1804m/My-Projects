name = str(input("what is your name: ").upper())
age = int(input('what is your age: '))
years = 65 - age

if age < 65:
    print(f'You will receive your CPF in {years} years.')
    if age % 2 == 0:
        print(f'Your name is {name}')
    else:
        print(f'Your age is {age}')
else:
    print("You have already received your CPF!")
