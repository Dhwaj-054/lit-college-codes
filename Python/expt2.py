# python lab expt 2 codes

# Python program to demonstrate
# Creation of List

# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])
Blank List: 
[]

List of numbers: 
[10, 20, 14]

List Items: 
Geeks
Geeks

# Creating a List with the use of Numbers (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)
 # Creating a List with  mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Name', 4, 'Dhwaj', 6, 'Jain']
print("\nList with the use of Mixed Values: ")
print(List)
List with the use of Numbers: 
[1, 2, 4, 4, 3, 3, 3, 6, 5]

List with the use of Mixed Values: 
[1, 2, 'Name', 4, 'Dhwaj', 6, 'Jain']
# Python program to demonstrate # accessing of element from list
 # Creating a List with the use of multiple values
List = ["Hello", "World"]
 # accessing a element from the list using index number
print("Accessing a element from the list")
print(List[0])
print(List[1])
Accessing a element from the list
Hello
World


# Creating a Multi-Dimensional List # (By Nesting a list inside a List)
List = [['Hello', 'World'], ['Heyyy']]
 # accessing an element from the # Multi-Dimensional List using # index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])
Accessing a element from a Multi-Dimensional list
World
Heyyy
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
 # accessing an element using negative indexing
print("Accessing element using negative indexing")
 # print the last element of list
print(List[-1])
 # print the third last element of list
print(List[-3])
Accessing element using negative indexing
Geeks
For
# Creating a List
List1 = []
print(len(List1))
 # Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))
0
3
# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List using Iterator
for i in range(1, 4):
  List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
Initial blank List: 
[]

List after Addition of Three elements: 
[1, 2, 4]

List after Addition of elements from 1-3: 
[1, 2, 4, 1, 2, 3]

List after Addition of a Tuple: 
[1, 2, 4, 1, 2, 3, (5, 6)]

List after Addition of a List: 
[1, 2, 4, 1, 2, 3, (5, 6), ['For', 'Geeks']]
List = [1,2,3,4]
print("Initial List: ")
print(List)

# Addition of Element at specific Position (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)
Initial List: 
[1, 2, 3, 4]

List after performing Insert Operation: 
['Geeks', 1, 2, 3, 12, 4]
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)
 # Addition of multiple elements to the List at the end (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)
Initial List: 
[1, 2, 3, 4]

List after performing Extend Operation: 
[1, 2, 3, 4, 8, 'Geeks', 'Always']
# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)
Tuple with the use of String: 
('Geeks', 'For')

Tuple using List: 
(1, 2, 4, 5, 6)

Tuple with the use of function: 
('G', 'e', 'e', 'k', 's')
# Creating a Tuple# with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)
# Creating a Tuple# with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)
# Creating a Tuple# with repetition
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1)
Tuple with Mixed Datatypes: 
(5, 'Welcome', 7, 'Geeks')

Tuple with nested tuples: 
((0, 1, 2, 3), ('python', 'geek'))

Tuple with repetition: 
('Geeks', 'Geeks', 'Geeks')
# Accessing Tuple
Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple1[0])

# Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")

# This line unpack
# values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)
First element of Tuple: 
G

Values after unpacking: 
Geeks
For
Geeks


Implement a program to store a matrix using nested list and fetch index element of matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def fetch_element(matrix, row, col):
    if row < len(matrix) and col < len(matrix[0]):
        return matrix[row][col]
    else:
        return "Index out of bounds"

print("Matrix:")
for row in matrix:
    print(row)

print("\nFetching elements:")
print("Element at (0, 0):", fetch_element(matrix, 0, 0))
print("Element at (1, 1):", fetch_element(matrix, 1, 1))
print("Element at (2, 2):", fetch_element(matrix, 2, 2))
print("Element at (3, 3):", fetch_element(matrix, 3, 3))
Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Fetching elements:
Element at (0, 0): 1
Element at (1, 1): 5
Element at (2, 2): 9
Element at (3, 3): Index out of bounds
Create a list of 10 random players in football team. Perform following operations on list and discuss on each output. Display list, Sorts the list, use remove to Remove the first item with the specified value

players = ['player1','player9','player3','player10','player5','player6','player7','player8','player2','player4']

print("Players List : ")
print(players)

players.sort()
print("\nSorted List : ")
print(players)

players.remove('player2')
print("\nList after removing player2 : ")
print(players)
Players List : 
['player1', 'player9', 'player3', 'player10', 'player5', 'player6', 'player7', 'player8', 'player2', 'player4']

Sorted List : 
['player1', 'player10', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9']

List after removing player2 : 
['player1', 'player10', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9']
Write a program to randomly select 10 integer elements from range 100 to 200 and find the minimum and maximum among all.

import random

numbers = list(random.sample(range(100, 201),10))

print("Randomly selected numbers : ")
print(numbers)

print("\nMinimum number : ", min(numbers))
print("Maximum number : ", max(numbers))
Randomly selected numbers : 
[190, 170, 114, 157, 186, 119, 181, 124, 195, 180]

Minimum number :  114
Maximum number :  195
Create a dictionary of 5 countries with their currency details and display them

countries = {
    "USA": {"currency": "US Dollar", "code": "USD"},
    "India": {"currency": "Indian Rupee", "code": "INR"},
    "Japan": {"currency": "Japanese Yen", "code": "JPY"},
    "UK": {"currency": "Pound Sterling", "code": "GBP"},
    "Brazil": {"currency": "Real", "code": "BRL"}
}

print("Countries and their Currency Details:")
for country, details in countries.items():
    print(country+":")
    print("\tCurrency: ",details['currency'])
    print("\tCode: ",details['code'])
Countries and their Currency Details:
USA:
	Currency:  US Dollar
	Code:  USD
India:
	Currency:  Indian Rupee
	Code:  INR
Japan:
	Currency:  Japanese Yen
	Code:  JPY
UK:
	Currency:  Pound Sterling
	Code:  GBP
Brazil:
	Currency:  Real
	Code:  BRL
