# inputs
# km = float(input('Please enter a number of kilometers: '))
# miles = km / 1.609344
# print(km, 'km = ', round(miles, 3), 'miles')

# strings
# first = input('Please enter your first name: ')
# middle = input('Please enter your middle name: ')
# last = input('Please enter your last name: ')
# print ('Your initials are', first[0],middle[0],last[0])

# lot_number = '037-00901-00027'
# print('Country Code:', lot_number[0:3])
# print('Product Code:', lot_number[4:9])
# print('Batch Number:', lot_number[10:])
 
# numbers
# import math
# radius = float(input('Please enter a radius: '))
# area = math.pi * (radius ** 2)
# circumference = 2 * math.pi * radius
# print('The area of the circle is ', round(area, 2), 'and the circumference is', round(circumference, 2))

# students = ['John', 'Mary', 'Steve']
# print(students[len(students)-1])
# print(students[0:2])

# Lists and Tuples
# months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
# birthdate = input('Please input your birthday in the following format DD-MM-YYYY: ')
# month_number = int(birthdate[3:5])-1
# month_name = months[month_number]
# print('You were born in', month_name)

# people = ['JBJ', 'Joseph', 'Joel']
# new_person = input('Please enter your name: ')
# people.append(new_person)
# print(people)

# Dictionaries

# person = { 'first_name': 'John', 'last_name': 'Green', 'children': ['Natalie', 'Ethan']}
# person['children'].append('Robbie')
# print(person)


# person = {'name': 'JBJ', "gender": 'NB', 'age': 41, 'address': '234 Main St', 'phone': '867-5309'}

# getter = input('What information do you want? ')
# info = person.get(getter, 'That information is not available')
# print(info)

# booleans
age = 41
user_age = float(input('What is your age? '))
if (age > user_age):
  print('I am older')
if (age < user_age):
  print('You are older')
if (age == user_age): 
  print('We are the same age.')