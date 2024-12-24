# list
#Removing elements
items = ["book","pen","bat","ball",]
print(items)
items.pop()
print(items)
items.remove("pen")
print(items)

#adding elements
items.append("pencil")
print(items)
items.insert(1,"pencil")
print(items)

#clear all elements
items.clear()
print(items)

#slicing list
num = [0, 10, 24, 37, 46, 57, 645]
print(num[1:4])  
print(num[:4])  
print(num[2:])  
print(num[::2]) 

#list function
fruits = ["orange","bannana","mango"]
print(len(fruits)) 

numbers = [5, 2, 9, 1]
print(sorted(numbers)) 
print(numbers.reverse()) 
print(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers)) 

print(fruits.index("bannana"))

#nested list
matrix = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]

print(matrix[2]) 
print(matrix[0][2])



