# collection list
# insert(postion, items), append('items'), remove(item_name), extend(iterable)
# remove, pop, del, clear
mytuple = (1,2,3,45)
empName = [1,2,3,4,5,6]
stud = ['laxman', 'tukaram']
stud.extend(empName)
stud.extend(mytuple)

#stud.remove('laxman');
#stud.pop(0)
#stud.pop()
#del stud[0]
# del stud[1]
#del stud[len(stud)-1]
stud.clear()
print(stud)
#print(stud)


#print(stud[1:3])
#print(stud[:5])
#print(stud[5:])
#print(stud[-3:])


"""
print(stud)
for i in range(len(stud)):
    if i == 0 :
        pass
    elif  i % 2 == 0:
        print(stud[i]," index ",i)
"""

"""
for i in range(len(stud)):
    print(stud[i], end=" ")
#print(empName)
"""





"""
print(age)
age.insert(2,'laxman')
print(age)
listlen = len(age)
age.insert(listlen,"Tukaram")
print(age)
listlen = len(age)
print(listlen)
age.append(200)
age.append(100)
print(age)
# insert, append, remove
age.remove(100)
age.remove(200)
print(age)


for i in age:
    if i == "Tukaram":
        print("Found")    
    else:
        pass

"""

# to printing satement
# print("tukaram chate")or print('tukaram chate')
# to declare variable: variable = ""
"""
for i in range(4):   
    for j in range(4):
        print('*',end="")
    print()
"""
"""
for i in range(4): 
    for j in range(4): 
        if i == 0 or i == 0 or j == 0 or j == 3-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


for i in range(4): 
    for j in range(4): 
        if i == 0 or i == 4-1 or j == 0 or j == 4-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    """