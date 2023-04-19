"""
old_age = input("enter  the your age")
int()
float()
str()
bool()

first = input("enter the first no :")
second = input("enter the second no :")
sum = int(first) + int(second)
print("the sum is : " +str(sum))

# string
# 0123 index
name = "tukaram chate is the student of raisoni college"
print(name.upper())
print(name.lower())
print(name)
name = "tukaram chate is the student of raisoni college"
#print(name.find('ll'))
# index 
print(name)
print(name.replace("tukaram chate", "vipin patil"))
"""
#arithmatic oprator
#print(5 ** 2)
# + - * / 
# // is remove after point value
# % remainder
# **  for the power 
"""
i = 5
i = i + 2
i += 2

# comprasion oprator
# < , > , == , !=
print( 5 < 3)
print( 3 == 4)
"""
#logical oprator
# or and not
#print( 4 > 5 or 4 < 5)
#if else
"""
if(condition):
    print("statement")
elif(condition):
    print("statement")    
else:
    print("statement")      

# mini project cal
first = int(input("enter the first number : "))
second = int(input("enter the second number : "))
oprator = input("enter operator (+,-,*,/,%) :")
"""
# range(5)
# while loop
"""
i =1 
while i <= 100:
    print(i)
    i = i +1

i = 1
while i <=10:
    print(i * "*")
    i = i +1

i = int(input("enter the number"))
while i >=0:
    print(i * "*")
    i = i - 1


for item in range(5):
    print("*")

"""
# list: is the collection of data
marks =[98,84,"tukaram"]
#print(marks)
#print(marks[2])
#print(marks[-1])
#print(marks[1:2])
#marks.append(12)
#print(marks)
"""
marks.insert(11,2)
print(marks)
print(98 in marks)
print(len(marks))


# [] list () tuple {} set
#break and continue
students = ["tukaram", "yash", "ram", "shyam"]

for student in students:
    if student == "yash":
        break;
    print(students)

students = ["ram", "shyam", "kishan", "radha", "radhika"]
for student in students:
    if(student == "radha"):
       continue;
    print(student)
"""
# tuple no modified 
# marks = ()
marks = (12,3,14,15,16)

#set
#num = {1,2,3,1,2,1,4,5,6,3,}
























