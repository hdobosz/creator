# ## Task 1

number_one=int(input('First number: '))
number_two=int(input('Second number: '))
number_three=int(input('Thierd number: '))
number_one
sum=number_one + number_two + number_three
print(sum)

# ## Task 2

number_one=int(input('first number'))
number_two=int(input('second number'))

if number_one and number_two> 10000:
    print('numbers are big')  

elif number_one>number_two:
    print('first number is greater') 

elif number_one<number_two:
    print('second number is greater')   

elif number_one==number_two:
    print('equal')    

# ## Task 3

num1=input('Enter number: ')
num2=input('Enter number: ')
num3=input('Enter number: ')
num4=input('Enter number: ')
num5=input('Enter number: ')
print()
print('Maximum of the number is: ',max(num1,num2,num3,num4,num5))

# ## Task 4

name=input('Month: ')
      
if name=='Januar':
    print('Number of days: 31 days')
elif name=='Februar':
    print('Number of days: 28 days')
elif name=='März':
    print('Number of days: 31 days')
elif name=='April':
    print('Number of days: 30 days')
elif name=='Mai':
    print('Number of days: 31 days')
elif name=='Juni':
    print('Number of days: 30 days')
elif name=='Juli':
    print('Number of days: 31 days')
elif name=='August':
    print('Number of days: 31 days')
elif name=='September':
    print('Number of days: 30 days')
elif name=='Oktober':
    print('Number of days: 31 days')
elif name=='November':
    print('Number of days: 30 days')
elif name=='Dezember':
    print('Number of days: 31 days')


# ## Task 5

numb=int(input('Number: '))
num=3

if numb % 2:
    print(numb, 'is uneven' )
else:
    print(numb, 'is even')

if numb%num==0:
    print('and divisible by 3')
else:
    print('and undivisible by 3')     