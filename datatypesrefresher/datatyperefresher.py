p = "Hello India"
q = 10
r = 10.2
print(type(p))
print(type(q))
print(type(r))
print(type(12+31j))
print(type(bool(0)))
print(bool(1))
print(type(True))
print(type(False))

str1 = 'Hello how are you'
str2 = "Hello how are you"
str3 = """multiline 
       String"""
print(str1)
print(str2)
print(str3)

f = 'data' 
s = 'structure'
print(f + s)
print('Data ' + 'structure')


st = 'data.'
print(st * 3)
print(4 * st)

print(list(range(10)))
print(range(10))
print(list(range(10)))
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(20,10,-2)))


a = ['food', 'bus', 'apple', 'queen']
print(a)
mylist  = [10, "India", "world", 8] 
# accessing elements in list.
print(mylist[1])

a = ['data', 'apple','app','structures', 'using', 'python', 'happy', 'learning']
print('dat' in a)
print("this is ",a)
print(a + ['New', 'elements'])
print(a *2)
print(len(a))
print(min(a))


mylist1 = [100,20,10,30,40]
mylist2 = [10,50,60,90,100,20]
if mylist1[1] in mylist2:
    print("elements are overlapping") 
else:
    print("elements are not overlapping")


person = {}
print(type(person))
person['name'] = 'ABC'
person['lastname'] = 'XYZ'
person['age'] = 31
person['address'] = ['Jaipur']
print(person)
print(person['name'])