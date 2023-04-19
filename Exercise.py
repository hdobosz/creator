## Task 1

number_one=int(input('First number: '))
number_two=int(input('Second number: '))
number_three=int(input('Thierd number: '))
number_one
sum=number_one + number_two + number_three
print(sum)

## Task 2

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

## Task 3

num1=input('erste')
num2=input('zweite')
num3=input('dritte')
num4=input('vierte')
num5=input('fünfte')
print()
print('Maximum of the number is: ',max(num1,num2,num3,num4,num5))

## Task 4

name=input('Month: ')
print('Number of days:')
      
if name=='Januar':
    print('31 days')
elif name=='Februar':
    print('28 days')
elif name=='März':
    print('30 days')
elif name=='April':
    print('30 days')
elif name=='Mai':
    print('31 days')
elif name==Juni:
    print('30 days')
elif name=='Juli':
    print('31 days')
elif name=='August':
    print('31 days')
elif name=='September':
    print('30 days')
elif name=='Oktober':
    print('31 days')
elif name=='November':
    print('30 days')
elif name=='Dezember':
    print('31 days')


## Task 5

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