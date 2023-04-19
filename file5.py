# list : collection str,flot,int, bool
# studData = [1,2,3.0,'Laxman',True]
# studData.insert(1,100)
# studData.extend([1000,2000,3000])
# studData.remove(1000)
# studData.remove("Laxman")
# studData.pop(3)
# studData.pop()
#studData.clear()
# lists = studData.copy()
#del studData
#lists.reverse()
#print(lists)
#print(lists[-2:])
# names = ['tukaram', 'chate']
#print(names)

"""
for i in range(len(names)-1,-1,-1):
    print(names[i],end=" ")
"""
#print(type(lists))
#print(type(str(lists)))
# names = ""
# for l in lists:
#     names += str(l)+" "
# print(names)
#print(studData)
# constructor :   list()
# how to loop list

"""
for i in studData:
    print(i,end=" ")

i = 0 
while i < len(studData):
    print(studData[i],end=" ")
    i+=1
"""

#print(studData[3])

#length = len(studData)
#print(length)





################################################################
# how to take input from console
# intput()
# raw_input() 3
# eval(input())


"""
name = input("Enter your name: ") # default string
print(type(name)) 
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
address = str(input("Enter your city name: "))
print(salary)
"""

################################################################

# if statement:
# if cont : statement
# if cond : stam else
#  collection list range tuple dict set




"""
name = "Laxman is a developer z"
print("While statement")
i = 0
while i < 10:
    print(i,end=" ")
    i+=1








num = 10
if num == 10:
    print('10',end="")
elif num == 8:
    print("9")
else:
    print("not found")





num = 10
if num == 10:
    print("find")
else:
    print("not found")

"""


"""
for i in range(10):
    print("*",end="")
num = int(input("Enter your number: "))
if num == 10:
    for i in range(num,0,-1):
        print(i,end=" ")
else:
    print("Not found!!")
"""




















# 1 3,5,7,11,13
# 1,3,5,7,9
"""
for i in range(pattrnum):
    for l in range(pattrnum-i):
        print(end=" ")
    for j in range(i*2-1):
        print("*",end="")
    print()


for i in range(pattrnum):
    for s in range(i): 
        print(" ",end="")
    for j in range(pattrnum):
        print("*",end=" ")
    print()
   
for i in range(pattrnum):
    for s in range(pattrnum-i): 
        print(" ",end="")
    for j in range(pattrnum):
        print("*",end=" ")
    print()
  
  
pattrnum = 7  
for i in range(pattrnum):
    for j in range(pattrnum-i):
        print("*",end=" ")
    print()
    """