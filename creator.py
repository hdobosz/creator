import random
print("*********************************")
print("welcom to the character generater!")
print("Let's name the brave adventurers:")
name1=input("character1:")
name2=input("character2:")
name3=input("character3:")
name4=input("character4:")
name5=input("character5:")
name1_num= random.randint(1,3)
name2_num= random.randint(1,3)
name3_num= random.randint(1,3)
name4_num= random.randint(1,3)
name5_num= random.randint(1,3)
print("Enough name!!!")
############################name1
if (name1_num == 1):
    print(name1,"is a Wizard")
    health=random.randint(5,10)
    print("health =" ,health)
    strength=random.randint(5,10)
    print("strength =",strength)
    magic=3*random.randint(5,10)
    print("magic is =" ,magic)
if (name1_num == 2):
    print(name2,"is a Warrior")
    health=random.randint(5,10)
    print("health =" ,health)
    strength=3*random.randint(5,10)
    print("strength =",strength)
    magic=random.randint(5,10)
    print("magic is =" ,magic)
if (name1_num == 3):
    print(name3,"is a potato")
    health=random.randint(5,10)
    print("health =" ,3*health)
    strength=random.randint(5,10)
    print("strength =",strength)
    magic=random.randint(5,10)
    print("magic is =" ,magic)